import pandas as pd
import plotly.graph_objects as go


def generate_scatterplot(dataFrame: pd.DataFrame, x_value: str, y_value: str, id_column: str, title: str, 
                        height: float = 1200, width: float = 1600) -> go.Figure:

    '''
    Returns a scatterplot, where points refer to each species, showing the height features of each species.

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)

    x_value: Name of the dataFrame's column to be used as the X values
    y_value: Name of the dataFrame's column to be used as the Y values
    id_column: Name of the dataFrame's column to be used as the id column (plant species) of the plot

    title: Title of the scatterplot
    
    height: Height of the plot; default is 1200
    width: Width of the plot; default is 1600
    ------------------------------------------------------------------------------------------------------------
    '''

    # Extract relevant columns for x and y axes
    x_values = dataFrame[x_value]
    y_values = dataFrame[y_value]
    plant_species = dataFrame[id_column]

    # Create a scatterplot
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x = x_values,
            y = y_values,
            mode = "markers",
            text = plant_species,
            marker = dict(color = "#AA9486", size = 8, opacity = 0.6),  # Customize marker color and size
            hoverinfo = "text+x+y")) # Display plant species on hover

    # Create scatterplot's layout
    fig.update_layout(
        height = height,
        width = width,
        title = dict(text = title, font = dict(size = 28, family = "Times New Roman")),
        yaxis = dict(title = y_value, titlefont = dict(size = 20, family = "Times New Roman"), tickfont = dict(size = 18, family = "Times New Roman")),
        xaxis = dict(title = x_value, titlefont = dict(size = 20, family = "Times New Roman"), tickfont = dict(size = 18, family = "Times New Roman")))

    return fig
