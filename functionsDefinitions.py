import pandas as pd


def getSortedCols(dataframe):
    return sorted(list(dataframe.columns))


def listColEls(dataframe, column):
    return list(dataframe.get(column))


def getOverlappingColumns(dfA, dfB):
    dataFrames = [dfA, dfB]
    cols = [set(frame.columns) for frame in dataFrames]
    overlappingColumns = list(set.intersection(*cols))
    return overlappingColumns


def cleanMergeDataframes(dfLeft, dfRight, how='inner'):
    overlap = getOverlappingColumns(dfLeft, dfRight)
    dataMerge = pd.merge(
        left=dfLeft, right=dfRight,
        on=overlap, how=how
    )
    return dataMerge
