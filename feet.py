import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set a seed for reproducibility
np.random.seed(42)

# Generate mock data
# Number of samples
N = 100

# Height (in inches) - normally distributed around 64 inches (5'4")
height_mean = 64
height_std = 3
height = np.random.normal(height_mean, height_std, N)

# Shoe size (US Women's) - positively correlated with height
# Base shoe size (linear relationship: 0.2 * height) + some noise
shoe_size_base = 0.2 * height + (np.random.rand(N) * 2 - 1)
# Normalize and round to typical shoe sizes (e.g., 5 to 12)
shoe_size = np.clip(np.round(shoe_size_base - np.mean(shoe_size_base) + 7.5), 5, 12)

# Create DataFrame
df = pd.DataFrame({
    'Height (in)': height,
    'Shoe Size (US Women\'s)': shoe_size
})

# Generate the chart
plt.figure(figsize=(10, 6))
plt.scatter(df['Height (in)'], df['Shoe Size (US Women\'s)'], alpha=0.7)

# Add titles and labels
plt.title('Relationship Between Female Height and Shoe Size (Mock Data)')
plt.xlabel('Height (in)')
plt.ylabel('Shoe Size (US Women\'s)')

# Set y-axis to integers for clearer shoe sizes
plt.yticks(np.arange(min(shoe_size), max(shoe_size)+1))
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Save the plot
chart_filename = 'height_vs_shoe_size_scatter_plot.png'
plt.savefig(chart_filename)
# The output will print the head of the generated DataFrame and the filename
# of the saved chart.