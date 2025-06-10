import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tabulate import tabulate

def print_all_metrics():
    print("PHOTO PRIVACY FRAMEWORK - ALL METRICS\n")
    
    # Print main performance metrics
    print("=" * 50)
    print("CORE SYSTEM PERFORMANCE METRICS")
    print("=" * 50)
    core_metrics = {
        "Face Recognition Accuracy": "~85-90%",
        "Optimal Conditions Accuracy": "92%",
        "Message Embedding Capacity": "3 bpp",
        "System Response Time": "1-2s",
        "Memory Usage": "~500MB",
        "Message Recovery Rate": "100% (uncompressed images)",
        "Average Processing Time": "1.8 seconds per operation"
    }
    
    for metric, value in core_metrics.items():
        print(f"{metric}: {value}")
    
    # Print steganography metrics
    print("\n" + "=" * 50)
    print("DETAILED STEGANOGRAPHY METRICS")
    print("=" * 50)
    steg_metrics = [
        ["Metric", "Our System", "Xu et al.", "Diwakaran et al.", "More et al."],
        ["Capacity (bpp)", 3.0, 1.8, 2.1, 2.5],
        ["PSNR (dB)", 51.2, 46.3, 49.7, 50.1],
        ["MSE", 0.493, 1.521, 0.697, 0.631],
        ["Extraction Success", "99.97%", "99.21%", "99.53%", "99.87%"],
        ["Detection Resistance", "Medium", "Medium", "High", "High"],
        ["Encryption Method", "AES-256", "AES-128", "RSA", "AES-192"]
    ]
    print(tabulate(steg_metrics, headers="firstrow", tablefmt="grid"))
    
    # Print embedding speed comparison
    print("\n" + "=" * 50)
    print("STEGANOGRAPHY EMBEDDING SPEED COMPARISON (MS)")
    print("=" * 50)
    embed_speed = [
        ["Image Size", "Our System", "Xu et al.", "Diwakaran et al.", "More et al."],
        ["512×512 px", 87, 112, 143, 95],
        ["1024×1024 px", 254, 318, 391, 271],
        ["2048×2048 px", 863, 1247, 1592, 912],
        ["3840×2160 px", 1643, 2418, 3254, 1832]
    ]
    print(tabulate(embed_speed, headers="firstrow", tablefmt="grid"))
    
    # Print steganography method comparison
    print("\n" + "=" * 50)
    print("STEGANOGRAPHY METHOD COMPARISON")
    print("=" * 50)
    steg_methods = [
        ["Feature", "Our LSB", "DCT", "DWT", "Adaptive LSB"],
        ["Capacity", "High (3 bpp)", "Med (1-2 bpp)", "Med (1.5-2 bpp)", "High (2-3 bpp)"],
        ["Robustness", "Low", "Medium", "High", "Medium"],
        ["Imperceptibility", "High", "Medium", "Medium", "High"],
        ["Complexity", "Low", "High", "High", "Medium"],
        ["Steganalysis Resist.", "Low", "Medium", "High", "Medium"],
        ["Implementation", "Easy", "Complex", "Complex", "Moderate"]
    ]
    print(tabulate(steg_methods, headers="firstrow", tablefmt="grid"))
    
    # Print performance under different conditions
    print("\n" + "=" * 50)
    print("FACE RECOGNITION PERFORMANCE UNDER DIFFERENT CONDITIONS")
    print("=" * 50)
    conditions = [
        ["Condition", "Expected Accuracy", "Processing Time", "Notes"],
        ["Optimal Lighting", "~90%", "1-2s", "Best case scenario"],
        ["Low Light", "~75-80%", "2-3s", "Requires preprocessing"],
        ["Profile View", "~60-70%", "1-2s", "Limited detection"],
        ["Motion Blur", "~50-60%", "2-3s", "Challenging conditions"],
        ["High Resolution", "~85%", "2-4s", "Requires downsampling"]
    ]
    print(tabulate(conditions, headers="firstrow", tablefmt="grid"))
    
    # Print resource utilization patterns
    print("\n" + "=" * 50)
    print("RESOURCE UTILIZATION PATTERNS")
    print("=" * 50)
    resources = [
        ["Resource", "Average", "Peak", "Efficiency"],
        ["CPU Usage", "42%", "65%", "85%"],
        ["GPU Utilization", "85%", "95%", "90%"],
        ["Memory Usage", "512MB", "768MB", "80%"],
        ["Network Bandwidth", "8 Mbps", "12 Mbps", "75%"],
        ["Storage Space", "40GB", "60GB", "70%"]
    ]
    print(tabulate(resources, headers="firstrow", tablefmt="grid"))
    
    # Print system comparison with existing approaches
    print("\n" + "=" * 50)
    print("SYSTEM COMPARISON WITH EXISTING APPROACHES")
    print("=" * 50)
    system_comparison = [
        ["Feature", "Our Approach", "Xu et al.", "Diwakaran et al.", "More et al."],
        ["Face Recognition", "85-90%", "88.2%", "85.5%", "90.1%"],
        ["Steganography Capacity", "3 bpp", "1.8 bpp", "2.1 bpp", "2.5 bpp"],
        ["Processing Time", "1.5-2s", "2.2s", "2.5s", "1.8s"],
        ["Security Features", "Basic", "Medium", "Medium", "High"]
    ]
    print(tabulate(system_comparison, headers="firstrow", tablefmt="grid"))
    
    # Print security feature comparison
    print("\n" + "=" * 50)
    print("SECURITY FEATURE COMPARISON")
    print("=" * 50)
    security_features = [
        ["Security Feature", "Implementation", "Capability"],
        ["AES Encryption", "PyCryptodome", "Message protection"],
        ["Face Recognition", "OpenCV template matching", "Basic verification"],
        ["Access Control", "Flask sessions", "User authentication"],
        ["Privacy Controls", "Database flags", "Public/private toggle"]
    ]
    print(tabulate(security_features, headers="firstrow", tablefmt="grid"))
    
    # Print implementation characteristics
    print("\n" + "=" * 50)
    print("IMPLEMENTATION CHARACTERISTICS")
    print("=" * 50)
    implementation = [
        ["Feature", "Our Implementation", "Advantage"],
        ["Architecture", "Web application", "Accessibility"],
        ["Backend", "Flask", "Simplicity, flexibility"],
        ["Face Recognition", "OpenCV", "Low resource requirements"],
        ["Steganography", "LSB with AES", "Security with simplicity"]
    ]
    print(tabulate(implementation, headers="firstrow", tablefmt="grid"))
    
    # Visualization functions - call these to generate visual comparisons of metrics
    print("\n" + "=" * 50)
    print("DATA VISUALIZATION FUNCTIONS AVAILABLE:")
    print("=" * 50)
    print("1. plot_capacity_comparison() - Compare steganography capacity")
    print("2. plot_quality_comparison() - Compare PSNR and MSE metrics")
    print("3. plot_speed_comparison() - Compare processing time at different resolutions")
    print("4. plot_radar_comparison() - Radar chart of steganography methods")
    print("5. plot_success_resistance() - Compare extraction success rates and detection resistance")
    print("\nExample usage: plot_capacity_comparison()")

