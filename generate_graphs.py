import matplotlib.pyplot as plt
import numpy as np
import os

# Create output directory if it doesn't exist
os.makedirs('static/graphs', exist_ok=True)

# Set style for better looking graphs
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

def save_fig(fig, filename):
    """Save figure with tight layout and in multiple formats."""
    fig.tight_layout()
    fig.savefig(f'static/graphs/{filename}.png', dpi=300, bbox_inches='tight')
    fig.savefig(f'static/graphs/{filename}.pdf', bbox_inches='tight')
    print(f"Saved {filename}")

# 1. Steganography Capacity Comparison
def generate_capacity_comparison():
    systems = ['Our System', 'Xu et al.', 'Diwakaran et al.', 'More et al.']
    capacities = [3.0, 1.8, 2.1, 2.5]
    
    fig, ax = plt.subplots()
    bars = ax.bar(systems, capacities, color=['#ff6b2b', '#5DA5DA', '#60BD68', '#F5C855'])
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{height:.1f}', ha='center', va='bottom')
    
    ax.set_ylim(0, max(capacities) + 0.5)
    ax.set_ylabel('Capacity (bits per pixel)')
    ax.set_title('Steganography Capacity Comparison')
    
    save_fig(fig, 'capacity_comparison')

# 2. Image Quality Comparison (PSNR)
def generate_quality_comparison():
    systems = ['Our System', 'Xu et al.', 'Diwakaran et al.', 'More et al.']
    psnr = [51.2, 46.3, 49.7, 50.1]
    mse = [0.493, 1.521, 0.697, 0.631]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # PSNR Plot
    bars1 = ax1.bar(systems, psnr, color=['#ff6b2b', '#5DA5DA', '#60BD68', '#F5C855'])
    ax1.set_ylabel('PSNR (dB)')
    ax1.set_title('Peak Signal-to-Noise Ratio Comparison')
    
    # Add value labels on top of bars
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height:.1f}', ha='center', va='bottom')
    
    # MSE Plot
    bars2 = ax2.bar(systems, mse, color=['#ff6b2b', '#5DA5DA', '#60BD68', '#F5C855'])
    ax2.set_ylabel('MSE')
    ax2.set_title('Mean Square Error Comparison')
    
    # Add value labels on top of bars
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                f'{height:.3f}', ha='center', va='bottom')
    
    fig.suptitle('Image Quality Metrics Comparison', fontsize=16)
    fig.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust for suptitle
    
    save_fig(fig, 'quality_comparison')

# 3. Processing Time Comparison
def generate_speed_comparison():
    image_sizes = ['512×512', '1024×1024', '2048×2048', '3840×2160']
    our_system = [87, 254, 863, 1643]
    xu = [112, 318, 1247, 2418]
    diwakaran = [143, 391, 1592, 3254]
    more = [95, 271, 912, 1832]
    
    x = np.arange(len(image_sizes))
    width = 0.2
    
    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(x - width*1.5, our_system, width, label='Our System', color='#ff6b2b')
    rects2 = ax.bar(x - width/2, xu, width, label='Xu et al.', color='#5DA5DA')
    rects3 = ax.bar(x + width/2, diwakaran, width, label='Diwakaran et al.', color='#60BD68')
    rects4 = ax.bar(x + width*1.5, more, width, label='More et al.', color='#F5C855')
    
    ax.set_ylabel('Processing Time (ms)')
    ax.set_xlabel('Image Resolution')
    ax.set_xticks(x)
    ax.set_xticklabels(image_sizes)
    ax.legend()
    ax.set_title('Steganography Processing Time by Image Size')
    
    # Convert to logarithmic scale for better visualization
    ax.set_yscale('log')
    ax.set_ylim(50, 4000)
    
    save_fig(fig, 'speed_comparison')

# 4. Radar chart for method comparison
def generate_radar_chart():
    # Categories for radar chart
    categories = ['Capacity', 'Robustness', 'Imperceptibility', 
                  'Speed', 'Security', 'Implementation\nEase']
    
    # Values for each method (on a scale of 0-5)
    our_lsb = [5, 2, 5, 5, 4, 5]
    dct = [3, 3, 3, 3, 3, 2]
    dwt = [3, 5, 3, 2, 4, 2]
    adaptive_lsb = [4, 3, 4, 4, 3, 3]
    
    # Number of categories
    N = len(categories)
    
    # Create angles for each category
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]  # Close the loop
    
    # Add values for each method
    our_lsb += our_lsb[:1]
    dct += dct[:1]
    dwt += dwt[:1]
    adaptive_lsb += adaptive_lsb[:1]
    
    # Create figure
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    # Plot each method
    ax.plot(angles, our_lsb, 'o-', linewidth=2, label='Our LSB', color='#ff6b2b')
    ax.plot(angles, dct, 'o-', linewidth=2, label='DCT', color='#5DA5DA')
    ax.plot(angles, dwt, 'o-', linewidth=2, label='DWT', color='#60BD68')
    ax.plot(angles, adaptive_lsb, 'o-', linewidth=2, label='Adaptive LSB', color='#F5C855')
    
    # Fill areas
    ax.fill(angles, our_lsb, alpha=0.1, color='#ff6b2b')
    ax.fill(angles, dct, alpha=0.1, color='#5DA5DA')
    ax.fill(angles, dwt, alpha=0.1, color='#60BD68')
    ax.fill(angles, adaptive_lsb, alpha=0.1, color='#F5C855')
    
    # Set category labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    
    # Set y-axis limits
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['1', '2', '3', '4', '5'])
    
    # Add legend
    ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    
    # Add title
    plt.title('Steganography Methods Comparison', size=15, y=1.1)
    
    save_fig(fig, 'radar_comparison')

# 5. Success Rate and Detection Resistance
def generate_success_resistance_chart():
    systems = ['Our System', 'Xu et al.', 'Diwakaran et al.', 'More et al.']
    success_rates = [99.97, 99.21, 99.53, 99.87]
    
    # Detection resistance ratings (1-5 scale)
    resistance_ratings = [3, 3, 4, 4]  # Converted from Medium/High text ratings
    
    fig, ax1 = plt.subplots()
    
    # Plot success rates as bars
    bars = ax1.bar(systems, success_rates, color=['#ff6b2b', '#5DA5DA', '#60BD68', '#F5C855'], alpha=0.7)
    ax1.set_ylim(99, 100.1)  # Zoom in on the high percentages
    ax1.set_ylabel('Extraction Success Rate (%)')
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.02,
                f'{height:.2f}%', ha='center', va='bottom')
    
    # Create a second y-axis for resistance ratings
    ax2 = ax1.twinx()
    ax2.plot(systems, resistance_ratings, 'o-', color='#d62728', linewidth=2, label='Detection Resistance')
    ax2.set_ylim(0, 5)
    ax2.set_ylabel('Detection Resistance Rating (1-5)')
    
    # Add a legend for the line
    lines, labels = ax2.get_legend_handles_labels()
    ax1.legend(lines, labels, loc='lower right')
    
    plt.title('Extraction Success Rate vs. Detection Resistance')
    
    save_fig(fig, 'success_resistance')

if __name__ == "__main__":
    generate_capacity_comparison()
    generate_quality_comparison()
    generate_speed_comparison()
    generate_radar_chart()
    generate_success_resistance_chart()
    
    print("All graphs generated successfully!") 