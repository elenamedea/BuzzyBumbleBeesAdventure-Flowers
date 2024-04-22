import pandas as pd
import plotly.graph_objects as go


def generate_two_features_parcats_plot(dataFrame: pd.DataFrame, n_landscapes_column: str, n_landscapes_label: str, 
                          family_column: str, family_label: str, title: str, color_dict: dict[str, str], 
                          height: float = 1600, width: float = 2800) -> go.Figure:
    
    '''
    Returns a parallel categories plot of plants under one landscape, regarding their growth cycle and two 
    binary features (e.g. edibility, toxicity).

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)

    n_landscapes_column: Name of the dataFrame's column referring to the number of landscapes, where the 
    plants are present
    n_landscapes_label: Label for the number of landscapes dimension

    family_column: Name of the dataFrame's column referring to the plant families
    family_label: Label for the plant families dimension

    title: Title of the parallel categories plot
    color_dict: Custom dictionary for the feature, containing the colors for each landscape
      
    height: Height of the plot; default is 1600
    width: Width of the plot; default is 2800
    ------------------------------------------------------------------------------------------------------------
    '''
    
    # Create dimensions
    n_present_landscapes_dim = go.parcats.Dimension(
        values = dataFrame[n_landscapes_column],
        categoryorder = "category ascending", label = n_landscapes_label)

    family_dim = go.parcats.Dimension(
        values = dataFrame[family_column], label = family_label)

    # Create Parcats trace with assigned colors
    parcats_trace = go.Parcats(
        dimensions = [n_present_landscapes_dim, family_dim],
        line = {"color" : dataFrame[family_column].map(color_dict)},
        hoveron = "category", hoverinfo = "count+probability",
        labelfont = {"size" : 20, "family" : "Times"},
        tickfont = {"size" : 18, "family" : "Times"},
        arrangement = "freeform")

    # Create layout
    layout = go.Layout(
        height = height, 
        width = width, 
        title = dict(text = title, font = dict(family = "Times New Roman", size = 28)),  
        margin = dict(l = 100, r = 150, b = 100, t = 100))

    # Create figure
    fig = go.Figure(data = [parcats_trace], layout = layout)

    return fig