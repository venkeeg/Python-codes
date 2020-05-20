# Cric T20 simulation
# Problem statement: Last 4 overs of a T20 cric match.3 wickets in hand. 40 runs to win. Percentage of 4s,6s,1s,2s,5s,0s and OUTs for each player is given.
# No run outs. Simulate the game for the last four overs.

import random
import collections
import time

##Player class with properties name,runs scored,balls faced and a run generator
class player:
  def __init__(self, name,runs_sco,balls_f,run_gen):
    self.name = name
    self.runs_sco = runs_sco
    self.balls_f = balls_f
    self.run_gen = run_gen


##Run generator variables based on the probability table given in the problem statement
## 7 means the batsman is OUT    
A_rungen = [0]*5 + [1]*30 + [2]*25 + [3]*10 + [4]*15 + [5]*1 + [6]*9 + [7]*5

B_rungen = [0]*10 + [1]*40 + [2]*20 + [3]*5 + [4]*10 + [5]*1 + [6]*4 + [7]*10

C_rungen = [0]*20 + [1]*30 + [2]*15 + [3]*5 + [4]*5  + [5]*1 + [6]*4 + [7]*20

D_rungen = [0]*30 + [1]*25 + [2]*5 + [3]*0 + [4]*5 + [5]*1 + [6]*4 + [7]*30


##scores = {'Kohli':[0,0,'NOT OUT'],'Pandya':[0,0,'NOT OUT'],'Bumrah':[0,0,'YTB'],'Nehra':[0,0,'YTB']}  # Initial scores
scores = {'Kohli':[0,0,'NOT OUT'],'Shivam Dube':[0,0,'NOT OUT']}  # Initial scores

##Incoming batsmen stored in an Ordered Dict to maintain batting order
nextin = collections.OrderedDict()
nextin.update({'W Sundar':[0,0,'YTB',C_rungen]})
nextin.update({'Navdeep Saini':[0,0,'YTB',D_rungen]})

## Intitialize striker and Nonstriker
striker = player('Kohli',0,0,A_rungen)

nonstriker = player('Shivam Dube',0,0,B_rungen)


wkts = 3  ## Wickets remaining

i = 1     ## First ball

ovrs = 4 # 4 overs remaining

team_runs = 0 # total runs scored by the players

disp_ovr=''
##Match situation
print(ovrs, " overs left",(40-team_runs), " to win.",str(wkts)+" wickets in hand ")

## Last four overs begin
while i<25 and striker is not None:   

    time.sleep(1) # Delay introduced for onlooker's convenience
    runs = random.choice(striker.run_gen)  #Score runs as per striker's probability
    disp_ovr=(str(i//6)+"."+str(i%6))      #Over number formatted

    
    if runs == 7:    # 7 is the indicator chosen for batsman getting out
      print(disp_ovr," ",striker.name + " is OUT")
      scores[striker.name]=[striker.runs_sco,(striker.balls_f + 1),'OUT']
      striker = None  #Remove the attributes of batsman who has got out
      wkts-=1         #Deduct wickets
      runs=0          #Set runs to 0
      
      ##Next batsman
      if any(nextin.values()) is not False: # Check if nextin is empty
       batsman,dtail=nextin.popitem(last=False) #extract next batsman in the order inserted - FIFO
       striker = player(batsman,dtail[0],dtail[1],dtail[3]) #New batsman

      elif any(nextin.values()) is False: # All wickets down
       print("All out !")
       break                               ##Match Over
      
    elif runs!= 7 and runs%2!=0:  # Odd no. of runs scored
      
      print(disp_ovr," ",striker.name+" scores",runs)
      striker.runs_sco = striker.runs_sco + runs # accumulate strikers runs
      striker.balls_f  = striker.balls_f  + 1    # accumulate balls faced
      scores[striker.name]=[striker.runs_sco,striker.balls_f,'NOT OUT'] #Store in Dict
      team_runs = team_runs + runs               # total runs
      
      striker,nonstriker = nonstriker,striker  ##strike change due to odd runs

    elif runs!= 7 and runs%2==0:  ## Even no. of runs scored
      
      print(disp_ovr," ",striker.name+" scores",runs)
      striker.runs_sco = striker.runs_sco + runs # accumulate strikers runs
      striker.balls_f  = striker.balls_f  + 1    # accumulate balls faced
      scores[striker.name]=[striker.runs_sco,striker.balls_f,'NOT OUT']
      team_runs = team_runs + runs
      
     
##    print( "Striker is "+striker.name,",","Nonstriker is " + nonstriker.name)

    if team_runs >= 40:  #Check for total runs
      print()
      print("Match over !")
      print("RCB won the match by ",wkts," wickets")

      break
     
    if i%6 == 0 and striker is not None :  #Last ball of the over 

       striker,nonstriker = nonstriker,striker #strike change for next over
       ovrs = ovrs - 1                         #Completion of over
       if ovrs !=0:
        print() 
        print(ovrs, " overs left",(40-team_runs), " to win.",str(wkts)+" wickets in hand ")

       elif ovrs == 0:
         break      
        
    i+=1                                    #Increment i for next ball

## Team losing and Tie situations      
if (team_runs <40): #Team loses match
  print()
  print("RCB lost the match by",(40-team_runs)," runs")

elif (team_runs == 39):      # Tie situation
  print("Its a Tie")


##Final score card
for l,m in scores.items():
    print(l,"-",m[0],"(",m[1],"balls"+")",m[2])
