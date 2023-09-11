# This algorithm is developed by X. Zhong, D. Enke, but written by Wyett. Please do not use this as I probably make fatal mistake somewhere in my code.
# If you really want to use this please don't make any financial decision from this

import Yahoo
from StLouisFred import FRED
import datetime


def getStockData():
    df = Yahoo.getDailyPrices(
        {"BCM": "3328.HK", "CEB": "6818.HK", "BOC": "3988.HK", "CNCB": "0998.HK"}
    )

    return df


def getData():
    df = getStockData()
    return df


df = getData()
print(df)
df.to_excel("LSTM Input data.xlsx")
