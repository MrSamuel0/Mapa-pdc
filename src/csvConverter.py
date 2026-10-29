import pandas as pd
import dataframe_image as dfi

def VisualRepresentation(filePath: str, outname: str):

    df = pd.read_csv(filePath, sep=None, engine="python")
    dfi.export(df, f"./output/{outname}.png")

    return "Operation Successful"