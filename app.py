from flask import Flask
import requests
import json
import time
import math
import os
from flask import Flask, render_template, url_for, json, send_from_directory
from pathlib import Path
from collections import defaultdict
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.cli.command()
def process():
    print('starting')
    """Run scheduled job."""
    countyMap = {
      "ADAMS": {
         "covid_region": 3
      },
      "ALEXANDER": {
         "covid_region": 5
      },
      "BOND": {
         "covid_region": 4
      },
      "BOONE": {
         "covid_region": 1
      },
      "BROWN": {
         "covid_region": 3
      },
      "BUREAU": {
         "covid_region": 2
      },                   
      "CALHOUN": {
         "covid_region": 3
      },
      "CARROLL": {
         "covid_region": 1
      },
      "CASS": {
         "covid_region": 3
      },
      "CHAMPAIGN": {
         "covid_region": 6
      },
      "CHICAGO": {
         "covid_region": 11
      },
      "CHRISTIAN": {
         "covid_region": 3
      },
      "CLARK": {
         "covid_region": 6
      },
      "CLAY": {
         "covid_region": 6
      },
      "CLINTON": {
         "covid_region": 4
      },
      "COLES": {
         "covid_region": 6
      },
      "COOK": {
         "covid_region": 10
      },
      "CRAWFORD": {
         "covid_region": 6
      },
      "CUMBERLAND": {
         "covid_region": 6
      },
      "DE WITT": {
         "covid_region": 6
      },
      "DEKALB": {
         "covid_region": 1
      },
      "DOUGLAS": {
         "covid_region": 6
      },
      "DUPAGE": {
         "covid_region": 8
      },
      "EDGAR": {
         "covid_region": 6
      },
      "EDWARDS": {
         "covid_region": 5
      },
      "EFFINGHAM": {
         "covid_region": 6
      },
      "FAYETTE": {
         "covid_region": 6
      },
      "FORD": {
         "covid_region": 6
      },
      "FRANKLIN": {
         "covid_region": 5
      },
      "FULTON": {
         "covid_region": 2
      },
      "GALLATIN": {
         "covid_region": 5
      },
      "GREENE": {
         "covid_region": 3
      },
      "GRUNDY": {
         "covid_region": 2
      },
      "HAMILTON": {
         "covid_region": 5
      },
      "HANCOCK": {
         "covid_region": 3
      },
      "HARDIN": {
         "covid_region": 5
      },
      "HENDERSON": {
         "covid_region": 2
      },
      "HENRY": {
         "covid_region": 2
      },
      "IROQUOIS": {
         "covid_region": 6
      },
      "JACKSON": {
         "covid_region": 5
      },
      "JASPER": {
         "covid_region": 6
      },
      "JEFFERSON": {
         "covid_region": 5
      },
      "JERSEY": {
         "covid_region": 3
      },
      "JO DAVIESS": {
         "covid_region": 1
      },
      "JOHNSON": {
         "covid_region": 5
      },
      "KANE": {
         "covid_region": 8
      },
      "KANKAKEE": {
         "covid_region": 7
      },
      "KENDALL": {
         "covid_region": 2
      },
      "KNOX": {
         "covid_region": 2
      },
      "LAKE": {
         "covid_region": 9
      },
      "LASALLE": {
         "covid_region": 2
      },
      "LAWRENCE": {
         "covid_region": 6
      },
      "LEE": {
         "covid_region": 1
      },
      "LIVINGSTON": {
         "covid_region": 2
      },
      "LOGAN": {
         "covid_region": 3
      },
      "MACON": {
         "covid_region": 6
      },
      "MACOUPIN": {
         "covid_region": 3
      },
      "MADISON": {
         "covid_region": 4
      },
      "MARION": {
         "covid_region": 5
      },
      "MARSHALL": {
         "covid_region": 2
      },
      "MASON": {
         "covid_region": 3
      },
      "MASSAC": {
         "covid_region": 5
      },
      "MCDONOUGH": {
         "covid_region": 2
      },
      "MCHENRY": {
         "covid_region": 9
      },
      "MCLEAN": {
         "covid_region": 2
      },
      "MENARD": {
         "covid_region": 3
      },
      "MERCER": {
         "covid_region": 2
      },
      "MONROE": {
         "covid_region": 4
      },
      "MONTGOMERY": {
         "covid_region": 3
      },
      "MORGAN": {
         "covid_region": 3
      },
      "MOULTRIE": {
         "covid_region": 6
      },
      "OGLE": {
         "covid_region": 1
      },
      "PEORIA": {
         "covid_region": 2
      },
      "PERRY": {
         "covid_region": 5
      },
      "PIATT": {
         "covid_region": 6
      },
      "PIKE": {
         "covid_region": 3
      },
      "POPE": {
         "covid_region": 5
      },
      "PULASKI": {
         "covid_region": 5
      },
      "PUTNAM": {
         "covid_region": 2
      },
      "RANDOLPH": {
         "covid_region": 4
      },
      "RICHLAND": {
         "covid_region": 6
      },
      "ROCK ISLAND": {
         "covid_region": 2
      },
      "SALINE": {
         "covid_region": 5
      },
      "SANGAMON": {
         "covid_region": 3
      },
      "SCHUYLER": {
         "covid_region": 3 
      },
      "SCOTT": {
         "covid_region": 3
      },
      "SHELBY": {
         "covid_region": 6
      },
      "ST. CLAIR": {
         "covid_region": 4
      },
      "STARK": {
         "covid_region": 2
      },
      "STEPHENSON": {
         "covid_region": 1
      },
      "TAZEWELL": {
         "covid_region": 2
      },
      "UNION": {
         "covid_region": 5
      },
      "VERMILION": {
         "covid_region": 6
      },
      "WABASH": {
         "covid_region": 5
      },
      "WARREN": {
         "covid_region": 2
      },
      "WASHINGTON": {
         "covid_region": 4
      },
      "WAYNE": {
         "covid_region": 5
      },
      "WHITE": {
         "covid_region": 5
      },
      "WHITESIDE": {
         "covid_region": 1
      },
      "WILL": {
         "covid_region": 7
      },
      "WILLIAMSON": {
         "covid_region": 5
      },
      "WINNEBAGO": {
         "covid_region": 1
      },
      "WOODFORD": {
         "covid_region": 2
      },
      "ILLINOIS": {
         "covid_region": 0
      }
    }
    cdt_url = 'https://idph.illinois.gov/DPHPublicInformation/api/COVID/GetCountyHistorical?countyName='
    test_url = 'https://idph.illinois.gov/DPHPublicInformation/api/COVID/GetCountyHistorical?countyName='
    vacc_url = 'https://idph.illinois.gov/DPHPublicInformation/api/COVIDVaccine/getVaccineAdministration?CountyName='
    
    cli_url = 'https://idph.illinois.gov/DPHPublicInformation/api/COVIDExport/GetResurgenceDataCLIAdmissions'
    cdt_urls = []
    test_urls = []
    vacc_urls = []

    # cdt = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11] #array 
    cdt = {}
    
    for county in countyMap:
       cdt_urls.append(cdt_url + county)
       test_urls.append(test_url + county)
       vacc_urls.append(vacc_url + county)
    
    # group county arrays by region
    for url in cdt_urls:
        r = requests.get(url)
        json_data = json.loads(r.text)
        county = url.split('=')[-1]
        region = countyMap[county.upper()]['covid_region']
        # cdt[region] = json_data['values']
        if region in cdt:
            cdt[region] += json_data['values']
        else:
            cdt[region] = json_data['values']
    
    # consolidate = {}
    # consolidate = defaultdict(list)
    consolidate = []    
    for i in range(12):
        consolidate.append([])
    # for int in dict of object lists 
    for region in cdt:
        # after the first loop, stop on the first repeated date
        firstdate = cdt[region][0]['ReportDate']
        once = False
        for datum in cdt[region]:

            if (firstdate == datum['ReportDate'] and once):
                break
            
            once = True

            # all objects with same date in region 
            nextsamedate = [item for item in cdt[region] if item['ReportDate']==datum['ReportDate']]

            CasesChangeSum = 0
            CumulativeCasesSum = 0
            DeathsSum = 0
            DeathsChangeSum = 0
            TotalTestedSum = 0
            TotalTestedChangeSum = 0
            TestPositivity = 0

            # all counties with same day in region    
            for day in nextsamedate:
                CasesChangeSum += day['CasesChange']
                CumulativeCasesSum += day['CumulativeCases']
                DeathsSum += day['Deaths']
                DeathsChangeSum += day['DeathsChange']
                TotalTestedSum += day['TotalTested']
                if day['TotalTestedChange'] > 2000000:
                    TotalTestedChangeSum = TotalTestedChangeSum
                else:
                    TotalTestedChangeSum += day['TotalTestedChange']
                
                if (TotalTestedChangeSum > 0):
                    TestPositivity = CasesChangeSum / TotalTestedChangeSum
                else:
                    TestPositivity = 0

            entry = {
                "confirmed_cases_change": CasesChangeSum,
                "CumulativeCases": CumulativeCasesSum,
                "Deaths": DeathsSum,
                "deaths_change": DeathsChangeSum,
                "date": datum['ReportDate'],
                "TotalTested": TotalTestedSum,
                "tested_change": TotalTestedChangeSum,
                "test_positivity": TestPositivity
            }

            # this should just be a list of lists 
            # print(region)
            consolidate[region].append(entry)
    
    # for each region array 
    POINTS_AVG = 7
    # for region in consolidate:
    for region in range(len(consolidate)):
        cases_sum = 0
        deaths_sum = 0
        test_pos_sum = 0
        tests_sum = 0

        i = 0
        # iterate to 6th day 
        while i < (POINTS_AVG - 1):
            # add tests/etc to sum 
            cases_sum += consolidate[region][i]['confirmed_cases_change']
            deaths_sum += consolidate[region][i]['deaths_change']
            test_pos_sum += consolidate[region][i]['test_positivity']
            tests_sum += consolidate[region][i]['tested_change']

            # day[avg = sum / day 
            if i < 1:
                consolidate[region][i]['cases_avg'] = cases_sum
                consolidate[region][i]['deaths_avg'] = deaths_sum
                consolidate[region][i]['test_pos_avg'] = test_pos_sum
                consolidate[region][i]['tests_avg'] = tests_sum
            else:
                consolidate[region][i]['cases_avg'] = cases_sum / i
                consolidate[region][i]['deaths_avg'] = deaths_sum / i
                consolidate[region][i]['test_pos_avg'] = test_pos_sum / i
                consolidate[region][i]['tests_avg'] = tests_sum / i
            i += 1

        # iterate from 7th to last day 
        while (i < len(consolidate[region])):
            # add to sum 
            cases_sum += consolidate[region][i]['confirmed_cases_change']
            deaths_sum += consolidate[region][i]['deaths_change']
            test_pos_sum += consolidate[region][i]['test_positivity']
            tests_sum += consolidate[region][i]['tested_change']
            # record avg = sum / 7 
            consolidate[region][i]['cases_avg'] = cases_sum / POINTS_AVG
            consolidate[region][i]['deaths_avg'] = deaths_sum / POINTS_AVG
            consolidate[region][i]['test_pos_avg'] = test_pos_sum / POINTS_AVG
            consolidate[region][i]['tests_avg'] = tests_sum / POINTS_AVG
            # sum -= earliest day added to sum -= values[i-N+1]

            cases_sum -= consolidate[region][i - POINTS_AVG + 1]['confirmed_cases_change']
            deaths_sum -= consolidate[region][i - POINTS_AVG + 1]['deaths_change']
            test_pos_sum -= consolidate[region][i - POINTS_AVG + 1]['test_positivity']
            tests_sum -= consolidate[region][i - POINTS_AVG + 1]['tested_change']

            i += 1
            
    ## cases_avg: 300
    ## deaths_avg: 1
    ## test_pos_avg: 0.034672976712329294
    ## tests_avg: 9037
    # test_positivity: 0.041373009658052726
    # tested_change: 7662
    # deaths_change: 0 
    # confirmed_cases_change: 317
    # date: Tue Nov 16 2021 00:00:00 GMT-0500 (Eastern Standard Time) {}

    
    cdtbase = Path()
    jsonpath = cdtbase / ("cdt.json")
    cdtbase.mkdir(exist_ok=True)
    jsonpath.write_text(json.dumps(consolidate, indent=4))


    # print('done')    
    # for url in test_urls:
    #     r = requests.get(url)
    #     json_data = json.loads(r.text)
    #     county = url.split('=')[-1]
    #     base = Path('TESTS')
    #     jsonpath = base / (county + ".json")
    #     base.mkdir(exist_ok=True)
    #     jsonpath.write_text(json.dumps(json_data, indent=4))

    # for url in vacc_urls:
    #     r = requests.get(url)
    #     json_data = json.loads(r.text)
    #     county = url.split('=')[-1]
    #     base = Path('VACCINE')
    #     jsonpath = base / (county + ".json")
    #     base.mkdir(exist_ok=True)
    #     jsonpath.write_text(json.dumps(json_data, indent=4))
    
    # r = requests.get(cli_url)
    # json_data = json.loads(r.text)
    # base = Path('CLI')
    # jsonpath = base / ("GetResurgenceDataCLIAdmissions.json")
    # base.mkdir(exist_ok=True)
    # jsonpath.write_text(json.dumps(json_data, indent=4))

