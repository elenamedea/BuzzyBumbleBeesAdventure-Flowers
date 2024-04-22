import pandas as pd
import plotly.graph_objects as go
from typing import Any


def generate_pie_chart(dataFrame: pd.DataFrame, feature: str, color_column: str, title: str, 
                       color_dict: dict[Any, str], legend_title: str, title_fontsize: float = 24, 
                       height: float = 1400, width: float = 2600) -> go.Figure:
    
    '''
    Returns a pie chart for one data's feature (column).

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)
    feature: Name of the dataFrame's column to be visualized
    color_column: Name of the column, which values will be used for the color mapping

    title: Title of the pie chart
    color_dict: Custom dictionary for the feature, containing the colors for each value
    legend_title: Title of the pie chart's legend
    
    title_fontsize: Font size of the title; default is 24
    height: Height of the plot; default is 1400
    width: Width of the plot; default is 2600
    ------------------------------------------------------------------------------------------------------------
    '''

    fig = go.Figure()

    # Group data by selected feature and count occurrences
    data_grouped = dataFrame.groupby(feature).size().reset_index(name = "Count")

    # Add Pie trace
    fig.add_trace(go.Pie(labels = data_grouped[feature], values = data_grouped["Count"], 
                         hoverinfo = "percent+label", textinfo = "percent+label",
                         marker = dict(colors = data_grouped[color_column].map(color_dict)),
                         title = dict(text = title, font = dict(family = "Times New Roman", size = title_fontsize)), hole = 0.6,
                         insidetextfont = {"size" : 18, "family" : "Times"},
                         textfont = {"size" : 18, "family" : "Times"}))

    # Choose pie's layout
    fig.update_layout(
        height = height,
        width = width,
        legend = dict(title = dict(text = legend_title, font = dict(family = "Times New Roman", size = 20)), font = dict(family = "Times New Roman", size = 16)))

    return fig