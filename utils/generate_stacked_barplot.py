import pandas as pd
import plotly.graph_objects as go


def generate_stacked_barplot(dataFrame: pd.DataFrame, feature: str, title: str, color_dict: dict[str, str], 
                       legend_title: str, height: float = 1200, width: float = 2600) -> go.Figure:

    '''
    Returns a stacked bar chart for one data's feature (column).

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)
    feature: Name of the dataFrame's column to be visualized

    title: Title of the bar chart
    color_dict: Custom dictionary for the feature, containing the colors for each value
    legend_title: Title of the bar chart's legend
    
    height: Height of the plot; default is 1200
    width: Width of the plot; default is 2600
    ------------------------------------------------------------------------------------------------------------
    '''

    # Count values for the bar chart
    feature_counts = dataFrame[feature].value_counts()

    # Create a list of traces for each category
    traces = []
    for feat in feature_counts.index:
        feat_data = dataFrame[dataFrame[feature] == feat]
        trace = go.Bar(x = feat_data[feature], y = feat_data.groupby(feature).size(), name = feat, marker_color = color_dict[feat])
        traces.append(trace)

    # Create layout
    layout = go.Layout(
        title = title, titlefont = {"size" : 24, "family" : "Times"},
        xaxis = dict(title = "Familie", titlefont = dict(size = 20, family = "Times New Roman"), tickfont = dict(size = 16, family = "Times New Roman")),
        yaxis = dict(title = "Anzahl", titlefont = dict(size = 20, family = "Times New Roman"), tickfont = dict(size = 16, family = "Times New Roman")),
        barmode = "stack"
    )

    # Create figure
    fig = go.Figure(data = traces, layout = layout)

    # Update layout
    fig.update_layout(
        height = height,
        width = width,
        legend = dict(title = dict(text = legend_title, font = dict(family = "Times New Roman", size = 20)),  # Set legend title and its font size
        traceorder = "normal",  # Set the trace order to "normal" (ascending)
        font = dict(family = "Times New Roman", size = 13.5)))  # Set legend font size
    
    return fig