import pandas as pd
import plotly.graph_objects as go


def generate_blossoming_time_barplot(dataFrame: pd.DataFrame, id_column: str, time_columns: list[str], 
                               xaxis_title: str, yaxis_title: str, title: str, color_dict: dict[str, str], 
                               height: float = 900, width: float = 1600) -> go.Figure:
 
    '''
    Returns a stacked bar chart for several time features (columns), after generating a melted data table for 
    these features.

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)
    id_column: Name of the dataFrame's column to be used as the id column of the melted dataFrame

    time_columns: List of the dataFrame time columns (e.g. months, seasons) to be visualized

    xaxis_title: Title of the x-axis
    yaxis_title: Title of the y-axis
    title: Title of the bar chart
    color_dict: Custom dictionary for the True boolean value

    height: Height of the plot; default is 900
    width: Width of the plot; default is 1600
    ------------------------------------------------------------------------------------------------------------
    '''

    # Melt the DataFrame for easy plotting
    melted_data = pd.melt(dataFrame, id_vars = [id_column], value_vars = time_columns, var_name = xaxis_title, value_name = yaxis_title)

    # Replace True with "TRUE" in the count column
    melted_data[yaxis_title] = melted_data[yaxis_title].replace(True, "TRUE")

    # Filter out FALSE and (TRUE) values
    melted_data = melted_data[melted_data[yaxis_title] == "TRUE"]

    # Initialize the figure
    fig = go.Figure()

    # Iterate through unique values in count column and create a trace for each
    for value in melted_data[yaxis_title].unique():
        subset_data = melted_data[melted_data[yaxis_title] == value]
        trace = go.Bar(
            x = subset_data[xaxis_title],
            y = [1] * len(subset_data),  # Use a constant y value for each bar
            name = value,
            showlegend = True,
            marker = dict(color = color_dict.get(value, "gray"))
        )
        fig.add_trace(trace)

    # Choose bar's layout
    layout = go.Layout(
        height = height,
        width = width,
        title = dict(text = title, font = dict(size = 24, family = "Times New Roman")),
        xaxis = dict(title = xaxis_title, titlefont = dict(size = 20, family = "Times New Roman"), tickfont = dict(size = 18, family = "Times New Roman")),
        yaxis = dict(title = yaxis_title, titlefont = dict(size = 20, family = "Times New Roman"), tickfont = dict(size = 18, family = "Times New Roman")),
        showlegend = False)

    # Update layout
    fig.update_layout(layout)

    return fig