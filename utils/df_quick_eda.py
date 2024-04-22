import pandas as pd
from typing import Tuple

from itables import init_notebook_mode
init_notebook_mode(all_interactive=True)


def df_quick_eda(dataFrame: pd.DataFrame) -> Tuple[Tuple[int, int], pd.Index, pd.Index, pd.Series]:

    """ 
    Returns the DataFrame's summary, shape, index, columns and number of unique values for each column.

    Parameters:
    ------------------------------------------------------------------------------------------------------------
    dataFrame: Name of a pandas DataFrame(two-dimensional, size-mutable, potentially heterogeneous tabular data)
    ------------------------------------------------------------------------------------------------------------

    """
    
    df_shape = dataFrame.shape
    df_index = dataFrame.index
    df_columns = dataFrame.columns
    df_nunique = dataFrame.nunique()
   

    return  df_shape, df_index, df_columns, df_nunique

