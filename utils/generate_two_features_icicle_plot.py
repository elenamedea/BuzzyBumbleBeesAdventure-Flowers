import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def generate_two_features_icicle_plot(dataFrame: pd.DataFrame, landscape: str, life_column: str, second_column: str, 
                                title: str, color_dict: dict[str, str], height: float = 1600, 
                                width: float = 1600) -> go.Figure:

    '''
    Returns an icicle plot regarding the growth cycle and a binary feature (e.g. edibility, toxicity) of the 
    plants, under one landscape.
    
    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)
    landscape: Name of the landscape to be explored

    life_column:  Name of the dataFrame's column referring to the growth cycle of the plants
    second_column: Name of the second dataFrame's column to be explored

    title: Title of the icicle plot
    color_dict: Custom dictionary for the feature, containing the colors for each landscape
      
    height: Height of the plot; default is 1600
    width: Width of the plot; default is 1600
    ------------------------------------------------------------------------------------------------------------
    '''

    # Filter data for the current landscape
    landscape_data = dataFrame[dataFrame[landscape] == True]

    # Create Icicle plot
    fig = px.icicle(
        landscape_data, path = [life_column, second_column], color = life_column, 
                           color_discrete_map = color_dict, title = f"{title}: {landscape}")

    # Update layout
    fig.update_layout(height = height, 
                      width = width, 
                      title = dict(text = title, font = dict(family = "Times New Roman", size = 26)), 
                      font = dict(size = 20, family = "Times New Roman"))

    return fig