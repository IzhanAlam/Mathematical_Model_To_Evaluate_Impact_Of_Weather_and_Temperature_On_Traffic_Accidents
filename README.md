**Step 1: Identifying the Problem/ Problem Statement**

Studies have been done prior to determine the correlation between weather and vehicular accidents. Ultimately, there is a correlation between low temperatures and vehicle accidents (Andreescu, 1997).  There are many factors which contribute to this correlation. Take for example, a less noticeable factor such as a driver’s psyche. Drivers often report a change of behaviour such as a decrease in speed (Summala, 2006), which in turn affects the flow of traffic and can lead to more accidents.However, such factors cannot be accurately determined, and thus, the relation between accidents and weather should be looked at directly. One such method is to directly relate the precipitation/temperature to the number of accidents that have occured (Andreescu, 1997), and then determine the accuracy of the results. However, this method struggles in accurately determining the trend of weather correlated accidents in the future. 

The goal of this study was to analyze the impact the weather and temperature has on a traffic accident. By analyzing this data, we are able to understand at which times and conditions road maintenance should be improved. This can also allow us to better analyze the cause of an accident and determine how much of it was impacted by the weather and how much of it was based on other factors such as visibility. To accomplish this,a mathematical model needs to be used which can be used to assess accident risk based on weather for future dates without the need of knowing the number of traffic accidents nor the annual weather of that year. In other words, to develop a model which can directly relate temperature and weather conditions to the number of accidents which will occur. It is important to understand the effect the environment plays on a traffic accident. By analyzing this, we are able to see at which times and conditions road maintenance is lacking. 

Before developing the mathematical model, it is important to distinguish what the word accident entails to. For this model, an accident was defined as a collision between two vehicles, a vehicle and a pedestrian, or a vehicle and an object. Weather was classified based on temperature, and precipitation (snow, and rain). 

**Step 2: Conceptual Model**

![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image18.png)


**Assumptions:**

When developing the model, several assumptions were made. First and foremost, the risk was used to assess three different types of weather conditions consisting of snow, rain, and clear (none). This was largely due to the availability of the data. Most free data sources only carried information regarding snow and rain. Different weather types such as hail and sleet were not recorded by the organization which we obtained our data from. Another assumption that we made during the development of this model was the fact we did not take into account the time of the day when the accident occured, but rather, whether or not there was precipitation when the accident occured.  Another important thing to note is the severity of the accident was also not taken into account. Accidents were treated the same regardless of severity. This was done on purpose to ensure the weights of the accidents remained the same throughout the year to allow for a better risk assessment. This mathematical model also made the assumption that the overall trend of temperature and weather conditions will be close to that of previous years. Another important thing to note is that although there may be different factors which affect the number of accidents only variables which could be directly measured were used.

**Data Collection/Acquisition:**

The weather data came from the Government of Canada’s historical weather database. The years which were collected consisted of 2017, 2018, and 2019. The first two years served as a means to develop the model, and the 2019 data served as a means of validation for the model. It should also be noted the station used was labelled as ‘Calgary Intl A’, which was located in the Calgary airport. The primary data which was extracted from the database consisted of the date, the maximum, minimum, and mean temperature associated with the date, as well as the total rain precipitation, snow precipitation, and overall precipitation (in mm) for that particular day. The temperature recorded was the air temperature 2m off the surface. 

The traffic data was taken from the City of Calgary’s open data database. From this data, we extracted the date of accident, the number of vehicles involved, the description of the accident, and the id. Although the data provided accurate accident descriptions and dates, it lacked volume. As mentioned in the problem statement, the CIty of Calgary reported 46021 accidents in the year of 2017. However, the open data database only recorded ~5242 accidents. This resulted in a large decrease of sample size. We were unable to find a more accurate database of traffic collisions for Calgary, likely due to the privacy of the data. On top of this, there was a lack of data in the summer months of 2019. This will be further explained in the computational model. 

Once all the data was collected, the weather data was sorted into two categories consisting of temperature and weather types. Traffic accidents were then related to the weather data based on dates. The temperature data was divided into bins to make sure a single temperature did not influence the significance of the others. It was found that a bin size of 2°C was best for temperature. Categorizing and sorting was done through Python code which can be found attached.

**Step 3: Computational Model**

The first step in developing the computational model was to assess the impact the weather condition (rain and snow) plays on the number of traffic accidents which occur. This was done through a risk assessment formula(Norman, 2000) , slightly modified as follows:





![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image1.png)		(1)

Where:

![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image2.png)= Accident risk for precipitation type



![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image3.png) = Number of accidents per type of precipitation (t) and month (m)


![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image4.png)= Number of hours in that month



![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image5.png)= Number of accidents in a month



![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image6.png)= Number of hours with that type of precipitation in the month



![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image7.png) = Number of months

The first step in applying this risk assessment was to determine the number of accidents on a particular date, as well as the weather conditions. The monthly number of accidents in clear weather, in snow, and in rain were sorted from the dataset which yielded the value of ![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image3.png) . 

