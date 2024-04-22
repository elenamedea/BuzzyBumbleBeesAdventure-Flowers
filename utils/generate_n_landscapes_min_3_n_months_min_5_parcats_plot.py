import pandas as pd
import plotly.graph_objects as go


def generate_n_landscapes_min_3_n_months_min_5_parcats_plot(dataFrame: pd.DataFrame, n_landscapes_column: str, 
            n_landscapes_label: str, n_months_column: str, n_months_label: str, id_column: str, 
            id_label: str, family_column: str, family_label: str, title: str, color_dict: dict[int, str], 
            height: float = 900, width: float = 2400) -> go.Figure:
    
    '''
    Returns a parallel categories plot of plant species, which are present in more than 3 landscapes and 
    blossoming for more than 5 months. In the plot the plant families are also visible as a separate
    dimension.

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)
    
    n_landscapes_column: Name of the dataFrame's column referring to the number of landscapes, where the 
    plants are present
    n_landscapes_label: Label for the number of landscapes dimension

    n_months_column: Name of the dataFrame's column referring to the number of months, that the 
    plants are blossoming
    n_months_label: Label for the number of months dimension

    id_column: Name of the dataFrame's column referring to the plant species
    id_label: Label for the plant species dimension

    family_column: Name of the dataFrame's column referring to the plant families
    family_label: Label for the plant families dimension

    title: Title of the parallel categories plot
    color_dict: Custom dictionary for the feature, containing the colors for each landscape
      
    height: Height of the plot; default is 900
    width: Width of the plot; default is 2400
    ------------------------------------------------------------------------------------------------------------
    '''
    
    # Filter data for the current landscape
    filtered_data = dataFrame[(dataFrame[n_landscapes_column] >= 3) & (dataFrame[n_months_column] >= 5)]

    # Create dimensions
    species_dim = go.parcats.Dimension(
        values = filtered_data[id_column],
        categoryorder = "category ascending", label = id_label)

    family_dim = go.parcats.Dimension(
        values=  filtered_data[family_column], label = family_label)

    n_months_dim = go.parcats.Dimension(
        values = filtered_data[n_months_column],
        categoryorder = "category ascending", label = n_months_label)

    n_present_landscapes_dim = go.parcats.Dimension(
        values=filtered_data[n_landscapes_column],
        categoryorder = "category ascending", label = n_landscapes_label)

    # Create Parcats trace with assigned colors
    parcats_trace = go.Parcats(
        dimensions = [species_dim, family_dim, n_months_dim, n_present_landscapes_dim],
        line = {"color" : filtered_data[n_landscapes_column].map(color_dict)},
        hoveron = "category", hoverinfo = "count+probability",
        labelfont = {"size" : 20, "family" : "Times"},
        tickfont = {"size" : 16, "family" : "Times"},
        arrangement = "freeform")

    # Create layout
    layout = go.Layout(
        height = height, 
        width = width, 
        title = dict(text = title, font = dict(family = "Times New Roman", size = 28)), 
        margin = dict(l = 250, r = 100, b = 100, t = 100))

    # Create figure
    fig = go.Figure(data = [parcats_trace], layout = layout)

    return fig