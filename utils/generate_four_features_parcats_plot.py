import pandas as pd
import plotly.graph_objects as go


def generate_four_features_parcats_plot(dataFrame: pd.DataFrame, landscape: str, life_column: str, 
                                                  life_label: str, edible_column: str, poisonous_column: str, 
                                                  title: str, color_dict: dict[str, str], height: float = 900, 
                                                  width: float = 1600) -> go.Figure:

    '''
    Returns a parallel categories plot of plants present in a landscape, regarding their growth cycle, 
    edibility, and toxicity.  

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)
    landscape: Name of the landscape to be explored

    life_column:  Name of the dataFrame's column referring to the life cycle of the plants
    life_label: Label for the life cycle dimension
    edible_column: Name of the dataFrame's column referring to the edibility of the plants
    poisonous_column: Name of the dataFrame's column referring to the toxicity of the plants

    title: Title of the parallel categories plot
    color_dict: Custom dictionary for the feature, containing the colors for each landscape
      
    height: Height of the plot; default is 900
    width: Width of the plot; default is 1600
    ------------------------------------------------------------------------------------------------------------
    '''

    # Filter data for the current landscape
    landscape_data = dataFrame[dataFrame[landscape] == True]

    # Create dimensions
    landscape_dim = go.parcats.Dimension(
        values = landscape_data[landscape], label = landscape)
    
    life_cycle_dim = go.parcats.Dimension(
        values = landscape_data[life_column], label = life_label)
    
    edible_dim = go.parcats.Dimension(
        values = landscape_data[edible_column], label = edible_column)
    
    poisonous_dim = go.parcats.Dimension(
        values = landscape_data[poisonous_column], label = poisonous_column)

    # Get the color for the current landscape
    landscape_color = color_dict.get(landscape, "gray")

    # Create Parcats trace with color
    parcats_trace = go.Parcats(
        dimensions = [landscape_dim, life_cycle_dim, edible_dim, poisonous_dim],
        line = {"color" : landscape_color},  # Set color for the landscape
        hoveron = "category", hoverinfo="count+probability",
        labelfont = {"size" : 18, "family": "Times"},
        tickfont = {"size" : 16, "family": "Times"},
        arrangement = "freeform")

    # Create layout
    layout = go.Layout(height = height, 
                       width = width, 
                       title = dict(text = title, font = dict(family = "Times New Roman", size = 24)), font = dict(size = 18, family = "Times New Roman"),
                       margin = dict(l = 50, r = 50, b = 50, t = 50))

    # Create figure
    fig = go.Figure(data = [parcats_trace], layout = layout)

    return fig