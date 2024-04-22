import pandas as pd
import plotly.graph_objects as go


def generate_height_range_barplot(dataFrame: pd.DataFrame, id_column: str, features: list[str], 
                                   color_dict: dict[str, str], title: str, xaxis_title: str,
                                   yaxis_title: str, legend_title: str, height: float = 1000, 
                                   width: float = 3800) -> go.Figure:

    '''
    Returns a bar plot for each species, showing the height range, i.e. height features of each species, after 
    generating a melted data table for these features.

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)
    id_column: Name of the dataFrame's column to be used as the id column of the melted dataFrame

    features: List of the dataFrame Height columns to be visualized
    color_dict: Custom dictionary for the features, containing the colors for each feature

    title: Title of the barplot
    xaxis_title: Title of the x-axis
    yaxis_title: Title of the y-axis
    legend_title: Title of the barplot's legend
    
    height: Height of the plot; default is 1000
    width: Width of the plot; default is 3800
    ------------------------------------------------------------------------------------------------------------
    '''

    # Melt the DataFrame to long format for plotting
    melted_data = pd.melt(dataFrame, id_vars = [id_column], value_vars = features,
                          var_name = "HeightType", value_name = "Height")

    # Combine "Höhe min(cm)" and "Höhe max(cm)" into a new column
    melted_data["Combined_Height"] = melted_data.groupby(id_column)["Height"].transform("sum")

    # Sort the DataFrame by "HeightType" and "Combined_Height" in ascending order
    melted_data = melted_data.sort_values(["HeightType", "Combined_Height"])

    # Create traces for the barplot
    traces = []
    for height_type, color in color_dict.items():
        height_data = melted_data[melted_data["HeightType"] == height_type]
        trace = go.Bar(
            x = height_data[id_column], y = height_data["Height"],
                       name = height_type, marker_color = color)
        traces.append(trace)

    # Create barplot's layout
    layout = go.Layout(
        height = height,
        width = width,
        title = dict(text = title, font = dict(size = 28, family = "Times New Roman")),
        xaxis = dict(title = xaxis_title, titlefont = dict(size = 20, family = "Times New Roman"), tickfont = dict(size = 16, family = "Times New Roman")),
        yaxis = dict(title = yaxis_title, titlefont = dict(size = 20, family = "Times New Roman"), tickfont = dict(size = 18, family = "Times New Roman")),
        legend = dict(
            title = dict(text = legend_title, font = dict(family = "Times New Roman", size = 20)),
            traceorder = "normal",
            font = dict(family = "Times New Roman", size = 17)
        ),
        xaxis_tickangle = -45)

    # Create figure
    fig = go.Figure(data = traces, layout = layout)

    return fig