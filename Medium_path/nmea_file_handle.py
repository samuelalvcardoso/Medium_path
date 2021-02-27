def dm2dgrees(value):
	if value[0] > 0 and value[1] > 0:
		SGN = 1
	elif value[0] < 0 and value[1] > 0:
		SGN = -1
	elif value[0] < 0 and value[1] < 0:
		print('Error on latitude and longitude file reading')

	return SGN * (abs(value[0]) + abs(value[1])/60)





def find_GPGGA(filename):

	lat_matrix = []
	long_matrix = []
	alt_matrix = []

	file1 = open(filename, 'r')
	Lines = file1.readlines()
	count = 0

# Strips the newline character
	for line in Lines:
		count += 1
		
		if '$GPGGA' in line:
			[ flag, time, latitude, latitude_sign, longitude, longitude_sign, fix_quality, nb_satellite, hdop, altitude, *_ ] =line.split(',')
			
			##Latitude conversion##

			lat_aux=float(latitude)/100
			
			lat_deg=int(lat_aux)
			lat_min_aux=(lat_aux-lat_deg)*100
			lat=[lat_deg, lat_min_aux]
			lat = dm2dgrees(lat)

			if latitude_sign == 'S':
				lat=-lat
			
			elif lat==0:
				lat=[]

			##Longitude conversion##

			long_aux=float(longitude)/100
			long_deg=int(long_aux)
			long_min_aux=(long_aux-long_deg)*100
			long=[long_deg, long_min_aux]
			long = dm2dgrees(long)

			if longitude_sign == 'W':
				long=-long
			
			elif long==0 or lat==0:
				long=[]

			#print(lat, long, altitude)

			lat_matrix.append(lat)
			long_matrix.append(long)
			alt_matrix.append(altitude)

			


	return lat_matrix, long_matrix, alt_matrix