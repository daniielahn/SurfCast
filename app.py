# app.py

from flask import Flask, render_template
import requests
import json
import re

CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

app = Flask(__name__)

@app.route('/')
def index():

    #Wedge Info
    wedgeCondition = requests.get("https://services.surfline.com/kbyg/regions/forecasts/conditions?spotId=5842041f4e65fad6a770882b")
    wedgeConditions1 = wedgeCondition.json()
    wedgeReport = requests.get("https://services.surfline.com/kbyg/spots/reports?spotId=5842041f4e65fad6a770882b")
    wedgeReport1 = wedgeReport.json()
    jsonString = json.dumps(wedgeReport1)

    #print(jsonString)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

    

    wedgeInfo = {
       'min' : wedgeReport1['forecast']['waveHeight']['min'],
       'max' : wedgeReport1['forecast']['waveHeight']['max'],
       'humanRelation' : wedgeReport1['forecast']['waveHeight']['humanRelation'],
       'forecastDay' : wedgeConditions1['data']['conditions'][0]['forecastDay'],
       'forecaster' : wedgeReport1['report']['forecaster']['name'],
       'observation' : cleanhtml(wedgeReport1['report']['body']),
       'waterTemp' : wedgeReport1['forecast']['waterTemp']['min'],
       'temp' : wedgeReport1['forecast']['weather']['temperature'],
    }

    #Churches Info
    
    churchCondition = requests.get("https://services.surfline.com/kbyg/regions/forecasts/conditions?spotId=5842041f4e65fad6a770888b")
    churchConditions1 = churchCondition.json()
    churchReport = requests.get("https://services.surfline.com/kbyg/spots/reports?spotId=5842041f4e65fad6a770888b")
    churchReport1 = churchReport.json()
    #jsonString = json.dumps()

    churchInfo = {
       'min' : churchReport1['forecast']['waveHeight']['min'],
       'max' : churchReport1['forecast']['waveHeight']['max'],
       'humanRelation' : churchReport1['forecast']['waveHeight']['humanRelation'],
       'forecastDay' : churchConditions1['data']['conditions'][0]['forecastDay'],
       'forecaster' : churchReport1['report']['forecaster']['name'],
       'observation' : cleanhtml(churchReport1['report']['body']),
       'waterTemp' : churchReport1['forecast']['waterTemp']['min'],
       'temp' : churchReport1['forecast']['weather']['temperature'],
    }

    #LowerTrestles Info
    
    lowerCondition = requests.get("https://services.surfline.com/kbyg/regions/forecasts/conditions?spotId=5842041f4e65fad6a770888a")
    lowerConditions1 = lowerCondition.json()
    lowerReport = requests.get("https://services.surfline.com/kbyg/spots/reports?spotId=5842041f4e65fad6a770888a")
    lowerReport1 = lowerReport.json()
    #jsonString = json.dumps()

    lowerInfo = {
       'min' : lowerReport1['forecast']['waveHeight']['min'],
       'max' : lowerReport1['forecast']['waveHeight']['max'],
       'humanRelation' : lowerReport1['forecast']['waveHeight']['humanRelation'],
       'forecastDay' : lowerConditions1['data']['conditions'][0]['forecastDay'],
       'forecaster' : lowerReport1['report']['forecaster']['name'],
       'observation' : cleanhtml(lowerReport1['report']['body']),
       'waterTemp' : lowerReport1['forecast']['waterTemp']['min'],
       'temp' : lowerReport1['forecast']['weather']['temperature'],
    }



    return render_template("index.html", wedgeInfo=wedgeInfo, churchInfo=churchInfo, lowerInfo=lowerInfo)

if __name__ == "__main__":
    app.run()
