from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse, request, response
import requests
import json
import urllib.request

from requests.api import post


def date_slice():
    return slice(10)
def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct  

def getcity():
    if request==post:
        location=request.POST['searchcity']
    else: location=("Mumbai")    
    return location






def getdata():

    loc1=getcity()


    url1="https://api.weatherapi.com/v1/forecast.json?key=b0cdb2f70d634db9ba9111218212306&q="
    url2="&days=5&aqi=no&alerts=no"
    url=url1+loc1+url2
    result=requests.get(url).json()

    return{"result":result}

def getdata2():

    loc2=getcity()
    url1="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    url2="?unitGroup=metric&key=T9AURXLDGDCWKL4ZGP837G4TB&include=fcst%2Cstats%2Chours%2Ccurrent"
    url=url1+loc2+url2
    result=requests.get(url).json()   
    return{"result":result} 


def getbgchanged(time):
    if time>6 and time<18:
        bgurl='/static/day.jpeg'

    else:
         bgurl="/static/night.jpeg"   
    return bgurl




def home(request):
    ans=getdata()
    ans1=getdata2()
    date_time=str(ans['result']['location']['localtime'])
    time0=str(ans['result']['current']['last_updated'])
    time=int(time0[11:13])
    date= date_time[date_slice()]
   

    bgimg=changebg(time)    
  

    res={
        "bgp":bgimg,
        "time":time,
        "city":ans1['result']['address'],
        "date":date,
        "current_temp":ans1['result']['currentConditions']['temp'],
        "current_pic":ans['result']['current']['condition']['icon'],
        "condition":ans1['result']['currentConditions']['conditions'],
        "current_wind":ans['result']['current']['wind_mph'], 
        "current_rain":ans['result']['forecast']['forecastday'][0]['day']['daily_chance_of_rain'],

        "c_max_temp":ans['result']['forecast']['forecastday'][0]['day']['maxtemp_c'],
        "c_min_temp":ans['result']['forecast']['forecastday'][0]['day']['mintemp_c'],
        "c_sunrise":ans['result']['forecast']['forecastday'][0]['astro']['sunrise'],
        "c_sunset":ans['result']['forecast']['forecastday'][0]['astro']['sunset'],


        "c_3am_temp":ans['result']['forecast']['forecastday'][0]['hour'][4]['temp_c'],
        "c_3am_text":ans['result']['forecast']['forecastday'][0]['hour'][4]['condition']['text'],
        "c_3am_pic":ans['result']['forecast']['forecastday'][0]['hour'][4]['condition']['icon'],

        "c_6am_temp":ans['result']['forecast']['forecastday'][0]['hour'][7]['temp_c'],
        "c_6am_text":ans['result']['forecast']['forecastday'][0]['hour'][7]['condition']['text'],
        "c_6am_pic":ans['result']['forecast']['forecastday'][0]['hour'][7]['condition']['icon'],

        "c_9am_temp":ans['result']['forecast']['forecastday'][0]['hour'][10]['temp_c'],
        "c_9am_text":ans['result']['forecast']['forecastday'][0]['hour'][10]['condition']['text'],
        "c_9am_pic":ans['result']['forecast']['forecastday'][0]['hour'][10]['condition']['icon'],

        "c_12am_temp":ans['result']['forecast']['forecastday'][0]['hour'][13]['temp_c'],
        "c_12am_text":ans['result']['forecast']['forecastday'][0]['hour'][13]['condition']['text'],
        "c_12am_pic":ans['result']['forecast']['forecastday'][0]['hour'][13]['condition']['icon'],
        
        "c_3pm_temp":ans['result']['forecast']['forecastday'][0]['hour'][16]['temp_c'],
        "c_3pm_text":ans['result']['forecast']['forecastday'][0]['hour'][16]['condition']['text'],
        "c_3pm_pic":ans['result']['forecast']['forecastday'][0]['hour'][16]['condition']['icon'],

        "c_6pm_temp":ans['result']['forecast']['forecastday'][0]['hour'][19]['temp_c'],
        "c_6pm_text":ans['result']['forecast']['forecastday'][0]['hour'][19]['condition']['text'],
        "c_6pm_pic":ans['result']['forecast']['forecastday'][0]['hour'][19]['condition']['icon'],
        
        "c_9pm_temp":ans['result']['forecast']['forecastday'][0]['hour'][22]['temp_c'],
        "c_9pm_text":ans['result']['forecast']['forecastday'][0]['hour'][22]['condition']['text'],
        "c_9pm_pic":ans['result']['forecast']['forecastday'][0]['hour'][22]['condition']['icon'],

        #day1
        "day1_date":ans['result']['forecast']['forecastday'][1]['date'],
        "day1_text":ans['result']['forecast']['forecastday'][1]['day']['condition']['text'],
        "day1_pic":"/static/"+ans1['result']['days'][1]['icon']+".png",
        "day1_low":ans['result']['forecast']['forecastday'][1]['day']["mintemp_c"],
        "day1_high":ans['result']['forecast']['forecastday'][1]['day']["maxtemp_c"],
        "day1_rain":ans['result']['forecast']['forecastday'][1]['day']['daily_chance_of_rain'],

        #day2
        "day2_date":ans['result']['forecast']['forecastday'][2]['date'],
        "day2_text":ans['result']['forecast']['forecastday'][2]['day']['condition']['text'],
        "day2_pic":"/static/"+ans1['result']['days'][2]['icon']+".png",
        "day2_low":ans['result']['forecast']['forecastday'][2]['day']["mintemp_c"],
        "day2_high":ans['result']['forecast']['forecastday'][2]['day']["maxtemp_c"],
        "day2_rain":ans['result']['forecast']['forecastday'][2]['day']['daily_chance_of_rain'],
       

        #day3
        "day3_date":ans1['result']['days'][3]['datetime'],
        "day3_text":ans1['result']['days'][3]['conditions'],
        "day3_pic":"/static/"+ans1['result']['days'][3]['icon']+".png",
        "day3_low":ans1['result']['days'][3]['tempmin'],
        "day3_high":ans1['result']['days'][3]['tempmax'],
        #"day3_rain":ans1['result']['forecast']['forecastday'][2]['day']['daily_chance_of_rain'],


        #day4
        "day4_date":ans1['result']['days'][4]['datetime'],
        "day4_text":ans1['result']['days'][4]['conditions'],
        "day4_pic":"/static/"+ans1['result']['days'][4]['icon']+".png",
        "day4_low":ans1['result']['days'][4]['tempmin'],
        "day4_high":ans1['result']['days'][4]['tempmax'],


        #day5
        "day5_date":ans1['result']['days'][5]['datetime'],
        "day5_text":ans1['result']['days'][5]['conditions'],
        "day5_pic":"/static/"+ans1['result']['days'][5]['icon']+".png",
        "day5_low":ans1['result']['days'][5]['tempmin'],
        "day5_high":ans1['result']['days'][5]['tempmax'],


    }


  
    
    return render(request,'index.htm',res)

    

