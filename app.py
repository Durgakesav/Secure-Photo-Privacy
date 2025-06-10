from flask import Flask, request, render_template, jsonify, redirect, url_for, flash, send_from_directory
from flask_login import login_required, current_user, login_user, logout_user
from database import db, bcrypt, login_manager, create_app
from models import User, Image
from image_processing import apply_filter
import os
import steganography
from steganography import hide_message, extract_message  # Import steganography functions
from face_recognition import register_face, verify_face  # Import Face Recognition Functions
from flask_babel import Babel, gettext as _
from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import secrets
from datetime import timedelta

# Initialize Flask app app by kesav
app = create_app()

# Security headers and CSP
csp = {
    'default-src': "'self'",
    'script-src': "'self' 'unsafe-inline' 'unsafe-eval'",
    'style-src': "'self' 'unsafe-inline'",
    'img-src': "'self' data: https:",
    'font-src': "'self' https://fonts.gstatic.com",
    'connect-src': "'self'"
}

# Initialize Talisman with security headers

Talisman(app, 
    content_security_policy=csp,
    force_https=True,
    strict_transport_security=True,
    session_cookie_secure=True,
    session_cookie_http_only=True
)

# Initialize Babel for internationalization
babel = Babel(app)

# Initialize rate limiter
limiter = Limiter(
    app,
    default_limits=["200 per day", "50 per hour"]
)

# Configure supported languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español',
    'fr': 'Français',
    'de': 'Deutsch',
    'zh': '中文',
    'ja': '日本語',
    'ar': 'العربية'
}


# Create required directories
UPLOAD_FOLDER = os.path.join(os.getcwd(), "static", "uploads")
FILTERED_FOLDER = os.path.join(os.getcwd(), "static", "filtered")
FACES_FOLDER = os.path.join(os.getcwd(), "static", "faces")
TEMP_FOLDER = os.path.join(os.getcwd(), "static", "temp")

# Create directories if they don't exist
for folder in [UPLOAD_FOLDER, FILTERED_FOLDER, FACES_FOLDER, TEMP_FOLDER]:
    os.makedirs(folder, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["FILTERED_FOLDER"] = FILTERED_FOLDER
app.config["FACES_FOLDER"] = FACES_FOLDER
app.config["TEMP_FOLDER"] = TEMP_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max file size
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=1)
app.config["SESSION_COOKIE_SECURE"] = True
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

# Clean up temp files on startup
for file in os.listdir(TEMP_FOLDER):
    try:
        os.remove(os.path.join(TEMP_FOLDER, file))
    except:
        pass

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# Home Page Route
@app.route('/')
def home():
    return render_template("index.html")

# User Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']
            password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
            
            # Check if face image was uploaded
            if 'face_image' not in request.files:
                return jsonify({"error": "No face image provided"}), 400
                
            face_image = request.files['face_image']
            if face_image.filename == '':
                return jsonify({"error": "No face image selected"}), 400
                
            # Check file type
            if not face_image.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                return jsonify({"error": "Invalid file type. Please upload a PNG, JPG, or JPEG image."}), 400

            # Create new user
            new_user = User(username=username, email=email, password=password)
            
            with app.app_context():
                db.session.add(new_user)
                db.session.commit()
                
                # Get the user ID after commit
                user_id = new_user.id
                
                # Save the face image temporarily
                temp_face_path = os.path.join(app.config["TEMP_FOLDER"], f"temp_face_{user_id}.jpg")
                face_image.save(temp_face_path)
                
                # Register the face
                success, message = register_face(user_id, temp_face_path)
                
                # Clean up temp file
                try:
                    os.remove(temp_face_path)
                except:
                    pass
                
                if not success:
                    # If face registration fails, delete the user
                    db.session.delete(new_user)
                    db.session.commit()
                    return jsonify({"error": message}), 400
                
                flash('Signup successful! Please log in.', 'success')
                return jsonify({"message": "Signup successful"}), 200
                
        except Exception as e:
            return jsonify({"error": f"Error during signup: {str(e)}"}), 500
    
    return render_template('signup.html')

# Image Editing Route
@app.route("/edit_image/<int:image_id>", methods=['GET', 'POST'])
@login_required
def edit_image(image_id):
    image = Image.query.filter_by(id=image_id, user_id=current_user.id).first()
    if not image:
        return jsonify({"error": "Image not found"}), 404

    filtered_filename = None  

    if request.method == 'POST':
        filter_type = request.form.get("filter_type")
        original_path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
        filtered_filename = f"filtered_{image.filename}"
        filtered_path = os.path.join(app.config["FILTERED_FOLDER"], filtered_filename)

        # Apply the filter
        success = apply_filter(original_path, filtered_path, filter_type)

        if success:
            return render_template("edit_image.html", image=image, filtered_image=filtered_filename)
        else:
            return jsonify({"error": "Failed to apply filter"}), 500

    return render_template("edit_image.html", image=image, filtered_image=None)

# User Login Route
# ✅ Route to Register User Face
@app.route("/register_face", methods=["POST"])
@login_required
def register_user_face():
    try:
        if "file" not in request.files:
            return jsonify({"error": "❌ No file provided"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "❌ No file selected"}), 400

        # Check file type
        if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            return jsonify({"error": "❌ Invalid file type. Please upload a PNG, JPG, or JPEG image."}), 400

        # Create faces directory if it doesn't exist
        faces_dir = os.path.join("static", "faces")
        os.makedirs(faces_dir, exist_ok=True)

        # Save the uploaded image
        image_path = os.path.join(faces_dir, f"user_{current_user.id}.jpg")
        file.save(image_path)

        # Register face
        success, message = register_face(current_user.id, image_path)

        if success:
            return jsonify({"message": message}), 200
        else:
            # Clean up the saved image if registration fails
            try:
                os.remove(image_path)
            except:
                pass
            return jsonify({"error": message}), 400

    except Exception as e:
        return jsonify({"error": f"❌ Error during face registration: {str(e)}"}), 500

