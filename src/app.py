from csvConverter import VisualRepresentation
from mapVisualization import MapVisualization

if __name__ == "__main__":

    path = input(str("Type filepath to csv table: "))
    outputName = input(str("Type name to output jpg image: "))
    VisualRepresentation(path, outputName)

    path = input(str("Type filepath to .kml map file: "))
    outputName = input(str("Type name to output html map: "))
    MapVisualization(path, outputName)
    

print("Data created will be available in 'Output' folder")

