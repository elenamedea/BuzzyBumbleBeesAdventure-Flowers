import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def generate_species_treemap(dataFrame: pd.DataFrame, feature: str, species_column: str, family_column: str, 
                             title: str, color_dict: dict[str, str], height: float = 900,
                             width: float = 2600) -> go.Figure:

    '''
    Returns a treemap of plant species for one data feature (column), when this feature is equal to TRUE. 
    In the treemap the plant families are also visible and are used for the color mapping.

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)
    feature:  Name of the dataFrame's column to be visualized
    
    species_column: Name of the dataFrame's column referring to plant species
    family_column: Name of the dataFrame's column referring to plant families
    
    title: Title of the treemap
    color_dict: Custom dictionary for the feature, containing the colors for each value
      
    height: Height of the plot; default is 900
    width: Width of the plot; default is 2600
    ------------------------------------------------------------------------------------------------------------
    '''

    # Filter data for the current feature
    feature_data = dataFrame[dataFrame[feature] == True]

    # Group by the feature and count the occurrences
    grouped_data = feature_data.groupby([species_column, family_column]).size().reset_index(name = "Count")

    # Create a treemap chart for the current feature
    fig = px.treemap(grouped_data, path = [family_column, species_column], values = "Count", 
                     color = family_column, color_discrete_map = color_dict)

    # Update treemap's layout
    fig.update_layout(height = height, 
                      width = width, 
                      title = dict(text = title, font = dict(family = "Times New Roman", size = 26)), 
                      font = dict(size = 18, family = "Times New Roman"))

    return fig 