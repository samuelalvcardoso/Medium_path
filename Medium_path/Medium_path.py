import os 
from os.path import isfile, join
 
import matplotlib.pyplot as plt
import numpy as np
from simplekml import Kml, Color
import dtaidistance 
import shutil

from flip_path import flip_path
from nmea_file_handle import find_GPGGA
from mean_filter import mean_average_filter
from dtw_func import dtw_func
from kml_file_creator import kml_file_creator

if __name__ == "__main__":

	dir_nmea_files='nmea_origin_city'
	nmea_files = os.listdir(dir_nmea_files)
	str_folder_results='kml_files_city'

	try:
		#shutil.rmtree(str_folder_results)
		 os.mkdir(str_folder_results)
	except OSError:
		print("Creation of the directory",str_folder_results,"already satisfied")
		pass;

	list_lat=[]
	list_long=[]
	list_alt=[]

	ai=0
	for file in nmea_files:

		lat, long, alt=find_GPGGA(dir_nmea_files + '/' + file)
		
		list_lat.append(lat)
		list_long.append(long)
		list_alt.append(alt)

		path_name='ini_'+str(ai)
		string_kml= str_folder_results +'/ini_'+str(ai)+'.kml'

		kml_file_creator(lat, long, 'y',2, path_name, string_kml)
		#plt.plot(lat, long, 'b')
		ai+=1

	list_lat_, list_long_, list_alt_ = flip_path(list_lat, list_long, list_alt)
	
	list_lat_m, list_long_m = mean_average_filter(list_lat_, list_long_, nr_points=12)

	list_lat_med_1=[]
	list_long_med_1=[]
	list_lat_med_2=[]
	list_long_med_2=[]
	list_lat_med_f=[]
	list_long_med_f=[]

	a=0
	for i in range(0,len(list_lat)-1,2):
		medium_lat_1,medium_long_1 = dtw_func(list_lat_m[i], list_long_m[i], list_lat_m[i+1], list_long_m[i+1])
		list_lat_med_1.append(medium_lat_1)
		list_long_med_1.append(medium_long_1)

		path_name='int1_'+str(a)
		string_kml= str_folder_results +'/int1_'+str(a)+'.kml'
		
		kml_file_creator(medium_lat_1,medium_long_1, 'b',2, path_name, string_kml)
		a+=1

	
	b=0
	for j in range(0,len(list_lat_med_1)-1,2):
		medium_lat_2, medium_long_2 = dtw_func(list_lat_med_1[j], list_long_med_1[j], list_lat_med_1[j+1], list_long_med_1[j+1])
		list_lat_med_2.append(medium_lat_2)
		list_long_med_2.append(medium_long_2)
		
		path_name='int2_'+str(b)
		string_kml= str_folder_results +'/int2_'+str(b)+'.kml'
		
		kml_file_creator(medium_lat_2, medium_long_2, 'g',2, path_name, string_kml)
		b=+1

	list_lat_med_f, list_long_med_f = dtw_func(list_lat_med_2[0], list_long_med_2[0], list_lat_med_2[1], list_long_med_2[1])

	#plt.plot(list_lat_med_f, list_long_med_f, 'r')
	#plt.show()

	kml_file_creator(list_lat_med_f, list_long_med_f, 'r',6, 'final',  str_folder_results +'/final.kml')
