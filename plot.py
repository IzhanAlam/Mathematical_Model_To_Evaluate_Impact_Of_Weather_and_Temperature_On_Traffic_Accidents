# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

def plot_traffic_monthly(traffic,year):
    
    fig = plt.figure(num=None, figsize=(24, 6), dpi=80, facecolor='w', edgecolor='k')
    ax = fig.add_subplot(1,1,1) 
    string = 'Monthly Accidents Year: ', str(year)
    string2 = "monthly_traffic_accodents"+str(year)+".jpg"
    ax.set_xlabel("Month")
    ax.set_ylabel("Number of Accidents")
    ax.set_title(string)
    ax.set_xticklabels(traffic[0],rotation=90)
    for i, v in enumerate(traffic[1]):
        ax.text(i - 0.25, v + 0.05, str(v), color='blue', fontweight='bold')
    ax.bar(traffic[0],traffic[1])
    plt.savefig(string2)
    plt.show()
    
    
def plot_traffic_temp(data):
    fig = plt.figure(num=None, figsize=(24, 6), dpi=60, facecolor='w', edgecolor='k')
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel("Temperature (celcius)")
    ax.set_ylabel("Number of Accidents")
    ax.set_title("Correlation between Temperature and Traffic Accidents")
    x = data[1]
    y = data[2]
   
    
    
    ax.scatter(x,y)
    
    
    
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)(x)
    
    ax.plot(x,p(y),'r--')
    text = "y=%.6fx+(%.6f)"%(z[0],z[1])
    p2 = np.poly1d(z)(x)
    
    r2 = r2_score(y, p2)
    text2 = "R2: ",str(r2)
    plt.gca().text(0.05, 0.95, text,transform=plt.gca().transAxes,
     fontsize=14, verticalalignment='top')
    
    plt.gca().text(0.05, 0.8, text2,transform=plt.gca().transAxes,
     fontsize=14, verticalalignment='top')
    
    plt.show()