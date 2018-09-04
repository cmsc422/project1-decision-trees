import pandas as pd

def binarize_features(df, fare_threshold):
    '''
    Binarize `Sex` and `Fare` Columns of the given dataframe. 

    For the `Fare` column, values greater than the given `fare_threshold`
    should be set to 1 and 0 otherwise. For the `Sex` column, map `male` to 0
    and `female` to 1.
    '''

    df['Sex'] = #TODO
    df['Fare'] = #TODO

    return df.astype(int)
