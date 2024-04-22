import pandas as pd
import plotly.graph_objects as go


def generate_treemap(dataFrame: pd.DataFrame, feature: str, color_dict: dict[str, str], title: str, 
                     fontsize: float = 24, height: float = 900, width: float = 2600) -> go.Figure:

    '''
    Returns a treemap for one data's feature (column).

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)
    feature: Name of the dataFrame's column to be visualized

    color_dict: Custom dictionary for the feature, containing the colors for each value
    title: Title of the pie chart
    
    fontsize: Font size of the plot's text; default is 24
    height: Height of the plot; default is 900
    width: Width of the plot; default is 2600
    ------------------------------------------------------------------------------------------------------------
    '''

    # Group by the feature and count the occurrences
    grouped_data = dataFrame.groupby([feature]).size().reset_index(name = "Count")

    # Create a treemap chart for the current feature
    fig = go.Figure(go.Treemap(
        labels = grouped_data[feature],
        parents = [""] * len(grouped_data),  # Setting parents to an empty string for a single-level treemap
        values = grouped_data["Count"],
        marker = dict(
            colors = grouped_data[feature].map(color_dict),
            line = dict(color = "#ffffff", width = 0.5)), # Adjust line color and width
            textinfo = "label+percent entry",
            textfont = dict(size = fontsize, family = "Times New Roman")))

    # Update treamap's layout
    fig.update_layout(
        height = height,
        width = width,
        title = dict(text = title, font = dict(family = "Times New Roman", size = fontsize)))

    return fig