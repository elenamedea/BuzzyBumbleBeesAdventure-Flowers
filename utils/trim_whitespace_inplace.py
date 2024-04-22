import pandas as pd

from itables import init_notebook_mode
init_notebook_mode(all_interactive=True)


def trim_whitespace_inplace(dataFrame: pd.DataFrame):

    """ 
    
    Removes extra leading and tailing whitespace from the values of the DataFrame's columns. 

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)
    ------------------------------------------------------------------------------------------------------------

    """

    # Custom function to trim whitespace from a single value
    def trim_whitespace(value):

        if isinstance(value, str):

            return value.strip()
        
        else:

            return value


    # Iterating over the dataFrame's columns
    for i in dataFrame.columns:
         
        # Checking datatype of each column; when there are only null values the datatype is float64
        if dataFrame[i].dtype == 'object':
            
            # Applying strip function on column's values
            dataFrame[i] = dataFrame[i].map(trim_whitespace)
        else: 
            
            # If condition is False then it will do nothing
            pass