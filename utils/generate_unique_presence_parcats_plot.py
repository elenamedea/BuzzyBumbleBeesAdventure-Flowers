import pandas as pd
import plotly.graph_objects as go


def generate_unique_presence_parcats_plot(dataFrame: pd.DataFrame, n_landscapes_column: str, id_column: str, 
                                   id_label: str, landscapes: list[str], landscapes_label: str, color_column: str, 
                                   title: str, color_dict: dict[str, str], height: float = 1200, 
                                   width: float = 2400) -> go.Figure:

    '''
    Returns a parallel categories plot of plant species, which are present only in one landscape.
    In the plot the landscapes could also be visible by using the respective color mapping.

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)
    n_landscapes_column: Name of the dataFrame's column referring to the number of landscapes, where the 
    plants are present
   
    id_column: Name of the dataFrame's column referring to the plant species
    id_label: Label for the plant species dimension

    landscapes:  List of the landscape's dataFrame columns to be visualized
    landscapes_label: Label for the number of landscapes dimension

    color_column: Name of the dataFrame's column to be used for color
    title: Title of the parallel categories plot
    color_dict: Custom dictionary for the feature, containing the colors for each value
      
    height: Height of the plot; default is 1200
    width: Width of the plot; default is 2400
    ------------------------------------------------------------------------------------------------------------
    '''

    # Filter data for the current landscape
    one_present_landscape_data = dataFrame[dataFrame[n_landscapes_column] == 1]

    # Melt the DataFrame to long format for plotting
    melted_data = pd.melt(one_present_landscape_data, id_vars = [id_column], value_vars = landscapes,
                          var_name = "Landscape", value_name = "Presence")

    # Sort the DataFrame by Id and "Presence" in ascending order
    melted_data = melted_data.sort_values([id_column, "Presence"])

    # Filter data for the current landscape
    landscape_presence_data = melted_data[melted_data["Presence"] == True]

    # Create dimensions
    landscape_name_dim = go.parcats.Dimension(
        values = landscape_presence_data["Landscape"],
        categoryorder = "category ascending", label = landscapes_label)

    species_dim = go.parcats.Dimension(
        values = landscape_presence_data[id_column], label = id_label)

    # Create Parcats trace with assigned colors
    parcats_trace = go.Parcats(
        dimensions = [landscape_name_dim, species_dim],
        line = {"color" : landscape_presence_data[color_column].map(color_dict)},
        hoveron = "color",
        hoverinfo = "count+probability",
        labelfont = {"size" : 20, "family" : "Times"},
        tickfont = {"size" : 16, "family" : "Times"},
        arrangement = "freeform")

    # Create layout
    layout = go.Layout(
        height = height, 
        width = width, 
        title = dict(text = title, font = dict(family = "Times New Roman", size = 28)), 
        margin = dict(l = 100, r = 250, b = 100, t = 100))

    # Create figure
    fig = go.Figure(data = [parcats_trace], layout = layout)

    return fig