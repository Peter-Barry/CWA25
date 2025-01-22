import csv
from datetime import datetime
import pandas as pd
import numpy as np
from flask import Flask, render_template
import plotly.express as px

# Input file name
input_file = 'cleaned2.csv'

# Read CSV file, handling missing values
data = pd.read_csv(input_file, na_values=['no data'], encoding='utf-8')
data.to_csv(input_file, index=False)

# Define non-numeric columns
non_numeric_cols = ['wkno', 'date', 'bool']
stat_dict = {}

# Calculate statistics for numeric columns
for col in data.columns:
    if col not in non_numeric_cols:
        stats_data = data[col]
        stat_dict[col] = {
            'Mean': stats_data.mean(),
            'Median': stats_data.median(),
            'Range': stats_data.max() - stats_data.min()
        }

stats_df = pd.DataFrame(stat_dict).transpose()
print(stats_df)

# Generate Bar Chart
bar_chart = px.bar(
    data,
    x=data.columns[1],
    y=data.columns[2],
    title="Bar Chart: Col 1 vs Col 2",
    labels={data.columns[1]: "Year", data.columns[2]: "Values"}
)
bar_chart_html = bar_chart.to_html(full_html=False, include_plotlyjs="cdn")

# Transform data for Line Chart
data_long = data.melt(
    id_vars=[data.columns[1]],
    value_vars=[data.columns[2], data.columns[3], data.columns[4]],
    var_name="Variable",
    value_name="Value"
)

# Generate Line Chart
line_chart = px.line(
    data_long,
    x=data.columns[1],
    y="Value",
    color="Variable",
    title="Line Chart: Column 1 Vs Column 2",
    labels={data.columns[1]: "Year", "Value": "Values", "Variable": "Categories"}
)
line_chart_html = line_chart.to_html(full_html=False, include_plotlyjs="cdn")

# Generate Scatter Plot
scatter_plot = px.scatter(
    data,
    x=data.columns[2],
    y=data.columns[3],
    title="Scatter Plot: Column 1 Vs Column 2",
    labels={data.columns[3]: "Values"}
)
scatter_plot_html = scatter_plot.to_html(full_html=False, include_plotlyjs="cdn")

# Create Flask web application
app = Flask(__name__)

# Home page with links to individual charts
@app.route('/')
def index():
    return render_template("index_AR1.html")

# Page for Bar Chart
@app.route('/bar_chart')
def bar_chart_page():
    return render_template("chart.html", chart_title="Bar Chart", chart=bar_chart_html)

# Page for Line Chart
@app.route('/line_chart')
def line_chart_page():
    return render_template("chart.html", chart_title="Line Chart", chart=line_chart_html)

# Page for Scatter Plot
@app.route('/scatter_chart')
def scatter_chart_page():
    return render_template("chart.html", chart_title="Scatter Plot", chart=scatter_plot_html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
