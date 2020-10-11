# -*- coding: utf-8 -*-

from traffic_daily import *
from weather import *
import datetime

def change_date(traffic_data):
    
    for i in range(0,len(traffic_data[0])):
        traffic_data[0][i]=datetime.datetime.strptime(traffic_data[0][i], '%m/%d/%Y').strftime('%Y-%m-%d')
    
    return traffic_data



def freq(data, interval):
    
    max_num = max(data[2])
    max_num = math.ceil(max_num)
    min_num = min(data[2])
    min_num = round(min_num)
    inter = np.arange(min_num,max_num,interval)
    count = np.zeros(len(inter))
    accidents = np.zeros(len(inter))
    condition = np.zeros(len(inter))

    
    for i in range (0, len(inter)-1):
        for j in range (0, len(data[2])):
            if inter[i] < data[2][j] <= inter[i+1]:
                count[i] = count[i] + 1
                
                
                accidents[i] = accidents[i] + data[1][j] 
                condition[i] = condition[i] + data[3][j]
    return [count, inter, accidents, condition]

def temp_collisions(collisions, temp):
    
    date = []
    min_temp = []

    for i in range(0, len(temp[0])):
        if temp[0][i] in collisions[0]:
            date.append(temp[0][i])
            min_temp.append(temp[2][i])
       
            
    return [date, collisions[1], min_temp]




def risk(collisions, rain, snow):
    date = []
    number_acc =[]
    new_val = []
    
    s = (0.895190946+0.865350569)/2
    c = (0.875048133+0.875048133)/2
    r = (4.46631102+1.26807314)/2

    risk = []

    

    for i in range(0,len(collisions[1])):
        if collisions[0][i] in rain[0]:
            date.append(collisions[0][i])
            number_acc.append(collisions[1][i])
            new_val.append('Rain Day')
            risk.append(r*number_acc[i])
        elif collisions[0][i] in snow[0]:
            date.append(collisions[0][i])
            number_acc.append(collisions[1][i])
            new_val.append('Snow Day')
            risk.append(s*number_acc[i])
        else:
            date.append(collisions[0][i])
            number_acc.append(collisions[1][i])
            new_val.append('Clear Day')
            risk.append(c*number_acc[i])
    
    snow_days = 0
    rain_days = 0
    clear_days = 0
    
    snow_days_acc = 0
    rain_days_acc= 0
    clear_days_acc = 0
    
    for i in range(0,len(date)):
        if new_val[i] == 'Snow Day':
            snow_days = snow_days + 1
            snow_days_acc = snow_days_acc + number_acc[i]
        elif new_val[i] == 'Rain Day':
            rain_days = rain_days + 1
            rain_days_acc = rain_days_acc + number_acc[i]
        else:
            clear_days = clear_days + 1
            clear_days_acc = clear_days_acc + number_acc[i]
        
    days = [rain_days_acc, snow_days_acc, clear_days_acc]
    
    return risk
            
    


    


collisions2017 = change_date(accidents2017)

temp_collisions2017 = temp_collisions(collisions2017,temp2017)

collisions2018 = change_date(accidents2018)

temp_collisions2018 = temp_collisions(collisions2018,temp2018)


collisions2019 = change_date(accidents2019)

temp_collisions2019 = temp_collisions(collisions2019,temp2019)

risk2017 = risk(collisions2017,rain2017,snow2017)

risk2018 = risk(collisions2018,rain2018,snow2018)

risk2019 = risk(collisions2019,rain2019,snow2019)

conditionrisk2017 = [temp_collisions2017[0], temp_collisions2017[1], temp_collisions2017[2], risk2017]
freq2017 = freq(conditionrisk2017,2)

conditionrisk2018 = [temp_collisions2018[0], temp_collisions2018[1], temp_collisions2018[2], risk2018]
freq2018 = freq(conditionrisk2018,2)

conditionrisk2019 = [temp_collisions2019[0], temp_collisions2019[1], temp_collisions2019[2], risk2019]
freq2019 = freq(conditionrisk2019,2)




'''
y2 = np.delete(freq2017[2],29)
y = []
for i in range(0,len(y2)):
    y.append(3.2728*y2[i]+125.91)


r2 = r2_score(y2,y)
'''
#plot_traffic_temp(freq2017)
