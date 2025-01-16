import csv
from datetime import datetime
import pandas as pd
import numpy as np
import pygal
#import matplotlib.pyplot as plt
from flask import Flask, render_template

import plotly.express as px

# Input and output file names
input_file = 'cleaned2.csv'
output_file = 'BR2-Out.csv'
data = pd.read_csv(input_file,na_values=['no data'],encoding='utf-8')
data.to_csv(input_file, index=False)


#numeric_cols = ['wkno','value1','value2']
non_numeric_cols = ['wkno','date','bool']
stat_dict = {}

for col in data.columns:
    if col not in non_numeric_cols:
        stats_data = data[col]
        stat_dict[col] = {
            'Mean': stats_data.mean(),
            'median': stats_data.median(),
            #'Mode': stats_data.mode().iloc(0) if not stats_data.mode().empty else np.nan,
            'Range': stats_data.max() - stats_data.min()
            }
#print(stat_dict)

stats_df = pd.DataFrame(stat_dict).transpose()
print(stats_df)

bar_chart = px.bar(
    data,
    x=data.columns[1],
    y=data.columns[2],
    title="Bar Chart: Col 1 vs Col2",
    labels={data.columns[1]: "year", data.columns[2]: "Values"}
)
bar_chart_html = bar_chart.to_html(full_html=False, include_plotlyjs="cdn")

data_long = data.melt(
    id_vars=[data.columns[1]],
    value_vars=[data.columns[2], data.columns[3], data.columns[4]],
    var_name="Variable",
    value_name="Value"
)
           
line_chart = px.line(
    data_long,
    x=data.columns[1],
    y="Value",
    color="Variable",
    title="Line Chart: Column 1 Vs Column 2",
    labels={data.columns[1]: "Year", "Value": "Values", "Variable": "Categories"}
)
line_chart_html = line_chart.to_html(full_html=False, include_plotlyjs="cdn")

scatter_plot = px.scatter(
    data,
    x=data.columns[2],
    y=data.columns[3],
    title="Scatter Plot: Column 1 Vs Column 2",
    labels={data.columns[3]: "Values"}
)
scatter_plot_html = scatter_plot.to_html(full_html=False, include_plotlyjs="cdn")


#bar_chart.show()
#line_chart.show()
#scatter_plot.show()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        bar_chart=bar_chart_html,
        line_chart=line_chart_html,
        scatter_chart=scatter_plot_html
    )

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5001,debug=False)