The hours of precipitation per month were not available from the chosen database. To accommodate for this, we used the total rain/snow precipitation and divided by the average rain/snow precipitation which falls in an hour. This allowed us to get approximate values for the hours of precipitation per month(

![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image6.png)

). We calculated this risk assessment for the years of 2017 and 2018. 

After calculating the accident risk for the different weather types, we decided to average the accident risks between the two years. This was to ensure the impact of outliers would be reduced. 

The next step was to incorporate the accident risk with the temperature to ensure the final accident risks are based on the temperature and weather conditions. To accomplish this, we first first gathered the temperatures and the date associated with them. Each date was classified as ‘Snow’, ‘Rain’, or ‘Clear’, depending on the amount of precipitation. From there, the number of accidents associated with the date were multiplied by their respective accident risk (i.e. if it was a snow day, the accident risk for snow was multiplied by the number of traffic accidents which occured on that day). This yielded an adjusted version of traffic accidents which takes into account the type of precipitation on that day. This process is summarized in the equation below:



![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image8.png)	(2)

Once the precipitation type and the number of accidents were linked, we then linked the temperature and the number of accidents. This was done in a relatively simple manner. We simply modelled the number of adjusted accidents which occured between a temperature range such as 

![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image9.png)

. The trend line was then found for this model for the years of 2017 and 2018. Note that most of the positive temperatures were intentionally left out as the traffic data for the year of 2019 was missing accidents which occurred during the summer months.

The average trendlines from 2017 and 2018 were then used as the final trendline. This trendline was then used to model the temperature and the number of accidents which occured to obtain the predicted number of accidents in relation to the temperature for the year of 2019. The predicted number of accidents in relation to temperature were then compared to the observed to evaluate the model which will be discussed in the section ‘Evaluation of the Model’.

Lastly, to find the probability of an accident  associated with a temperature bin, the following equations were used:



![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image10.png)		(3)



![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image11.png)		(4)



![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image12.png)		(5)

**Step 4: Evaluation of the Model**:

Model Calibration:

The model created as an empirical model which means that parameter identification is reliant on the field data acquisition. A number of factors might enhance the relation of these parameters, such as separating the data based on seasons, or comparing the trends of weather for the years of 2017 and 2018 to that of previous years. However, this was not done as it was assumed that the trend of weather stays consistent. Outliers were removed from the dataset such as during winter blasts which had much higher recorded accidents.

Model Validation:

The evaluation of the model was conducted in terms of a predictive validation. That is, it examines the ability to forecast an issue of interest.  The model used empirical relations generated from 2017 and 2018 traffic accidents and their corresponding weather conditions to predict the number of traffic accidents that happened in 2019. The accuracy of the prediction was evaluated as a statistical/quantitative approach, specifically, the coefficient of determination, 

![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image13.png). This value varies between 0 and 1, which indicates whether none of the data variance is captured, or all of it is, respectively. The coefficient of determination is highly sensitive to outliers as they are far from the mean. During the model evaluation, we removed outliers that were greater than 

![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image14.png)

.. As a rule of thumbs, if  a value can capture 62.5% of the variance, or higher, it  can be considered as a reasonably good fit in a biological system (Hassan, 2018). Before comparing the predicted value with the observed values, the accident risk under different weather conditions were calculated as described in equation 1. As Table 1 illustrates, the risk index for traffic accidents under different weather conditions were calculated based on 2017 and 2018 data respectively. It was computed yearly because the weather conditions over the two years are different.

 Table 1: Accident Risk Calculation for Year 2017, 2018 based on equation (1).


<table>
  <tr>
   <td>Year
   </td>
   <td>Accident Risk (Clear)
   </td>
   <td>Accident Risk (Rain)
   </td>
   <td>Accident Risk (Snow)
   </td>
  </tr>
  <tr>
   <td>2017
   </td>
   <td>0.875048133
   </td>
   <td>1.26807314
   </td>
   <td>0.865350569
   </td>
  </tr>
  <tr>
   <td>2018
   </td>
   <td>1.235982331
   </td>
   <td>4.46631102
   </td>
   <td>0.895190946
   </td>
  </tr>
</table>


As mentioned in the computational method section, the environmental condition was then categorized in terms of the minimum surface temperature measured on the day the traffic accident occurred. The weather conditions associated with each accident were incorporated via equation 2. The number of accidents at each temperature interval for 2017 and the 2018 are shown in figure 1 and figure 2.  The coefficient of determination for 2017 data was found to be 0.7836 and the coefficient of determination for the 2018 data was found to be 0.7288. Both values suggest a relatively strong correlation between the two inputs. In other words, most of the variability was able to be captured. 

 

![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image15.png)





Figure 1. correlation between number of accidents happened and the minimum surface temperature measured for 2017

 

![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image16.png)




Figure 2. correlation between number of accidents happened and the minimum surface temperature measured for 2018

The trendlines for the years of 2017, and 2018 were then averaged, which was then used to model the predicted accidents occurring at each temperature interval. According to figure 3, the  coefficient of determination was determined to be 0.7027 indicating a relatively strong correlation under the biological modelling context. Figures 1, 2, and 3 show a linear increase in the number of accidents occurring as temperature rises. However, this is not entirely accurate. There were more days with a higher temperature than those of lower temperatures which yields a larger amount of traffic accidents. 

