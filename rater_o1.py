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
# tesing codes for scores
# for batsman individual match score

# test 1 data random player out

Run=5
Balls=13
SR=(Run/Balls)*100
score_test=player_batsman_score_match(Run, Balls, SR, 1,2)
print(score_test)

# test 2 data random player not out

Run=50
Balls=70
SR=(Run/Balls)*100
score_test=player_batsman_score_match(Run, Balls, SR, 0,4)
print(score_test)

# test 3 data from data set player out

players=df['Name'].values
selection=int(2)
player_selected=players[selection]
player_test_data=data[player_selected]
Run=player_test_data[0]
Balls=player_test_data[1]
SR=player_test_data[3]
Out=player_test_data[2]
Batting_order=player_test_data[9]
score_test=player_batsman_score_match(Run, Balls, SR, Out,Batting_order)
print(score_test)
# test 4 data from data set player not out

players=df['Name'].values
selection=int(9)
player_selected=players[selection]
player_test_data=data[player_selected]
Run=player_test_data[0]
Balls=player_test_data[1]
SR=player_test_data[3]
Out=player_test_data[2]
Batting_order=player_test_data[9]
score_test=player_batsman_score_match(Run, Balls, SR, Out,Batting_order)
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




