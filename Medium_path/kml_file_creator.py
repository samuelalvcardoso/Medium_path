def kml_file_creator(list_lat, list_long, color,line_width, filename):

	if color=='r':
		code_color = '941400FF'

	elif color=='bk':
		code_color = '94000000'

	elif color=='b':
		code_color = '94F00014'

	elif color=='g':
		code_color = '9414F000'

	elif color=='gr':
		code_color = '94646464'

	f = open(filename, "w")
	f.write('<?xml version="1.0" encoding="utf-8"?>\n')
	f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
	f.write("\t<Document>\n")
	f.write("\t\t<name>cidade1</name>\n")
	f.write("\t\t<Placemark>\n")
	f.write('\t\t\t<Snippet maxLines="0"> </Snippet>\n')
	f.write("\t\t\t<description> </description>\n")
	f.write("\t\t\t<name>Line 1</name>\n")
	f.write("\t\t\t<Style>\n")
	f.write("\t\t\t\t<IconStyle>\n")
	f.write("\t\t\t\t\t<color>"+code_color+"</color>\n")
	f.write("\t\t\t\t</IconStyle>\n")
	f.write("\t\t\t\t<LineStyle>\n")
	f.write("\t\t\t\t\t<color>"+code_color+"</color>\n")
	f.write("\t\t\t\t\t<width>"+str(line_width)+"</width>\n")
	f.write("\t\t\t\t</LineStyle>\n")
	f.write("\t\t\t</Style>\n")
	f.write("\t\t\t<LineString>\n")
	f.write('\t\t\t\t<altitudeMode>clampToGround</altitudeMode>\n\n')
	f.write('<coordinates> ')

	for i in range(len(list_lat)):
		f.write(str(list_long[i])+','+str(list_lat[i])+',0 ')

	f.write('</coordinates> ')
	f.write("\t\t\t</LineString>\n")
	f.write("\t\t</Placemark>\n")
	f.write("\t</Document>\n")
	f.write("</kml>\n")
	
	f.close()

