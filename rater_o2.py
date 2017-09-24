import pandas as pd
import numpy as np
import time

df=pd.read_csv('test2.csv')#reading csv file
data = {}#creating dictionary as player name as key value

for i in range(0,len(df.index.values)):# print(len(df.index))
# print(df.index.values)
	player_1=df.loc[i]#taking index 0 of the data frame
	player_1=player_1.values#getting the values 
	data[player_1[0]] = [player_1[i] for i in range(1,len(player_1))]#putting values in the dic
#print(data)
###################################################
# ab=[]
# ab.append(np.nan)
# if np.isnan(ab).any():
# 	print(ab)
###################################################
def player_batsman_score_match(runs, balls, sr, out, batting_order):
	score=0
	if (np.isnan(runs)):
		return 450
	else:	
		if (batting_order==0):#openers
			if (out==1):
				if (balls>=0 and balls<20):
					if (runs<20):
						score=runs
					elif(runs>=20 and runs<25):
						score=runs
					elif (runs>=25 and runs<30):
						score=runs*4
					elif (runs>=30 and runs<50):
						score=runs*9.5
					elif (runs>=50):
						score=502				
				elif (balls<40 and balls>=20):
					if (runs<=20):
						score=runs*1
					elif (runs>20 and runs<=25):
						score=(runs*4)
					elif (runs>25 and runs<43):
						score=runs*3		
					elif (runs>43):
						if (runs<=150):
							score=runs*6
						else :
							score=1000		
				elif balls>=40 and balls<=80:
					if (runs<15):
						score=runs
					elif (runs>=15 and runs<30):
						score=runs*4
					elif(runs>=30 and runs<=40):
						score=runs*5
					if (runs>40 and runs>=balls and runs<=balls+19):
						score=(runs+(runs-balls))*6.36
						if (score<300):
							score+=150
					elif (runs>40 and runs<balls):
						score=450		
				elif balls>80 :
					if (sr>=300):
						score=1000
					elif (sr<300 and sr>250):
						score=997
					elif (sr<=250 and sr>200):
						score=995
					elif (sr<=200 and sr>160):
						score=992
					elif (sr<=160 and sr>150):
						score=990
					elif (sr<=150 and sr>=130):
						score=sr*6.3
					elif (sr<130 and sr>120):
						score=sr*6.4
					elif (sr<=120 and sr>115):
						score=sr*6.62
					elif (sr<=115 and sr>110):
						score=sr*6.62
					elif (sr<=110 and sr>105):
						score=sr*6.62
					elif (sr<=105 and sr>100):
						score=sr*6.8
					elif (sr<=100 and sr>95):
						score=sr*6.9
					elif (sr<=95 and sr>=90):
						score=sr*6.99
					else:
						score=sr*7.17	
			else:
				if (sr>=300):
					score=1000
				elif (sr<300 and sr>250):
					score=997
				elif (sr<=250 and sr>200):
					score=995
				elif (sr<=200 and sr>160):
					score=992
				elif (sr<=160 and sr>150):
					score=990
				elif (sr<=150 and sr>=130):
					score=sr*6.328
				elif (sr<130 and sr>120):
					score=sr*6.42
				elif (sr<=120 and sr>115):
					score=sr*6.64
				elif (sr<=115 and sr>110):
					score=sr*6.64
				elif (sr<=110 and sr>105):
					score=sr*6.64
				elif (sr<=105 and sr>100):
					score=sr*6.83
				elif (sr<=100 and sr>95):
					score=sr*6.92
				elif (sr<=95 and sr>=90):
					score=sr*7.1
				else:
					score=sr*7.19															
		
		if (batting_order>0 and batting_order<6):#middle order
			if (out==1):
				if (balls>=0 and balls<10):
					if (sr>=300):
						score=700
					elif (sr<300 and sr>=250):
						score=sr+400
					elif (sr<250 and sr>=170):
						score=sr+405
					elif (sr<170 and sr>=120):
						score=sr*3.42
					elif (sr<120):
						score=sr*3.4	
				elif (balls>=10 and balls<25):
					if (sr>=300):
						score=720
					elif (sr<300 and sr>=250):
						score=sr+420
					elif (sr<250 and sr>=170):
						score=sr+409
					elif (sr<170 and sr>=120):
						score=sr*3.44
					elif (sr<120):
						score=sr*3.42
				elif (balls>=25 and balls<30):
					if (sr>=300):
						score=730
					elif (sr<300 and sr>=250):
						score=sr+425
					elif (sr<250 and sr>=170):
						score=sr+412
					elif (sr<170 and sr>=120):
						score=sr*3.449
					elif (sr<120):
						score=sr*3.427
				elif (balls>=30 and balls<40):
					if (sr>=300):
						score=740
					elif (sr<300 and sr>=250):
						score=sr+430
					elif (sr<250 and sr>=170):
						score=sr+417
					elif (sr<170 and sr>=120):
						score=sr*3.47
					elif (sr<120):
						score=sr*3.43
				elif (balls>=40 and balls<=60):
					if (sr>=300):
						score=1000
					elif (sr<300 and sr>=250):
						score=980
					elif (sr<250 and sr>=170):
						score=sr+730
					elif (sr<170 and sr>=140):
						score=sr*4.2+30
					elif (sr<140 and sr>=100):
						score=sr+490
					elif (sr<100 and sr>=80):
						score=550
					elif (sr<80):
						score=sr*5.63		
				elif (balls>60 and balls<80):
					if (sr>=300):
						score=1000
					elif (sr<300 and sr>=250):
						score=982
					elif (sr<250 and sr>=170):
						score=sr+732
					elif (sr<170 and sr>=140):
						score=sr*4.21+30
					elif (sr<140 and sr>=100):
						score=sr+492
					elif (sr<100 and sr>=80):
						score=556
					elif (sr<80):
						score=sr*5.636
				elif (balls>=80 and balls<100):
					if (sr>=300):
						score=1000
					elif (sr<300 and sr>=250):
						score=988
					elif (sr<250 and sr>=170):
						score=sr+738
					elif (sr<170 and sr>=140):
						score=sr*4.26+30
					elif (sr<140 and sr>=100):
						score=sr+496
					elif (sr<100 and sr>=80):
						score=sr*5.7
					elif (sr<80):
						score=sr*5.636
				elif (balls>=100):	
					if (sr>=300):
						score=1000
					elif (sr<300 and sr>250):
						score=997
					elif (sr<=250 and sr>200):
						score=995
					elif (sr<=200 and sr>160):
						score=992
					elif (sr<=160 and sr>150):
						score=990
					elif (sr<=150 and sr>=130):
						score=sr*6.3
					elif (sr<130 and sr>120):
						score=sr*6.4
					elif (sr<=120 and sr>115):
						score=sr*6.62
					elif (sr<=115 and sr>110):
						score=sr*6.62
					elif (sr<=110 and sr>105):
						score=sr*6.62
					elif (sr<=105 and sr>100):
						score=sr*6.8
					elif (sr<=100 and sr>95):
						score=sr*6.9
					elif (sr<=95 and sr>=90):
						score=sr*6.99
					else:
						score=sr*7.17
			if (out==0):
				if (balls>=0 and balls<10):
					if (sr>=300):
						score=700
					elif (sr<300 and sr>=250):
						score=sr+400
					elif (sr<250 and sr>=170):
						score=sr+405
					elif (sr<170 and sr>=120):
						score=sr*3.42
					elif (sr<120):
						score=sr*3.4	
				elif (balls>=10 and balls<25):
					if (sr>=300):
						score=720
					elif (sr<300 and sr>=250):
						score=sr+420
					elif (sr<250 and sr>=170):
						score=sr+409
					elif (sr<170 and sr>=120):
						score=sr*3.44
					elif (sr<120):
						score=sr*3.42
				elif (balls>=25 and balls<30):
					if (sr>=300):
						score=730
					elif (sr<300 and sr>=250):
						score=sr+425
					elif (sr<250 and sr>=170):
						score=sr+412
					elif (sr<170 and sr>=120):
						score=sr*3.449
					elif (sr<120):
						score=sr*3.427
				elif (balls>=30 and balls<40):
					if (sr>=300):
						score=740
					elif (sr<300 and sr>=250):
						score=sr+430
					elif (sr<250 and sr>=170):
						score=sr+417
					elif (sr<170 and sr>=120):
						score=sr*3.47
					elif (sr<120):
						score=sr*3.43
				elif (balls>=40 and balls<=60):
					if (sr>=300):
						score=1000
					elif (sr<300 and sr>=250):
						score=980
					elif (sr<250 and sr>=170):
						score=sr+730
					elif (sr<170 and sr>=140):
						score=sr*4.2+30
					elif (sr<140 and sr>=100):
						score=sr+490
					elif (sr<100 and sr>=80):
						score=550
					elif (sr<80):
						score=sr*5.63		
				elif (balls>60 and balls<80):
					if (sr>=300):
						score=1000
					elif (sr<300 and sr>=250):
						score=982
					elif (sr<250 and sr>=170):
						score=sr+732
					elif (sr<170 and sr>=140):
						score=sr*4.21+30
					elif (sr<140 and sr>=100):
						score=sr+492
					elif (sr<100 and sr>=80):
						score=556
					elif (sr<80):
						score=sr*5.636
				elif (balls>=80 and balls<100):
					if (sr>=300):
						score=1000
					elif (sr<300 and sr>=250):
						score=988
					elif (sr<250 and sr>=170):
						score=sr+738
					elif (sr<170 and sr>=140):
						score=sr*4.26+30
					elif (sr<140 and sr>=100):
						score=sr+496
					elif (sr<100 and sr>=80):
						score=sr*5.7
					elif (sr<80):
						score=sr*5.636
				elif (balls>=100):	
					if (sr>=300):
						score=1000
					elif (sr<300 and sr>250):
						score=997
					elif (sr<=250 and sr>200):
						score=995
					elif (sr<=200 and sr>160):
						score=992
					elif (sr<=160 and sr>150):
						score=990
					elif (sr<=150 and sr>=130):
						score=sr*6.3
					elif (sr<130 and sr>120):
						score=sr*6.4
					elif (sr<=120 and sr>115):
						score=sr*6.62
					elif (sr<=115 and sr>110):
						score=sr*6.62
					elif (sr<=110 and sr>105):
						score=sr*6.62
					elif (sr<=105 and sr>100):
						score=sr*6.8
					elif (sr<=100 and sr>95):
						score=sr*6.9
					elif (sr<=95 and sr>=90):
						score=sr*6.99
					else:
						score=sr*7.17
					if (score<979):
						score+=20				
		if (runs>=50 and score<=550 and runs<100) :
			score+=110
		if (runs>=50 and score<=580 and runs<100) :
			score+=40
		if (runs>=50 and score<=500 and runs<100) :
			score+=160			
		if (runs>100 and score<750 and runs<155):
			score+=200
		if (runs>=155 and score<750) :
			score=1000	
		assert score<=1000
		if (batting_order>=0 and batting_order<6):
			return score
		else:
			return np.nan	