An accident/temperature risk assessment was performed to gain more insight out of an accident being related to temperature. Equations (3), (4), and (5) were used to perform this accident to temperature risk. This allows us to gain an insight as to which temperature ranges cause the most accidents. Figure 4 shows the result of this. The higher the index is at a particular temperature, the higher the likelihood an accident occurs at that temperature. We found the coefficient of determination to be 0.6 (comparing the actual risk of an accident at a temperature to the predicted risk). This is not as high as the previously determined values, but still suitable for a system with as many variables as this one. Figure 4 also showcases that as temperature decreases, the likelihood of an accident occurring increases. 

Sensitivity Analysis:

For sensitivity analysis, the Pearson’s Correlation Coefficient was determined. This determines the relationship between two variables of interest, which in this case are the predicted and observed values. The Pearson’s correlation coefficient (r) for 2019 predicted vs observed was calculated as 0.837228378 which indicates a good correlation has been observed in the validation scenario. The Pearson’s correlation coefficient (r)  for accident/temperature risk assessment was calculated as 0.68182781 which is adequate for a biological system. 



![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image17.png)






Figure 3. Model validation between modelled result and observed result in 2019

 

 

![alt_text](https://github.com/IzhanAlam/Mathematical_Model_To_Evaluate_Impact_Of_Weather_and_Temperature_On_Traffic_Accidents/blob/main/images/image19.png)





Figure 4. The ratio of accidents occurring at a temperature (r2 = 0.6)

 

**Conclusion**:

The scope of this project was to develop an environmental model which can be used to assess the risk of an accident occurring based on temperature and weather in the future. The impact of weather conditions on an accident were done through a risk assessment as explained in equation (1). This was then used to weigh the accidents according to the weather. The number of accidents were then plotted against temperature intervals to determine the trend lines which would allow us to predict the number of traffic accidents in relation to the weather and temperature for the year of 2019. An accident to temperature risk index was also calculated to help visualize the results. The model was validated via the correlation of coefficient which yielded a value of 0.7027 and 0.68182781 when comparing the predicted values to the actual values for the number of accidents at each temperature, and the accident to temperature risk, respectively. This indicates that the model is well-validated and yields above average results. Through this model, we can observe that as temperature decreases, the chance an accident occurs is higher. On top of this, rain has the highest accident to weather risk indicating that Calgary drivers are not as used to driving in the rain than they are in the snow or clear conditions. 

This model was limited by the availability of the data. The traffic accidents data used did not coincide with the actual number of reported accidents from the City of Calgary’s report. This meant that we were not able to accurately plot the number of accidents to higher temperatures as data from the summer months were missing which would skew the data. The model also assumed consistent weather and temperature from year to year which is likely not going to happen because of climate change. On top of this, this data is only applicable for the City of Calgary, as other regions have much different weather conditions. 

Understanding road safety is useful for analysis and prevention. One potential application of this model would be the ability to use this for road maintenance in winter. We can observe that the highest risk of an accident occurs at lower temperatures. At this temperature, the road is likely covered in ice or snow which will result in more accidents. This means that the road maintenance in winter for Calgary is not as adequate as it should be. Poor weather negatively impacts road conditions, and the risk of an accident increases.Another application of this model is that once we learn the impact of weather and temperature on traffic accidents, we can analyze the impact of other factors much better. In other words, we can limit the effects of weather and temperature on an accident and look solely towards other factors such as the lighting conditions.

References

[1]   R. Ivers, K. Brown, R. Norton, and M. Stevenson, “Road Traffic Injuries,” _International Encyclopedia of Public Health_. pp. 393–400, 2016, doi: 10.1016/B978-0-12-803678-5.00391-X.

[2]   City of Calgary, “2017 Traffic Collision Summary.” pp. 2–5, 2018, [Online]. Available: https://pub-calgary.escribemeetings.com/filestream.ashx?DocumentId=78003.

[3]   L. F. Miranda-Moreno, P. Morency, and A. M. El-Geneidy, “The link between built environment, pedestrian activity and pedestrian-vehicle collision occurrence at signalized intersections,” _Accid. Anal. Prev._, vol. 43, no. 5, pp. 1624–1634, 2011, doi: 10.1016/j.aap.2011.02.005.

[4]   Spencer Gallichan-lowe, “Winter weather causes over 100 crashes on Calgary roads - Calgary _ Globalnews,” Global News, Mar. 16, 2018.

[5] Andreescu, M. and Frost, D., 1998. Weather and traffic accidents in Montreal, Canada. _Climate Research_, 9, pp.225-230.

[6] Norrman, J., Eriksson, M. and Lindqvist, S., 2000. Relationships between road slipperiness, traffic accident risk and winter road maintenance activity. _Climate Research_, 15, pp.185-193.

[7] Hassan, Q., 2020. [online] Prism.ucalgary.ca. Available at: https://prism.ucalgary.ca/bitstream/handle/1880/106247/Lec_06_Model_validation.pdf?sequence=14&isAllowed=y [Accessed 8 April 2020].
