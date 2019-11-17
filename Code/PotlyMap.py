import pandas as pd
import plotly.express as px
try:
    df2015= pd.read_csv(r"C:\Users\jmcarpenter\Desktop\UVA Graduate School Stuff\CS_DataScience_5010\CS_5010\CS_Project\HappinessAnalysis\2015.csv")
    df2016= pd.read_csv(r"C:\Users\jmcarpenter\Desktop\UVA Graduate School Stuff\CS_DataScience_5010\CS_5010\CS_Project\HappinessAnalysis\2016.csv")
    df2017= pd.read_csv(r"C:\Users\jmcarpenter\Desktop\UVA Graduate School Stuff\CS_DataScience_5010\CS_5010\CS_Project\HappinessAnalysis\2017.csv")
    print("Read data is successful.")
except NotADirectoryError as err:
    print(err)
    print("Could not read these files in")

df2015['year'] = 2015
df2016['year'] = 2016
df2017['year'] = 2017

df2017= df2017.rename(columns={'Happiness.Rank': 'Happiness Rank', 'Happiness.Score':'Happiness Score',
       'Economy..GDP.per.Capita.':'Economy (GDP per Capita)',  'Health..Life.Expectancy.':'Health (Life Expectancy)',
       'Trust..Government.Corruption.':'Trust (Government Corruption)',
       'Dystopia.Residual':'Dystopia Residual'})

df2017 = df2017.replace(to_replace ="Hong Kong S.A.R., China",
                 value ="Hong Kong")
df2017 = df2017.replace(to_replace ="Taiwan Province of China",
                 value ="Taiwan")

region_df = df2016[['Country', 'Region']]
df2017 = df2017.merge(region_df, how = 'left', on = 'Country' )
stacked_data = df2015.append(df2016)
stacked_data = stacked_data.append(df2017)

df2015['year'] = 2015
df2016['year'] = 2016
df2017['year'] = 2017

df2017= df2017.rename(columns={'Happiness.Rank': 'Happiness Rank', 'Happiness.Score':'Happiness Score','Economy..GDP.per.Capita.':'Economy (GDP per Capita)',  'Health..Life.Expectancy.':'Health (Life Expectancy)','Trust..Government.Corruption.':'Trust (Government Corruption)','Dystopia.Residual':'Dystopia Residual'})
df2017 =df2017.replace(to_replace ="Hong Kong S.A.R., China", value ="Hong Kong")
df2017 =df2017.replace(to_replace ="Taiwan Province of China",value ="Taiwan")

region_df = df2016[['Country', 'Region']]
df2017 = df2017.merge(region_df, how = 'left', on = 'Country' )
stacked_data = df2015.append(df2016)
stacked_data = stacked_data.append(df2017)

gapminder = px.data.gapminder().query("year==2007")

#gapminder
df = stacked_data.merge(gapminder[['country', 'iso_alpha']], how = 'left', left_on = "Country", right_on = "country" )
fig = px.choropleth(df[df['year'] ==2017], locations="iso_alpha",color="Health (Life Expectancy)",hover_name="Country", color_continuous_scale=px.colors.sequential.Hot)
fig.show()