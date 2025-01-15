import pandas as pd
import numpy as np
from lets_plot import *
from palmerpenguins import load_penguins

# Load the Palmer Penguins dataset
penguins = load_penguins()

# Display the first few rows of the dataset for inspection
print(penguins['species'])  # Corrected line

# Setup LetsPlot for HTML rendering
LetsPlot.setup_html(isolated_frame=True)