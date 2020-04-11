# Import our dependencies
import pandas as pd
import numpy as np
import io
url='https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
df=pd.read_csv(url, dtype={
            "date" : str,
            "country" : str,
            "state" : str,
            "fibs" : str,
            "cases" : str,
            "death" : str
        })
df=df.drop(columns=['fips'])
df["id"]=df["county"]
df.to_json('data.json', orient='records')

