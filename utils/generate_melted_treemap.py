import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def generate_melted_treemap(dataFrame: pd.DataFrame, id_column: str, features: list[str], 
                            color_dict: dict[str, str], title: str, height: float = 900, 
                            width: float = 2600) -> go.Figure:

    '''
    Returns a treemap for several data features (columns), after generating a melted data table for 
    these features.

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)
    id_column: Name of the dataFrame's column to be used as the id column of the melted dataFrame
    features: List of the dataFrame columns to be visualized

    color_dict: Custom dictionary for the features, containing the colors for each feature
    title: Title of the treemap
    
    height: Height of the plot; default is 900
    width: Width of the plot; default is 2600
    ------------------------------------------------------------------------------------------------------------
    '''

    # Use pd.melt to reshape the data for the treemap
    melted_data = pd.melt(dataFrame, id_vars = [id_column], value_vars = features, var_name = "Category", value_name = "Count")

    # Create a common treemap for the specified features
    fig = px.treemap(melted_data, path = ["Category"], values = "Count", color = "Category", color_discrete_map = color_dict,
                     title = title, labels = {"Count" : "Number of Plants"})

    # Add custom data (Number of Plants) as text on the Treemap
    fig.update_traces(textinfo = "label+value+text")

    # Update treemap's layout
    fig.update_layout(height = height, 
                      width = width, 
                      title = dict(font = dict(family = "Times New Roman", size = 26)), 
                      font = dict(size = 20, family = "Times New Roman"))

    return fig
    