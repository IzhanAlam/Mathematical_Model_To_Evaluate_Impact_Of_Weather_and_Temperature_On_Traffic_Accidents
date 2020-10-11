# -*- coding: utf-8 -*-

import numpy as np
import math
import pandas as pd


from plot import *

def read_traffic(name):
    
    df = pd.read_csv(name, encoding = 'unicode_escape',usecols = ['INCIDENT INFO', 'DESCRIPTION', 'START_DT', 'id'])
    
    
    return df['INCIDENT INFO'].tolist(), df['DESCRIPTION'].tolist(), df['START_DT'].tolist(), df['id'].tolist()



def remove_char(lines):
    date =[]
    for i in range(0,len(lines)):
        date.append((lines[i][:10]))
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
        dm.append((count[i][:10]))
    
    return [dm, incidents]
        

traffic_data2017 = read_traffic('Traffic_Incidents_2017.csv')
traffic_data2018 = read_traffic('Traffic_Incidents_2018.csv')
traffic_data2019 = read_traffic('Traffic_Incidents_2019.csv')


accidents2017 = count_traffic(traffic_data2017)
accidents2018 = count_traffic(traffic_data2018)
accidents2019 = count_traffic(traffic_data2019)

#plot_traffic(accidents2017)