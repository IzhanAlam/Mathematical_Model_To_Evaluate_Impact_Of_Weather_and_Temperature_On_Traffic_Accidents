# -*- coding: utf-8 -*-
import numpy as np
import math
import pandas as pd


from plot import *


def read_weather(name):
    
    df = pd.read_csv(name, encoding = 'unicode_escape',usecols = ['Date/Time', 'Year', 'Month', 'Day', 'Max Temp', 'Min Temp', 'Mean Temp', 'Total Rain (mm)', 'Total Snow (cm)',  'Total Precip (mm)'])
    
    df.fillna(0, inplace=True)
    return df['Date/Time'].tolist(), df['Year'].tolist(), df['Month'].tolist(), df['Day'].tolist(), df['Max Temp'].tolist(), df['Min Temp'].tolist(), df['Mean Temp'].tolist(), df['Total Rain (mm)'].tolist(), df['Total Snow (cm)'].tolist(),  df['Total Precip (mm)'].tolist()


weather_data2017 = read_weather('weather_2017/weather2017.csv')
weather_data2018 = read_weather('weather_2018/weather2018.csv')
weather_data2019 = read_weather('weather_2019/weather2019.csv')


temp2017 = ([weather_data2017[0], weather_data2017[4], weather_data2017[5], weather_data2017[6]])
temp2018 = ([weather_data2018[0], weather_data2018[4], weather_data2018[5], weather_data2018[6]])
temp2019 = ([weather_data2019[0], weather_data2019[4], weather_data2019[5], weather_data2019[6]])

#rain = [7]
def rainy_days(data):
    rain = []
    days = []
    for i in range(0,len(data[0])):
        if data[7][i] != 0:
            rain.append(data[7][i])
            days.append(data[0][i])
    return [days,rain]

#snow = [8] (cm)
def snow_days(data):
    snow = []
    days = []
    for i in range(0,len(data[0])):
        if data[8][i] != 0:
            snow.append(data[8][i])
            days.append(data[0][i])
    return [days,snow]


#total precipitation = [9] (mm)
def total_precipitation(data):
    precip = []
    days = []
    for i in range(0,len(data[0])):
        if data[9][i] != 0:
            precip.append(data[9][i])
            days.append(data[0][i])
    return [days,precip]




rain2017 = rainy_days(weather_data2017)
snow2017 = snow_days(weather_data2017)
precip2017 = total_precipitation(weather_data2017)

rain2018 = rainy_days(weather_data2018)
snow2018 = snow_days(weather_data2018)
precip2018 = total_precipitation(weather_data2018)

rain2019 = rainy_days(weather_data2019)
snow2019 = snow_days(weather_data2019)
precip2019 = total_precipitation(weather_data2019)