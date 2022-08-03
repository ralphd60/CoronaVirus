import pandas as pd

try:
    df = pd.read_csv("https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv", sep=',', index_col='Province_State')
except:
    pass

df_transpose = df.transpose()


df_transpose.to_csv("C:\\temp\\coronavirusDeathsCounty.csv",sep=',', header=True)




####CASES

try:
    df = pd.read_csv("https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv", sep=',', index_col='Province_State')
except:
    pass


df_transpose = df.transpose()


df_transpose.to_csv("C:\\temp\\coronavirusCasesCounty.csv",sep=',', header=True)

