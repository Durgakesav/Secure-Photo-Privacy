#!/usr/bin/env python3

import os
import subprocess
import shutil

def run_graph_generation():
    """Run the graph generation script and verify outputs."""
    print("Starting graph generation...")
    
    # Create the output directories if they don't exist
    os.makedirs('static/graphs', exist_ok=True)
    
    # Run the graph generation script
    subprocess.run(['python', 'generate_graphs.py'], check=True)
    
    # Verify that graphs were created
    expected_files = [
        'capacity_comparison.png',
        'capacity_comparison.pdf',
        'quality_comparison.png',
        'quality_comparison.pdf',
        'speed_comparison.png',
        'speed_comparison.pdf',
        'radar_comparison.png',
        'radar_comparison.pdf',
        'success_resistance.png',
        'success_resistance.pdf'
    ]
    
    missing_files = []
    for filename in expected_files:
        if not os.path.exists(f'static/graphs/{filename}'):
            missing_files.append(filename)
    
    if missing_files:
        print(f"Warning: The following files were not generated: {', '.join(missing_files)}")
    else:
        print("All graph files were generated successfully!")
    
    # Copy files to LaTeX directory if needed
    # This assumes the LaTeX file is in the same directory
    # If LaTeX is looking for images in a specific directory, copy them there
    latex_img_dir = 'static'
    if not os.path.exists(latex_img_dir):
        os.makedirs(latex_img_dir, exist_ok=True)
    
    # Copy graph files to LaTeX image directory
    for filename in expected_files:
        if os.path.exists(f'static/graphs/{filename}'):
            # Only copy if the source file exists
            shutil.copy2(f'static/graphs/{filename}', f'{latex_img_dir}/{filename}')
    
    print(f"Copied graph files to {latex_img_dir} for LaTeX access")
    print("Done!")

if __name__ == "__main__":
    run_graph_generation() 