# ✅ Route to Verify Face Before Hiding/Extracting Messages
@app.route("/verify_face", methods=["POST"])
@login_required
def verify_user_face():
    try:
        if "file" not in request.files:
            return jsonify({"error": "❌ No file uploaded!"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "❌ No file selected!"}), 400

        # Check file type
        if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            return jsonify({"error": "❌ Invalid file type. Please upload a PNG, JPG, or JPEG image."}), 400

        # Create temp directory if it doesn't exist
        temp_dir = os.path.join("static", "temp")
        os.makedirs(temp_dir, exist_ok=True)

        # Save temporary file
        temp_image_path = os.path.join(temp_dir, f"temp_face_{current_user.id}.jpg")
        file.save(temp_image_path)

        # Verify face
        match, message = verify_face(current_user.id, temp_image_path)
        
        # Clean up temp file
        try:
            os.remove(temp_image_path)
        except:
            pass

        if match:
            return jsonify({"message": message, "verified": True}), 200
        else:
            return jsonify({"error": message, "verified": False}), 400

    except Exception as e:
        return jsonify({"error": f"❌ Error during face verification: {str(e)}"}), 500

    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        with app.app_context():
            user = User.query.filter_by(email=email).first()
        
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('my_images'))  
        else:
            flash('Login Failed. Check email and password.', 'danger')
    
    return render_template('login.html')

# User Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# Image Upload Route
@app.route('/upload', methods=['POST'])
@login_required
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    is_public = request.form.get('is_public') == 'true'
    
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    new_image = Image(filename=file.filename, user_id=current_user.id, is_public=is_public)
    
    try:
        with app.app_context():
            db.session.add(new_image)
            db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Database error: {str(e)}"}), 500

    return jsonify({"message": f"File '{file.filename}' uploaded successfully!"}), 200

# User's Images Route
@app.route('/my_images')
@login_required
def my_images():
    with app.app_context():
        user_images = db.session.query(Image).filter_by(user_id=current_user.id).all()  
        return render_template('my_images.html', images=user_images)

# Delete Image Route
@app.route('/delete_image/<int:image_id>', methods=['POST'])
@login_required
def delete_image(image_id):
    with app.app_context():
        image = Image.query.filter_by(id=image_id, user_id=current_user.id).first_or_404()
        
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
        if os.path.exists(file_path):
            os.remove(file_path)
        
        db.session.delete(image)
        db.session.commit()

        return jsonify({"message": "Image deleted successfully"}), 200


@app.route('/update_privacy/<int:image_id>', methods=['POST'])
@login_required
def update_privacy(image_id):
    with app.app_context():
        image = Image.query.filter_by(id=image_id, user_id=current_user.id).first()

        if not image:
            return jsonify({"error": "Image not found"}), 404

        # Toggle privacy setting
        image.is_public = not image.is_public  
        db.session.commit()
        
        # Return updated status
        return jsonify({"message": "Privacy updated successfully", "new_status": "Public" if image.is_public else "Private"}), 200



# Route to Download Original Images from Public Gallery
@app.route("/download_image/<filename>")
def download_image(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)

# Route to Download Filtered Images
@app.route("/download_filtered/<filename>")
@login_required
def download_filtered_image(filename):
    return send_from_directory(app.config["FILTERED_FOLDER"], filename, as_attachment=True)


@app.route("/download_filtered/<filename>")
@login_required
def download_filtered(filename):
    return send_from_directory(app.config["FILTERED_FOLDER"], filename, as_attachment=True)




# Route to Download Images from Public Gallery


# Public Gallery Route
@app.route("/public_gallery")
def public_gallery():
    with app.app_context():
        # Use eager loading to fetch the owner relationship
        public_images = db.session.query(Image).options(db.joinedload(Image.owner)).filter_by(is_public=True).all()
        return render_template("public_gallery.html", images=public_images)

# Route to Hide Message in Image
@app.route("/hide_message/<int:image_id>", methods=["POST"])
@login_required
def hide_message_route(image_id):
    image = Image.query.filter_by(id=image_id, user_id=current_user.id).first()
    if not image:
        return jsonify({"error": "Image not found"}), 404

    message = request.form.get("message")
    if not message:
        return jsonify({"error": "No message provided"}), 400

    stego_image_path = hide_message(image.filename, message)  # Call the steganography function

    if stego_image_path is None:
        return jsonify({"error": "Failed to hide message in image"}), 500

    return jsonify({
        "message": "Message hidden successfully",
        "stego_image": os.path.basename(stego_image_path)  # Extract filename only
    })

# ✅ Route to Extract Message from Image
@app.route('/extract_message/<int:image_id>', methods=['GET'])
@login_required
def extract_message_route(image_id):
    image = Image.query.filter_by(id=image_id, user_id=current_user.id).first()
    if not image:
        return jsonify({"error": "Image not found"}), 404

    stego_filename = f"stego_{image.filename}"
    extracted_message = extract_message(stego_filename)

    return jsonify({"extracted_message": extracted_message})

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
