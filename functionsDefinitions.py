import pandas as pd


def getSortedColumns(dataframe):
    # Returns a list of the dataframe's columns in alphanumerical sorting
    return sorted(list(dataframe.columns))


def listColumnElements(dataframe, column):
    # Returns a list with the elements contained in the dataframe's column
    return list(dataframe.get(column))


def getOverlappingColumns(dfA, dfB):
    # Returns a list with the columns that overlap between dataframes
    dataFrames = [dfA, dfB]
    cols = [set(frame.columns) for frame in dataFrames]
    overlappingColumns = list(set.intersection(*cols))
    return overlappingColumns


def cleanMergeDataframes(dfLeft, dfRight, how='inner'):
    # Merges two dataframes without repeated columns
    overlap = getOverlappingColumns(dfLeft, dfRight)
    dataMerge = pd.merge(
        left=dfLeft, right=dfRight,
        on=overlap, how=how
    )
    return dataMerge