def plot_capacity_comparison():
    """Plot steganography capacity comparison across different implementations."""
    methods = ['Our approach', 'Xu et al.', 'Diwakaran et al.', 'More et al.']
    capacity = [3.0, 1.8, 2.1, 2.5]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(methods, capacity, color='skyblue')
    
    # Add data labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{height} bpp', ha='center', va='bottom')
    
    plt.title('Steganography Capacity Comparison', fontsize=14)
    plt.ylabel('Capacity (bits per pixel)', fontsize=12)
    plt.ylim(0, 3.5)  # Set y-axis limit
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_quality_comparison():
    """Plot image quality metrics comparison (PSNR and MSE)."""
    methods = ['Our approach', 'Xu et al.', 'Diwakaran et al.', 'More et al.']
    psnr = [51.2, 46.3, 49.7, 50.1]
    mse = [0.493, 1.521, 0.697, 0.631]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # PSNR plot (higher is better)
    bars1 = ax1.bar(methods, psnr, color='green')
    ax1.set_title('PSNR Comparison (higher is better)', fontsize=14)
    ax1.set_ylabel('PSNR (dB)', fontsize=12)
    ax1.grid(axis='y', linestyle='--', alpha=0.7)
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height} dB', ha='center', va='bottom')
    
    # MSE plot (lower is better)
    bars2 = ax2.bar(methods, mse, color='salmon')
    ax2.set_title('MSE Comparison (lower is better)', fontsize=14)
    ax2.set_ylabel('Mean Square Error', fontsize=12)
    ax2.grid(axis='y', linestyle='--', alpha=0.7)
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                f'{height}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()

