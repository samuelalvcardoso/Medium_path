from flip_path import distance_lat_long

def dtw_func(lat_1, long_1, lat_2, long_2):

    i=0
    j=0
    a=0

    medium_path_list_1=[]
    medium_path_list_2=[]
    final_path_lat_list=[]
    final_path_long_list=[]

    while i<(len(lat_1)-1) and j<(len(lat_2)-1):
        
        right = distance_lat_long(lat_1[i], long_1[i], lat_2[j+1], long_2[j+1])
        diagonal = distance_lat_long(lat_1[i+1], long_1[i+1], lat_2[j+1], long_2[j+1])
        down = distance_lat_long(lat_1[i+1], long_1[i+1], lat_2[j], long_2[j])

       

        if right < diagonal and right < down:

            medium_path_1=i
            medium_path_2=j+1
            j+=1
            a+=1
            medium_path_list_1.append(medium_path_1)
            medium_path_list_2.append(medium_path_2)
           

        elif  diagonal < right and diagonal < down:

            medium_path_1=i+1
            medium_path_2=j+1
            i+=1
            j+=1
            a+=1
            medium_path_list_1.append(medium_path_1)
            medium_path_list_2.append(medium_path_2)
           
        elif down < diagonal and down < right:

            medium_path_1=i+1
            medium_path_2=j
            i+=1
            a+=1
            medium_path_list_1.append(medium_path_1)
            medium_path_list_2.append(medium_path_2)
          

        else:
            medium_path_1=i+1
            medium_path_2=j+1
            i+=1
            j+=1
            a+=1
            medium_path_list_1.append(medium_path_1)
            medium_path_list_2.append(medium_path_2)
            

        lat_med = (lat_1[medium_path_1]+lat_2[medium_path_2])/2
        long_med = (long_1[medium_path_1]+long_2[medium_path_2])/2


        final_path_lat_list.append(lat_med)
        final_path_long_list.append(long_med)

    
    return final_path_lat_list, final_path_long_list