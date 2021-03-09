def mean_average_filter(lat, long, nr_points = 5):

	mov_median_list_lat_tot=[]
	mov_median_list_long_tot=[]
	#mov_median_list_alt_tot=[]

	for j in range(len(lat)):

		mov_median_list_lat=[]
		mov_median_list_long=[]
		#mov_median_list_alt=[]

		for i in range(len(lat[j])-nr_points):

			x=lat[j]
			y=long[j]
			#z=alt[j]

			aux_i=i+nr_points

			mov_median_x=sum(x[i:aux_i])/nr_points
			mov_median_y=sum(y[i:aux_i])/nr_points
			#mov_median_z=sum(z[i:aux_i])/nr_points

			mov_median_list_lat.append(mov_median_x)
			mov_median_list_long.append(mov_median_y)
			#mov_median_list_alt.append(mov_median_z)

		mov_median_list_lat_tot.append(mov_median_list_lat)
		mov_median_list_long_tot.append(mov_median_list_long)
		#mov_median_list_alt_tot.append(mov_median_list_alt)

	return mov_median_list_lat_tot, mov_median_list_long_tot