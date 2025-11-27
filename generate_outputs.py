import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Set random seed for reproducibility
np.random.seed(42)

# Load data from CSV
try:
    df = pd.read_csv('data.csv')
    print("Data loaded from data.csv")
except FileNotFoundError:
    print("Error: data.csv not found")
    exit()

# Calculate Correlation Matrix
corr_matrix = df.corr()

# Save Correlation Matrix to CSV
corr_matrix.to_csv('correlation.csv')
print("correlation.csv generated.")

# Create Custom Red-White-Green Colormap (mimicking Excel)
# Red (low) -> White (middle) -> Green (high)
colors = ["#FF0000", "#FFFFFF", "#00FF00"]
cmap = LinearSegmentedColormap.from_list("excel_rwg", colors)

# Create Heatmap
plt.figure(figsize=(8, 8))
sns.set(font_scale=1.0)
ax = sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap=cmap,
    vmin=-1,
    vmax=1,
    center=0,
    square=True,
    linewidths=0.5,
    linecolor='lightgray',
    cbar=False  # Excel conditional formatting usually doesn't show a colorbar in the cells
)

plt.title('Supply Chain Correlation Matrix', fontsize=14)
plt.tight_layout()

# Save Heatmap with specific dimensions (512x512)
plt.savefig('heatmap.png', dpi=64) # 8x64 = 512
print("heatmap.png generated.")
