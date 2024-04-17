import pandas as pd
import plotly.graph_objects as go


def generate_pie_chart_for_subplotting(dataFrame: pd.DataFrame, feature: str, color_column: str, title: str, 
                                       color_dict: dict[bool, str], fontsize: float = 18) -> go.Pie:

    '''
    Returns a pie chart for one data's feature (column), which can be used for subplotting.

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)
    feature: Name of the dataFrame's column to be visualized
    color_column: Name of the column, which values will be used for the color mapping

    title: Title of the pie chart
    color_dict: Custom dictionary for the feature, containing the colors for each value

    fontsize: Font size of the plot's text; default is 18
    ------------------------------------------------------------------------------------------------------------
    '''
     
    # Group data by feature and count occurrences
    data_grouped = dataFrame.groupby(feature).size().reset_index(name = "Count")

    # Create Pie trace
    pie_trace = go.Pie(
        labels = data_grouped[feature],
        values = data_grouped["Count"],
        hoverinfo = "percent+label",
        textinfo = "percent+label",
        marker = dict(colors = data_grouped[color_column].map(color_dict)),
        title = dict(text = title, position = "bottom center", font = dict(family = "Times New Roman", size = fontsize)), hole = 0.6,
        insidetextfont = {"size" : fontsize, "family" : "Times"},
        textfont = {"size" : fontsize, "family" : "Times"})

    return pie_trace