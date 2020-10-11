# -*- coding: utf-8 -*-

import numpy as np
import math
import pandas as pd


from plot import *

def read_traffic(name):
    
    df = pd.read_csv(name, encoding = 'unicode_escape',usecols = ['INCIDENT INFO', 'DESCRIPTION', 'START_DT', 'id'])
    
    
    return df['INCIDENT INFO'].tolist(), df['DESCRIPTION'].tolist(), df['START_DT'].tolist(), df['id'].tolist()


def read_weather(name):
    
    df = pd.read_csv(name, encoding = 'unicode_escape',usecols = ['Date/Time', 'Year', 'Month', 'Day', 'Max Temp', 'Min Temp', 'Mean Temp', 'Total Rain (mm)', 'Total Snow (cm)',  'Total Precip (mm)'])
    
    
    return df['Date/Time'].tolist(), df['Year'].tolist(), df['Month'].tolist(), df['Day'].tolist(), df['Max Temp'].tolist(), df['Min Temp'].tolist(), df['Mean Temp'].tolist(), df['Total Rain (mm)'].tolist(), df['Total Precip (mm)'].tolist()


def remove_char(lines):
    date =[]
    for i in range(0,len(lines)):
        date.append((lines[i][:2]))
    return date


def day_accident(data):
    new_data = data
    days = remove_char(new_data[2])
    for i in range(0,len(new_data[2])):
        new_data[2][i] = days[i]
    return new_data

def count_traffic(data):
    count = []
    new_data = day_accident(data)
    dm = []
    
    for x in new_data[2]:
        if x not in count:
            count.append(x)
    
    incidents = np.zeros(len(count))
    for i in range(0,len(count)):
        incidents[i] = new_data[2].count(count[i])
    
    for i in range(0,len(count)):
        dm.append((count[i][:5]))
    
    return [dm, incidents]
        

traffic_data2017 = read_traffic('Traffic_Incidents_2017.csv')
traffic_data2018 = read_traffic('Traffic_Incidents_2018.csv')
traffic_data2019 = read_traffic('Traffic_Incidents_2019.csv')

weather_data2017 = read_weather('weather_2017/weather2017.csv')
weather_data2018 = read_weather('weather_2018/weather2018.csv')
weather_data2019 = read_weather('weather_2019/weather2019.csv')

accidents2017 = count_traffic(traffic_data2017)
accidents2018 = count_traffic(traffic_data2018)
accidents2019 = count_traffic(traffic_data2019)

plot_traffic_monthly(accidents2017,2017)
plot_traffic_monthly(accidents2018,2018)
plot_traffic_monthly(accidents2019,2019)