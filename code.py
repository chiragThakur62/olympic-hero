# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data=pd.read_csv(path)

data.rename(columns = {"Total": "Total_Medals"},inplace=True)

data.head()
#Code starts here



# --------------
#Code starts here



data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')

data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])

better_event=data['Better_Event'].value_counts().idxmax()

print(better_event)


# --------------
#Code starts here




top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

top_countries.drop(top_countries.index[-1:],inplace=True)

#print(top_countries[-1:])

def top_ten(top_countries,column):
     
    country_list=[]
    #top_10 += '_column'
    top_10=top_countries.nlargest(10, column)

    country_list=list(top_10['Country_Name'])
    return country_list

top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')


common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)


# --------------
#Code starts here



top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')

summer_df=data[data["Country_Name"].isin(top_10_summer) ]
winter_df=data[data["Country_Name"].isin(top_10_winter) ]
top_df=data[data["Country_Name"].isin(top_10) ]

plt.plot(summer_df["Country_Name"], summer_df["Total_Summer"]) 
plt.plot(winter_df["Country_Name"], winter_df["Total_Winter"]) 
plt.plot(top_df["Country_Name"], top_df["Total_Medals"]) 
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show() 


# --------------
#Code starts here

summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']

#print(summer_df[summer_df['Golden_Ratio']=summer_df['Golden_Ratio'].max()])
summer_df=summer_df.loc[summer_df['Golden_Ratio'].idxmax()]
summer_max_ratio=summer_df['Golden_Ratio']
summer_country_gold=summer_df['Country_Name']


winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']

#print(summer_df[summer_df['Golden_Ratio']=summer_df['Golden_Ratio'].max()])
winter_df=winter_df.loc[winter_df['Golden_Ratio'].idxmax()]
winter_max_ratio=winter_df['Golden_Ratio']
winter_country_gold=winter_df['Country_Name']


top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']

#print(summer_df[summer_df['Golden_Ratio']=summer_df['Golden_Ratio'].max()])
top_df=top_df.loc[top_df['Golden_Ratio'].idxmax()]
top_max_ratio=top_df['Golden_Ratio']
top_country_gold=top_df['Country_Name']



# --------------
#Code starts here


data_1=data[:-1]

#top_countries.drop(top_countries.index[-1:],inplace=True)

data_1['Total_Points']=data_1['Gold_Total']*3+data_1['Silver_Total']*2+data_1['Bronze_Total']*1




most_points=max(data_1['Total_Points'])
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']


# --------------
#Code starts here

best=data[data['Country_Name']==best_country]

print(best)

best=best[['Gold_Total','Silver_Total','Bronze_Total']]


best.plot.bar(stacked=True)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
#plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))

plt.show()