####################################################

def player_bowler_score_match(wicket, maiden, extra, economy):
	score=0
	if (np.isnan(economy)):
		return np.nan
	else:
		if (economy>=8):
			if (wicket>=7 and wicket<=10):
				score=700+(wicket*22)
			elif (wicket<7 and wicket>=5):
				score=600+(wicket*20)
			elif (wicket<5 and wicket>=3):
				score=300+(wicket*60)-(economy*2.5)
			elif (wicket==2):
				score=290+(wicket*60)-(economy*4.5)
			elif (wicket==1):
				score=270+(wicket*60)-(economy*5.8)
			elif (wicket==0):
				score=220-(economy*7)
				if (score<0):
					score=0
		elif (economy>=5 and economy<8):
			if (wicket>=7 and wicket<=10):
				score=1000
			elif (wicket<7 and wicket>=5):
				score=900
			elif (wicket<5 and wicket>=3):
				score=860
			elif (wicket==2):
				if (economy>=5 and economy<7):
					score=(1/economy)*4100
				elif (economy>7):
					score=(1/economy)*4500	
			elif (wicket==1):
				score=600-(economy*15)
			elif (wicket==0):
				score=550-(economy*15)
		elif (economy<5 and economy>=3):
			if (wicket>=7 and wicket<=10):
				score=1000
			elif (wicket<7 and wicket>=5):
				score=970
			elif (wicket<5 and wicket>=3):
				score=940
			elif (wicket==2):
				score=(1/economy)*2800
				if (score>940):
					score-=13
			elif (wicket==1):
				score=(1/economy)*2200
			elif (wicket==0):
				score=(1/economy)*1900		
		elif (economy<3 and economy>2 ):
			score=950
		elif (economy<2):
			score=1000

		if (extra>0):
			score-=extra*20
		if (maiden>0):
			if ((score+(maiden*50))<1000):
				score+=maiden*50
			else :
				score=1000
		return score
	assert score<=1000							

