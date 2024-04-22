import pandas as pd
import plotly.graph_objects as go


def generate_three_features_parcats_plot(dataFrame: pd.DataFrame, true_column: str, true_column_label: str, 
                                       n_landscapes_column: str, n_landscapes_label: str, family_column: str, 
                                       family_label: str, title: str, color_dict: dict[int, str], 
                                       height: float = 1200, width: float = 2400) -> go.Figure:
    
    '''
    Returns a parallel categories plots of a plants' subset (e.g. bordering/transition plants) 
    regarding the number of landscapes it is present and the plant families which consist it.

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)

    true_column: Name of the dataFrame's column, of which the True values will be explored 
    true_column_label: Label for the true_column dimension

    n_landscapes_column: Name of the dataFrame's column referring to the number of landscapes, where the 
    plants are present
    n_landscapes_label: Label for the number of landscapes dimension

    family_column: Name of the dataFrame's column referring to the plant families
    family_label: Label for the plant families dimension

    title: Title of the parallel categories plot
    color_dict: Custom dictionary for the feature, containing the colors for each landscape
      
    height: Height of the plot; default is 1200
    width: Width of the plot; default is 2400
    ------------------------------------------------------------------------------------------------------------
    '''

    # Filter the data
    df2 = dataFrame[dataFrame[true_column] == True]

    # Create dimensions
    n_present_landscapes_dim = go.parcats.Dimension(
        values = df2[n_landscapes_column],
        categoryorder = "category ascending", label = n_landscapes_label)

    bordering_dim = go.parcats.Dimension(
        values = df2[true_column], label = true_column_label)

    family_dim = go.parcats.Dimension(
        values = df2[family_column], label = family_label)

    # Create Parcats trace with assigned colors
    parcats_trace = go.Parcats(
        dimensions = [bordering_dim, n_present_landscapes_dim, family_dim],
        line = {"color" : df2[n_landscapes_column].map(color_dict)},
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