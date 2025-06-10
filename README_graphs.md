# Graph Generation for Steganography Paper

This folder contains Python scripts to generate visual graphs for the steganography performance analysis in the paper.

## Requirements

The graph generation requires:
- Python 3.6 or higher
- matplotlib
- numpy

You can install the required packages using:

```bash
pip install matplotlib numpy
```

## Generating the Graphs

1. Run the automation script:

```bash
python run_graphs.py
```

This will:
- Execute the graph generation script
- Create all required graphs in both PNG and PDF formats
- Copy the files to the appropriate directories for LaTeX

Alternatively, you can run the generation script directly:

```bash
python generate_graphs.py
```

## Generated Graphs

The script creates the following visualizations:

1. **Capacity Comparison** (`capacity_comparison.png/pdf`)
   - Bar chart comparing steganography capacity (bits per pixel) across different implementations

2. **Quality Comparison** (`quality_comparison.png/pdf`)
   - Side-by-side bar charts of PSNR and MSE metrics across implementations

3. **Speed Comparison** (`speed_comparison.png/pdf`)
   - Bar chart comparing processing times across different image resolutions

4. **Radar Comparison** (`radar_comparison.png/pdf`)
   - Radar/spider chart comparing steganography methods across 6 dimensions

5. **Success & Resistance** (`success_resistance.png/pdf`)
   - Dual-axis chart showing extraction success rates and detection resistance

## LaTeX Integration

The graphs are referenced in the LaTeX document using:

```latex
\begin{figure}[h]
    \centering
    \includegraphics[width=0.8\textwidth]{static/graphs/filename.png}
    \caption{Caption text here.}
    \label{fig:label}
\end{figure}
```

If you regenerate the graphs, run LaTeX compilation again to see the updated images.

## Customization

To modify the graph data or appearance:

1. Edit the values in the appropriate function in `generate_graphs.py`
2. Run the script again to regenerate the graphs
3. Recompile the LaTeX document to see the changes

## Troubleshooting

- If LaTeX can't find the images, check the paths in the `\includegraphics` commands
- Make sure the `static` directory is in the same folder as your LaTeX document
- If you get `FileNotFoundError`, ensure you have write permissions to the output directories 