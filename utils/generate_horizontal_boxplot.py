import pandas as pd
import plotly.graph_objects as go


def generate_horizontal_boxplot(dataFrame: pd.DataFrame, id_column: str, features: list[str], 
                               color_dict: dict[str, str], title: str, yaxis_title: str, xaxis_title: str, 
                               height: float = 900, width: float = 2600) -> go.Figure:

    '''
    Returns a boxplot for Height data features (columns), after generating a melted data table for 
    these features.

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)
    id_column: Name of the dataFrame's column to be used as the id column of the melted dataFrame
    features: List of the dataFrame Height columns to be visualized

    color_dict: Custom dictionary for the features, containing the colors for each feature
    title: Title of the boxplot
    yaxis_title: Title of the y-axis
    xaxis_title: Title of the x-axis
    
    height: Height of the plot; default is 900
    width: Width of the plot; default is 2600
    ------------------------------------------------------------------------------------------------------------
    '''

    # Melt the DataFrame to long format for plotting
    melted_data = pd.melt(dataFrame, id_vars = [id_column], value_vars = features,
                          var_name = "Height(cm)", value_name = "Height")

    # Sort the DataFrame by "HeightType" and "Height" in ascending order
    melted_data = melted_data.sort_values([id_column, "Height"])

    # Create traces for the horizontal box plot
    traces = []
    for height_type, color in color_dict.items():
        height_data = melted_data[melted_data["Height(cm)"] == height_type]
        trace = go.Box(
            y = height_data["Height(cm)"], x = height_data["Height"], name = height_type, 
            boxpoints = "all", marker_color = color, orientation = "h")
        traces.append(trace)

    # Create boxplot's layout
    layout = go.Layout(
        height = height,
        width = width,
        title = dict(text = title, font = dict(size = 28, family = "Times New Roman")),
        yaxis = dict(title = yaxis_title, titlefont = dict(size = 20, family = "Times New Roman"), tickfont = dict(size = 18, family = "Times New Roman")),
        xaxis = dict(title = xaxis_title, titlefont = dict(size = 20, family = "Times New Roman"), tickfont = dict(size = 18, family = "Times New Roman")),
        legend = dict(
            title = dict(text = xaxis_title, font = dict(family = "Times New Roman", size = 20)),
            traceorder = "normal",
            font = dict(family = "Times New Roman", size = 17)))

    # Create figure
    fig = go.Figure(data = traces, layout = layout)

    return fig