####################################################
# tesing codes for scores

#for reference how to get data from the data set for testing assuming we have the dictionary named data of every player
# players=df['Name'].values
# selection=int(2)
# player_selected=players[selection]
# player_test_data=data[player_selected]
# Run=player_test_data[0]
# Balls=player_test_data[1]
# SR=player_test_data[3]
# Out=player_test_data[2]
# Batting_order=player_test_data[9]
# score_test=player_batsman_score_match(Run, Balls, SR, Out,Batting_order)
# print(score_test)

# for bowler individual match score

# player data random 
Wicket=2
Maiden=0
Extra=4
Economy=7.5
score_test=player_bowler_score_match(Wicket, Maiden, Extra, Economy)
print(score_test)


players=df['Name'].values
selection=int(9)
player_selected=players[selection]
player_test_data=data[player_selected]
Wicket=player_test_data[4]
Maiden=player_test_data[6]
Extra=player_test_data[7]
Economy=player_test_data[8]
score_test=player_bowler_score_match(Wicket, Maiden, Extra, Economy)
print(score_test)




####################################################
players=df['Name'].values
# print('Select the player whose rating you want')
# for x in range(len(players)):
#  	print('Press',x,'for the rating of player',players[x])
# selection=input()
# selection=int(selection)
# player_selected=players[selection]
# print(data[player_selected])




