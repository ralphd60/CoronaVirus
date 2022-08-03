import pandas as pd

try:
    df = pd.read_csv("https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv", sep=',', index_col='Province_State')
except:
    pass

df = df.drop(['UID','iso2','iso3', 'code3', 'FIPS', 'Admin2', 'Country_Region', 'Lat', 'Long_', 'Combined_Key', 'Population'], axis=1)


df_sum = df.groupby(df.index).sum()
df_transpose = df_sum.transpose()


df_transpose.to_csv("C:\\temp\\coronavirusDeaths.csv",sep=',', header=True)



####CASES

try:
    df = pd.read_csv("https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv", sep=',', index_col='Province_State')
except:
    pass

df = df.drop(['UID','iso2','iso3', 'code3', 'FIPS', 'Admin2', 'Country_Region', 'Lat', 'Long_', 'Combined_Key'], axis=1)


df_sum = df.groupby(df.index).sum()
df_transpose = df_sum.transpose()


df_transpose.to_csv("C:\\temp\\coronavirusCases.csv",sep=',', header=True)

