import csv
from datetime import datetime
import pandas as pd
import numpy as np
# import pygal
import matplotlib.pyplot as plt

import plotly.express as px

# Input and output file names
input_file = 'cleaned.csv'
output_file = 'BR2-Out.csv'
data = pd.read_csv(input_file,na_values=['no data'],encoding='utf-8')
data.to_csv(input_file, index=False)


numeric_cols = ['wkno','value1','value2']
non_numeric_cols = ['date','bool']
stat_dict = {}