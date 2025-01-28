#Laptops will be visualized y matplotlib

import matplotlib.pyplot as plt
import pandas as pd
class VisualizeData():
    def __init__(self):
        self.visualize()
    def visualize(self):
        #read data from DarazLaptops.csv
        df = pd.read_csv("DarazLaptops.csv", index_col=0)
        print(df.head())                #checking few rows of the data for validity
        print(df.columns)
        #plotting the data
        #will continue
v = VisualizeData()
