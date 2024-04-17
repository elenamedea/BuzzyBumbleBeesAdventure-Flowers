import pandas as pd
import plotly.graph_objects as go


def generate_landscape_barplot(dataFrame: pd.DataFrame, landscape: str, feature: str, title: str, 
                               xaxis_title: str, yaxis_title: str, title_fontsize: float, tick_fontsize: float, 
                               angle: float, color_dict: dict[str, str], height: float = 900, 
                               width: float = 1600) -> go.Figure:
     
    '''
    Returns a bar chart for one data's feature (column) and for one landscape.

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)
    landscape: Name of the landscape to be explored
    feature: Name of the dataFrame's column to be visualized

    title: Title of the barplot
    xaxis_title: Title of the x-axis
    yaxis_title: Title of the y-axis
    title_fontsize: Font size of the title
    tick_fontsize: Font size of the axes tick values

    angle: The angle of the x-axis tick values
    color_dict: Custom dictionary for the landscape, containing the colors for each value
    
    height: Height of the plot; default is 900
    width: Width of the plot; default is 1600
    ------------------------------------------------------------------------------------------------------------
    '''

    # Filter data for the current landscape
    landscape_data = dataFrame[dataFrame[landscape] == True]

    summary = landscape_data[feature].value_counts()

    # Create a bar chart for feature 
    fig = go.Figure(go.Bar(
                     x = summary.index, y = summary))

    # Update layout
    fig.update_traces(marker_color = color_dict[landscape])

    fig.update_layout(height = height, width = width, 
                      title = dict(text = title, font = dict(size = 22, family = "Times New Roman")),
                             showlegend = False,
                             xaxis = dict(title = xaxis_title, titlefont = dict(size = title_fontsize, family = "Times New Roman"), tickfont = dict(size = tick_fontsize, family = "Times New Roman")),
                             yaxis = dict(title = yaxis_title, titlefont = dict(size = title_fontsize, family = "Times New Roman"), tickfont = dict(size = tick_fontsize, family = "Times New Roman")),
                             barmode = "stack", xaxis_tickangle = angle)

    return fig