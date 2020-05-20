# This script calls cric_stats.py
import cric_stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

cols = ['Result','Team Runs','Kohli Runs', 'Kohli bfaced', 'Kohli ON','S Dube Runs','S Dube bfaced',\
        'S Dube ON','W Sundar Runs','W Sundar bfaced','W Sundar ON','N Saini Runs','N Saini bfaced','N Saini ON']


stats = pd.DataFrame(columns=cols)

stats[['Team Runs','Kohli Runs', 'Kohli bfaced','S Dube Runs','S Dube bfaced',\
        'W Sundar Runs','W Sundar bfaced','N Saini Runs','N Saini bfaced']] = stats[['Team Runs','Kohli Runs', 'Kohli bfaced','S Dube Runs','S Dube bfaced',\
        'W Sundar Runs','W Sundar bfaced','N Saini Runs','N Saini bfaced']].apply(pd.to_numeric)

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns',50)

##Set initial values
kohli_runs=0
kohli_bfaced=0
kohli_ON=''

dube_runs = 0
dube_bfaced = 0
dube_ON = ''

sundar_runs = 0
sundar_bfaced = 0
sundar_ON =''

saini_runs = 0
saini_bfaced = 0
saini_ON = ''

print("Simulation in progress...")
for i in range(200):
    
    cric_stats.play()

    for l,m in cric_stats.scores.items():
##        print(l,"-",m[0],"(",m[1],"balls"+")",m[2])

        if l=='Kohli':
            kohli_runs = m[0]
            kohli_bfaced = m[1]
            kohli_ON = m[2]
        elif l=='Shivam Dube':
            dube_runs = m[0]
            dube_bfaced =m[1]
            dube_ON = m[2]
        elif l== 'W Sundar':
            sundar_runs = m[0]
            sundar_bfaced = m[1]
            sundar_ON = m[2]
        elif l== 'Navdeep Saini':
            saini_runs = m[0]
            saini_bfaced = m[1]
            saini_ON = m[2]          

    stats=stats.append({'Result':cric_stats.result,'Team Runs':cric_stats.team_runs,'Kohli Runs':kohli_runs, 'Kohli bfaced':kohli_bfaced, 'Kohli ON':kohli_ON,\
                        'S Dube Runs':dube_runs,'S Dube bfaced':dube_bfaced,'S Dube ON':dube_ON,'W Sundar Runs':sundar_runs,'W Sundar bfaced':sundar_bfaced\
                        ,'W Sundar ON':sundar_ON,'N Saini Runs':saini_runs,'N Saini bfaced':saini_bfaced,'N Saini ON':saini_ON},ignore_index=True)
    

    #Clear variables after every simulation
    kohli_runs=0
    kohli_bfaced=0
    kohli_ON=''

    dube_runs = 0
    dube_bfaced = 0
    dube_ON = ''

    sundar_runs = 0
    sundar_bfaced = 0
    sundar_ON =''

    saini_runs = 0
    saini_bfaced = 0
    saini_ON = ''

print("Simulation complete.Data stored in pandas dataframe #stats#")






