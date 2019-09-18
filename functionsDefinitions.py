def getSortedCols(dataframe):
    return sorted(list(dataframe.columns))

def listColEls(dataframe, column):
    return list(dataframe.get(column))