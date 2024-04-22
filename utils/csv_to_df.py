import pandas as pd
import os
from typing import Union

from itables import init_notebook_mode
init_notebook_mode(all_interactive=True)


def csv_to_df(file_path: Union[os.PathLike, str], sep: str = ";") -> pd.DataFrame:

    """ 
    Reads a csv file into a DataFrame and returns it.

    Parameters:
    ----------------------------------------------------------------------------
    file_path: str; file path to the csv file
    sep: str, default ";"; character or regex pattern to treat as the delimiter
    ----------------------------------------------------------------------------
   
    """

    df = pd.read_csv(file_path, sep = sep)

    return df