def plot_speed_comparison():
    """Plot processing time comparison at different image resolutions."""
    resolutions = ['512×512', '1024×1024', '2048×2048', '3840×2160']
    our_system = [87, 254, 863, 1643]
    xu = [112, 318, 1247, 2418]
    diwakaran = [143, 391, 1592, 3254]
    more = [95, 271, 912, 1832]
    
    plt.figure(figsize=(12, 7))
    
    plt.plot(resolutions, our_system, 'o-', label='Our system', linewidth=2, markersize=8)
    plt.plot(resolutions, xu, 's-', label='Xu et al.', linewidth=2, markersize=8)
    plt.plot(resolutions, diwakaran, '^-', label='Diwakaran et al.', linewidth=2, markersize=8)
    plt.plot(resolutions, more, 'D-', label='More et al.', linewidth=2, markersize=8)
    
    plt.title('Processing Time Comparison at Different Resolutions', fontsize=14)
    plt.ylabel('Processing Time (ms)', fontsize=12)
    plt.xlabel('Image Resolution', fontsize=12)
    plt.yscale('log')  # Using log scale for better visualization
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)
    
    # Add data labels
    for i, res in enumerate(resolutions):
        plt.text(i, our_system[i] + 50, f'{our_system[i]} ms', ha='center')
    
    plt.tight_layout()
    plt.show()

def plot_radar_comparison():
    """Plot radar chart comparing different steganography methods."""
    # Categories
    categories = ['Capacity', 'Robustness', 'Imperceptibility', 
                  'Computational\nEfficiency', 'Steganalysis\nResistance', 'Implementation\nEase']
    
    # Values for each method (scale 0-5)
    our_lsb = [5, 1, 5, 5, 1, 5]
    dct = [3, 3, 3, 2, 3, 1]
    dwt = [3, 5, 3, 2, 5, 1]
    adaptive_lsb = [4, 3, 5, 4, 3, 3]
    
    # Number of categories
    N = len(categories)
    
    # Create angles for each category
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]  # Close the loop
    
    # Add the last value to close the loop for each method
    our_lsb += our_lsb[:1]
    dct += dct[:1]
    dwt += dwt[:1]
    adaptive_lsb += adaptive_lsb[:1]
    
    # Create plot
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    
    # Draw one axis per variable and add labels
    plt.xticks(angles[:-1], categories, size=12)
    
    # Plot data
    ax.plot(angles, our_lsb, 'o-', linewidth=2, label='Our LSB')
    ax.fill(angles, our_lsb, alpha=0.1)
    
    ax.plot(angles, dct, 's-', linewidth=2, label='DCT')
    ax.fill(angles, dct, alpha=0.1)
    
    ax.plot(angles, dwt, '^-', linewidth=2, label='DWT')
    ax.fill(angles, dwt, alpha=0.1)
    
    ax.plot(angles, adaptive_lsb, 'D-', linewidth=2, label='Adaptive LSB')
    ax.fill(angles, adaptive_lsb, alpha=0.1)
    
    # Set y-axis limits
    ax.set_ylim(0, 5)
    
    # Add legend
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=12)
    
    plt.title('Steganography Methods Comparison', size=15)
    plt.tight_layout()
    plt.show()

def plot_success_resistance():
    """Plot extraction success rates and detection resistance ratings."""
    methods = ['Our approach', 'Xu et al.', 'Diwakaran et al.', 'More et al.']
    success_rates = [99.97, 99.21, 99.53, 99.87]
    
    # Convert detection resistance ratings to numeric scale (1-5)
    resistance_ratings = [2, 2, 4, 4]  # Medium = 2, High = 4
    
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    # Success rate bars
    bars = ax1.bar(methods, success_rates, color='lightblue', width=0.4)
    ax1.set_ylabel('Extraction Success Rate (%)', fontsize=12)
    ax1.set_ylim(98.5, 100.1)  # Set y-axis limit to zoom in on differences
    
    # Add data labels to bars
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                f'{height}%', ha='center', va='bottom')
    
    # Resistance rating line plot on secondary y-axis
    ax2 = ax1.twinx()
    ax2.plot(methods, resistance_ratings, 'ro-', linewidth=2, markersize=8)
    ax2.set_ylabel('Detection Resistance Rating', fontsize=12, color='r')
    ax2.set_ylim(0, 5)
    ax2.set_yticks([1, 2, 3, 4, 5])
    ax2.set_yticklabels(['Very Low', 'Low', 'Medium', 'High', 'Very High'])
    ax2.tick_params(axis='y', labelcolor='r')
    
    # Add data labels to line points
    for i, rating in enumerate(resistance_ratings):
        label = 'Medium' if rating == 2 else 'High'
        ax2.text(i, rating + 0.2, label, ha='center', va='bottom', color='r')
    
    plt.title('Extraction Success Rates and Detection Resistance', fontsize=14)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print_all_metrics() 