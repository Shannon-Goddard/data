# Import our dependencies
import pandas as pd
import numpy as np
import io
url='https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
df=pd.read_csv(url)
df.to_json (r'C:\Users\User\Desktop\data\data.json')

