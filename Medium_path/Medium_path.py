import os 
from os.path import isfile, join
import matplotlib.pyplot as plt
import numpy as np
from simplekml import Kml, Color
import dtaidistance 

from flip_path import flip_path
from nmea_file_handle import find_GPGGA
from mean_filter import mean_average_filter
from dtw_func import dtw_func
from kml_file_creator import kml_file_creator

if __name__ == "__main__":

	dir_nmea_files='city'
	nmea_files = os.listdir(dir_nmea_files)
	
	list_lat=[]
	list_long=[]
	list_alt=[]


	for file in nmea_files:

		lat, long, alt=find_GPGGA(dir_nmea_files + '/' + file)
		
		list_lat.append(lat)
		list_long.append(long)
		list_alt.append(alt)


	list_lat_, list_long_, list_alt_ = flip_path(list_lat, list_long, list_alt)
	
	list_lat_m, list_long_m = mean_average_filter(list_lat_, list_long_, nr_points=12)

	#for i in range(len(list_lat)):
	#	filename = dir_nmea_files + '/' + dir_nmea_files + '_' + str(i) + '.kml'
	#	filename_m = dir_nmea_files + '/' + dir_nmea_files + '_m_' + str(i) + '.kml'

	#	kml_file_creator(list_lat_[i], list_long_[i], 'r',5, filename)
	#	kml_file_creator(list_lat_m[i], list_long_m[i], 'b',5, filename_m)
	
	
	


