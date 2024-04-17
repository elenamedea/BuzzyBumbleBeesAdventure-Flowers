import pandas as pd
import plotly.graph_objects as go


def generate_melted_pie_chart(dataFrame: pd.DataFrame, id_column: str, features: list[str], title: str, 
                              color_dict: dict[str, str], legend_title: str, title_fontsize: float = 20, 
                              height: float = 1400, width: float = 2600) -> go.Figure:
    
    '''
    Returns a pie chart for several data features (columns), after generating a melted data table for 
    these features.

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)
    id_column: Name of the dataFrame's column to be used as the id column of the melted dataFrame
    features: List of the dataFrame columns to be visualized

    title: Title of the pie chart
    color_dict: Custom dictionary for the features, containing the colors for each feature
    legend_title: Title of the pie chart's legend

    title_fontsize: Font size of the title; default is 20
    height: Height of the plot; default is 1400
    width: Width of the plot; default is 2600
    ------------------------------------------------------------------------------------------------------------
    '''
    
    fig = go.Figure()

    # Use pd.melt to reshape the data for the pie chart
    melted_data = pd.melt(dataFrame, id_vars = [id_column], value_vars = features, var_name = "Category", value_name = "Count")

    # Calculate total count for each feature
    total_counts = melted_data.groupby("Category")["Count"].sum().reset_index()


    # Add Pie trace
    fig.add_trace(go.Pie(labels = total_counts["Category"], values = total_counts["Count"], 
                         hoverinfo = "percent+label", textinfo = "percent+label",
                         marker = dict(colors = total_counts["Category"].map(color_dict)),
                         title = title, hole = 0.6,
                         insidetextfont = {"size" : 18, "family" : "Times"},
                         textfont = {"size" : 18, "family" : "Times"},
                         titlefont = {"size" : 24, "family" : "Times"}))

    # Choose pie's layout
    fig.update_layout(
        height = height,
        width = width,
        legend = dict(title = dict(text = legend_title, font = dict(family = "Times New Roman", size = title_fontsize)), font = dict(family = "Times New Roman", size = 18)))

    return fig
