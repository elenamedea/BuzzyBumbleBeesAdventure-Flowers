import pandas as pd

from itables import init_notebook_mode
init_notebook_mode(all_interactive=True)


def max_char_length(dataFrame: pd.DataFrame) -> pd.Series:
    
    """ 
    Returns the maximum lenght of characters for the values of each column
    (useful for the database design).
    
    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)
    ------------------------------------------------------------------------------------------------------------
    
    """
    
    max_length = pd.Series({c: dataFrame[c].map(lambda x: len(str(x))).max() for c in dataFrame}).sort_values(ascending =False)

    return max_length