import math
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt



def distance_lat_long(lat1, long1, lat2, long2):

	EARTH_R=6371000

	phi1 = lat1*math.pi/180
	phi2 = lat2*math.pi/180

	delta_phi=(lat2-lat1)*math.pi/180
	delta_lambda=(long2-long1)*math.pi/180

	cte_a = math.sin(delta_phi/2)*math.sin(delta_phi/2)+math.cos(phi1)*math.cos(phi2)*math.sin(delta_lambda/2)*math.sin(delta_lambda/2)
	cte_c = 2*math.atan2(math.sqrt(cte_a), math.sqrt(1-cte_a))
	distance = EARTH_R * cte_c

	return distance


def flip_path(list_lat, list_long, list_alt):
	
	distance_tot=[]

	for i in range(len(list_lat)):

		distance_mat = []

		lat1=list_lat[i][0]
		long1=list_long[i][0]

		string='Path ' + str(i)

		for j in range(len(list_lat)):

			lat2=list_lat[j][0]
			long2=list_long[j][0]

			distance=distance_lat_long(lat1, long1, lat2, long2)
			distance_mat.append(distance)

		distance_tot.append(distance_mat)
		df=pd.DataFrame(distance_tot)

	corrMatrix = df.corr()
	corr_Matrix_list=corrMatrix.values.tolist()

	list_lat_=list_lat
	list_long_=list_long
	list_alt_=list_alt

	#print(list_lat, list_long)

	nr_path=0

	for i in range(len(corr_Matrix_list)):

		flag_invert=countNegative(corr_Matrix_list[:][i])

		if flag_invert==1:
			list_lat_[i]=list_lat[i][::-1]
			list_long_[i]=list_long[i][::-1]
			list_alt_[i]=list_alt[i][::-1]
		else:
			pass


	return list_lat_, list_long_, list_alt_



def countNegative(Matrix): 

	count_negative = 0
	count_positive = 0

	for a in range(len(Matrix)): 
		 
			if Matrix[a] < 0: 
				count_negative += 1
  
			else: 
				count_positive += 1
     
	if count_negative>count_positive:
		flag_invert=1
	else:
		flag_invert=0

	return flag_invert

		
	