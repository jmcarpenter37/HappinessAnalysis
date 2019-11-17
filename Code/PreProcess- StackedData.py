#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd
df2015= pd.read_csv("../2015.csv")

df2016= pd.read_csv("../2016.csv")
df2017= pd.read_csv("../2017.csv")

df2015['year'] = 2015
df2016['year'] = 2016
df2017['year'] = 2017


# In[53]:


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
#df1.merge(df2, left_on='lkey', right_on='rkey')


# In[54]:


stacked_data = df2015.append(df2016)
stacked_data = stacked_data.append(df2017)
#stacked_data[stacked_data['Country'] == "Taiwan Province of China"]


# In[55]:


stacked_data


# In[56]:


stacked_data.to_csv("../full_data.csv", index = False)

