import os
import exifread

#give directory of geotagged images
imagedir = "T:\ProjectWorkspace\UAS\Missions\Active\CO_Fort_Collins_CSU_Arboretum_HoJo_Adams\\20170325_leaf_off\UAV_data\CSU_CAS_Research_Field_Centre_Ave\\20170325_Ricoh\JPG_Geotagged"
relativedir = "Geotagged_JPG"
nameofkml = "CSU_Nursery_LeafOff"
save_path = "F:\Workspace\CO_Fort_Collins_CSU_Arboretum_HoJo_Adams\Google Earth\Nursery_LeafOff"

new_file = open(save_path + '/' + nameofkml + '.kml', 'a')
new_file.close()

textforkml = '<?xml version="1.0" encoding="UTF-8"?> \n'\
'<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">\n'\
'<Document>\n\t'\
	'<name>'+nameofkml+'.kml</name>\n\t'\
	'<StyleMap id="msn_camera">\n\t\t'\
		'<Pair>\n\t\t\t'\
			'<key>normal</key>\n\t\t\t'\
			'<styleUrl>#sn_camera</styleUrl>\n\t\t'\
		'</Pair>\n\t\t'\
		'<Pair>\n\t\t\t'\
			'<key>highlight</key>\n\t\t\t'\
			'<styleUrl>#sh_camera</styleUrl>\n\t\t'\
		'</Pair>\n\t'\
	'</StyleMap>\n\t'\
	'<Style id="sn_camera">\n\t\t'\
		'<IconStyle>\n\t\t\t'\
			'<scale>0.7</scale>\n\t\t\t'\
			'<Icon>\n\t\t\t\t'\
				'<href>icon.png</href>\n\t\t\t'\
			'</Icon>\n\t\t'\
		'</IconStyle>\n\t\t'\
		'<LabelStyle>\n\t\t\t'\
			'<scale>0</scale>\n\t\t'\
		'</LabelStyle>\n\t\t'\
		'<ListStyle>\n\t\t'\
		'</ListStyle>\n\t'\
	'</Style>\n\t'\
	'<Style id="sh_camera">\n\t\t'\
		'<IconStyle>\n\t\t\t'\
			'<scale>0.816667</scale>\n\t\t\t'\
			'<Icon>\n\t\t\t\t'\
				'<href>icon.png</href>\n\t\t\t'\
			'</Icon>\n\t\t'\
		'</IconStyle>\n\t\t'\
		'<LabelStyle>\n\t\t\t'\
			'<scale>0</scale>\n\t\t'\
		'</LabelStyle>\n\t\t'\
		'<ListStyle>\n\t\t'\
		'</ListStyle>\n\t'\
	'</Style>\n\t'

for filename in os.listdir(imagedir):
    name = filename
    os.chdir(imagedir)
    f = open(filename, 'rb')
    tags = exifread.process_file(f, details=False)
    if not 'GPS GPSLatitude' in tags:
        lat_cent = 'x'
        print filename + ' has no Latitude information!'
    else:
        lat_cent1 = str(tags['GPS GPSLatitude'])
        lat_cent2 = lat_cent1.split('[')
        lat_cent3 = lat_cent2[1]
        lat_cent4 = lat_cent3.split(']')
        lat_cent5 = lat_cent4[0]
        lat_cent6 = lat_cent5.split(',')
        lat_cent_deg = float(lat_cent6[0])
        lat_cent_min = float(lat_cent6[1])
        lat_cent_sec1 = lat_cent6[2]
        lat_cent_sec2 = lat_cent_sec1.split('/')
        lat_cent_sec = float(lat_cent_sec2[0])/ float(lat_cent_sec2[1])
        lat_sign = str(tags['GPS GPSLatitudeRef'])
        if lat_sign == 'S':
            lat_cent = float(-1) * (lat_cent_deg + ((lat_cent_min + (lat_cent_sec/float(60)))/float(60)))
        elif lat_sign == 'N':
            lat_cent = lat_cent_deg + ((lat_cent_min + (lat_cent_sec/float(60)))/float(60))

        # retrieving longitude info from EXIF,converting to dec degrees
    if not 'GPS GPSLongitude' in tags:
        long_cent = 'x'
        print filename + ' has no Longitude information!'
    else:
        long_cent1 = str(tags['GPS GPSLongitude'])
        long_cent2 = long_cent1.split('[')
        long_cent3 = long_cent2[1]
        long_cent4 = long_cent3.split(']')
        long_cent5 = long_cent4[0]
        long_cent6 = long_cent5.split(',')
        long_cent_deg = float(long_cent6[0])
        long_cent_min = float(long_cent6[1])
        long_cent_sec1 = long_cent6[2]
        long_cent_sec2 = long_cent_sec1.split('/')
        long_cent_sec = float(long_cent_sec2[0])/ float(long_cent_sec2[1])
        long_sign = str(tags['GPS GPSLongitudeRef'])
        if long_sign == 'W':
            long_cent = float(-1) * (long_cent_deg + ((long_cent_min + (long_cent_sec/float(60)))/float(60)))
        elif long_sign == 'E' :
            long_cent = long_cent_deg + ((long_cent_min + (long_cent_sec/float(60)))/float(60))
    if not 'GPS GPSAltitude' in tags:
        zvalue = 'x'
        print filename + ' has no altitude information'
    else:
        z1 = str(tags['GPS GPSAltitude']).split('/')
        lenz = len(z1)
        if lenz == 2:
            zvalue = float(z1[0])/float(z1[1])
        else:
            zvalue = float(z1[0])
    
    relativedir2 = relativedir + '/' + filename
    if long_cent == 'x' or lat_cent == 'x' or zvalue == 'x':
        texttoadd = ''
    else:
        texttoadd = '<Placemark>\n\t\t'\
    		'<name>'+ name +'</name>\n\t\t'\
          '<visibility>0</visibility>\n\t\t'\
    		'<description><![CDATA[<img style="max-width:500px;" src="'+relativedir2 +'">]]></description>\n\t\t'\
    		'<LookAt>\n\t\t\t'\
    			'<longitude>'+ str(long_cent) + '</longitude>\n\t\t\t'\
    			'<latitude>'+str(lat_cent)+'</latitude>\n\t\t\t'\
    			'<altitude>0</altitude>\n\t\t\t'\
    			'<heading>0.0003068323459074509</heading>\n\t\t\t'\
    			'<tilt>0</tilt>\n\t\t\t'\
    			'<range>3750.893526546607</range>\n\t\t\t'\
    			'<gx:altitudeMode>relativeToSeaFloor</gx:altitudeMode>\n\t\t'\
    		'</LookAt>\n\t\t'\
    		'<styleUrl>#msn_camera</styleUrl>\n\t\t'\
    		'<Point>\n\t\t\t'\
    			'<gx:drawOrder>1</gx:drawOrder>\n\t\t\t'\
    			'<coordinates>'+str(long_cent)+','+str(lat_cent)+','+str(zvalue)+'</coordinates>\n\t\t'\
    		'</Point>\n\t'\
    	'</Placemark>\n\t'
        
    textforkml = textforkml + texttoadd

endtext = '</Document>\n'\
'</kml>'

finaltextforkml = textforkml + endtext

new_file = open(save_path + '/' + nameofkml + '.kml', 'w')
new_file.write(finaltextforkml)
new_file.close()