#        bg='linear-gradient(to bottom, rgb(17, 22, 124) 0%, rgb(15, 137, 207) 100%)'

#        bg ='linear-gradient(to bottom, rgb(11, 14, 70) 0%, rrgb(8, 61, 92)100%)'


def changebg(time):
     if time>=6 and time<=18:
         bg="/static/day.jpeg"

     else:
         bg="/static/night.jpeg"
     return bg

# Create your views here.

def searchresult(request):
    var1=request.POST['searchcity']
    url1="https://api.weatherapi.com/v1/forecast.json?key=b0cdb2f70d634db9ba9111218212306&q="
    url2="&days=5&aqi=no&alerts=no"
    url=url1+var1+url2
    result1=requests.get(url).json() 













    url1="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    url2="?unitGroup=metric&key=T9AURXLDGDCWKL4ZGP837G4TB&include=fcst%2Cstats%2Chours%2Ccurrent"
    url=url1+var1+url2
    result2=requests.get(url).json()   

    ans={"result":result1} 
    ans1={"result":result2} 
    


    date_time=str(ans['result']['location']['localtime'])
    time0=str(ans['result']['current']['last_updated'])
    time=int(time0[11:13])
    date= date_time[date_slice()]
   

    bgimg=changebg(time)    






    res={
        "bgp":bgimg,
        "time":time,
        "city":ans1['result']['address'],
        "date":date,
        
        "city":ans1['result']['address'],
        "current_temp":ans1['result']['currentConditions']['temp'],
        "current_pic":ans['result']['current']['condition']['icon'],
        "condition":ans1['result']['currentConditions']['conditions'],
        "current_wind":ans['result']['current']['wind_mph'], 
        "current_rain":ans['result']['forecast']['forecastday'][0]['day']['daily_chance_of_rain'],

        "c_max_temp":ans['result']['forecast']['forecastday'][0]['day']['maxtemp_c'],
        "c_min_temp":ans['result']['forecast']['forecastday'][0]['day']['mintemp_c'],
        "c_sunrise":ans['result']['forecast']['forecastday'][0]['astro']['sunrise'],
        "c_sunset":ans['result']['forecast']['forecastday'][0]['astro']['sunset'],


        "c_3am_temp":ans['result']['forecast']['forecastday'][0]['hour'][4]['temp_c'],
        "c_3am_text":ans['result']['forecast']['forecastday'][0]['hour'][4]['condition']['text'],
        "c_3am_pic":ans['result']['forecast']['forecastday'][0]['hour'][4]['condition']['icon'],

        "c_6am_temp":ans['result']['forecast']['forecastday'][0]['hour'][7]['temp_c'],
        "c_6am_text":ans['result']['forecast']['forecastday'][0]['hour'][7]['condition']['text'],
        "c_6am_pic":ans['result']['forecast']['forecastday'][0]['hour'][7]['condition']['icon'],

        "c_9am_temp":ans['result']['forecast']['forecastday'][0]['hour'][10]['temp_c'],
        "c_9am_text":ans['result']['forecast']['forecastday'][0]['hour'][10]['condition']['text'],
        "c_9am_pic":ans['result']['forecast']['forecastday'][0]['hour'][10]['condition']['icon'],

        "c_12am_temp":ans['result']['forecast']['forecastday'][0]['hour'][13]['temp_c'],
        "c_12am_text":ans['result']['forecast']['forecastday'][0]['hour'][13]['condition']['text'],
        "c_12am_pic":ans['result']['forecast']['forecastday'][0]['hour'][13]['condition']['icon'],
        
        "c_3pm_temp":ans['result']['forecast']['forecastday'][0]['hour'][16]['temp_c'],
        "c_3pm_text":ans['result']['forecast']['forecastday'][0]['hour'][16]['condition']['text'],
        "c_3pm_pic":ans['result']['forecast']['forecastday'][0]['hour'][16]['condition']['icon'],

        "c_6pm_temp":ans['result']['forecast']['forecastday'][0]['hour'][19]['temp_c'],
        "c_6pm_text":ans['result']['forecast']['forecastday'][0]['hour'][19]['condition']['text'],
        "c_6pm_pic":ans['result']['forecast']['forecastday'][0]['hour'][19]['condition']['icon'],
        
        "c_9pm_temp":ans['result']['forecast']['forecastday'][0]['hour'][22]['temp_c'],
        "c_9pm_text":ans['result']['forecast']['forecastday'][0]['hour'][22]['condition']['text'],
        "c_9pm_pic":ans['result']['forecast']['forecastday'][0]['hour'][22]['condition']['icon'],

        #day1
        "day1_date":ans['result']['forecast']['forecastday'][1]['date'],
        "day1_text":ans['result']['forecast']['forecastday'][1]['day']['condition']['text'],
        "day1_pic":"/static/"+ans1['result']['days'][1]['icon']+".png",
        "day1_low":ans['result']['forecast']['forecastday'][1]['day']["mintemp_c"],
        "day1_high":ans['result']['forecast']['forecastday'][1]['day']["maxtemp_c"],
        "day1_rain":ans['result']['forecast']['forecastday'][1]['day']['daily_chance_of_rain'],

        #day2
        "day2_date":ans['result']['forecast']['forecastday'][2]['date'],
        "day2_text":ans['result']['forecast']['forecastday'][2]['day']['condition']['text'],
        "day2_pic":"/static/"+ans1['result']['days'][2]['icon']+".png",
        "day2_low":ans['result']['forecast']['forecastday'][2]['day']["mintemp_c"],
        "day2_high":ans['result']['forecast']['forecastday'][2]['day']["maxtemp_c"],
        "day2_rain":ans['result']['forecast']['forecastday'][2]['day']['daily_chance_of_rain'],
       

        #day3
        "day3_date":ans1['result']['days'][3]['datetime'],
        "day3_text":ans1['result']['days'][3]['conditions'],
        "day3_pic":"/static/"+ans1['result']['days'][3]['icon']+".png",
        "day3_low":ans1['result']['days'][3]['tempmin'],
        "day3_high":ans1['result']['days'][3]['tempmax'],
        #"day3_rain":ans1['result']['forecast']['forecastday'][2]['day']['daily_chance_of_rain'],


        #day4
        "day4_date":ans1['result']['days'][4]['datetime'],
        "day4_text":ans1['result']['days'][4]['conditions'],
        "day4_pic":"/static/"+ans1['result']['days'][4]['icon']+".png",
        "day4_low":ans1['result']['days'][4]['tempmin'],
        "day4_high":ans1['result']['days'][4]['tempmax'],


        #day5
        "day5_date":ans1['result']['days'][5]['datetime'],
        "day5_text":ans1['result']['days'][5]['conditions'],
        "day5_pic":"/static/"+ans1['result']['days'][5]['icon']+".png",
        "day5_low":ans1['result']['days'][5]['tempmin'],
        "day5_high":ans1['result']['days'][5]['tempmax'],


    }



    return render(request,"resultweather.htm",res)


