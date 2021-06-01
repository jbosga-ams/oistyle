import json
from pathlib import Path
import sys
import seaborn as sns

sns.axes_style()

# read file
with open(Path(sys.prefix, 'etc/oistyle/base_style.json'), 'r') as f:
    data=f.read()
base_style = json.loads(data)
colors = base_style["colors"]

base_template = {'axes.facecolor': 'white', 'axes.edgecolor': base_style['gridline_color'], 'axes.grid': False, 'axes.axisbelow': 'line', 
'axes.labelcolor': 'black', 'figure.facecolor': 'white', 'grid.color': '#b0b0b0', 'grid.linestyle': '-', 'text.color': 'black', 
'xtick.color': 'black', 'ytick.color': 'black', 'xtick.direction': 'out', 'ytick.direction': 'out',  'patch.edgecolor': 'black', 
'patch.force_edgecolor': False, 'image.cmap': 'viridis', 'font.family': [base_style['font']], 'xtick.bottom': True, 'xtick.top': False, 'ytick.left': True, 'ytick.right': False, 
'axes.spines.left': True, 'axes.spines.bottom': True, 'axes.spines.right': True, 'axes.spines.top': True}