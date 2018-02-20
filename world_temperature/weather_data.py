import pyowm
from time import sleep
import json
import pycountry
import csv


owm = pyowm.OWM('f4278087b1a0af655a1a587528ce100c')
# 6045167b5c634fed59941123e07783a6

with open('city.list.json/data') as data_file:    
    data = json.load(data_file)

# print(data[0])
# exit()
# country_data = []

# for x in range(len(data)):
# 	if len(country_data)>1:
# 		# try:
# 		for c_data in country_data:
# 			if c_data['country_name'] == data[x]['name']:
# 				c_data['city_id'].append(data[x]['id'])
				
# 			else:
# 				country_data.append({'country_code': pycountry.countries.get(alpha_2=data[x]['country']).alpha_3, \
#     		'country_name': data[x]['name'], 'city_id':[data[x]['id']]})
		
# 	else:
		
# 		country_data.append({'country_code': pycountry.countries.get(alpha_2=data[x]['country']).alpha_3, \
# 			'country_name': data[x]['name'], 'city_id':[data[x]['id']]})
      
# alpha_2 = []
# for x in range(len(data)):
# 	if data[x]['country'] not in alpha_2:
# 		alpha_2.append(data[x]['country'])
# 		try:
# 			country_data.append({'country_code': pycountry.countries.get(alpha_2=data[x]['country']).alpha_3, \
# 			'country_name': data[x]['name'], 'city_id': data[x]['id']})
# 		except KeyError:
# 			pass

# with open('country_data.txt', 'a') as file:
# 	for x in range(200,245):
# 		observation = owm.weather_at_id(country_data[x]['city_id'])
# 		w = observation.get_weather()
# 		country_data[x]['temperature'] = w.get_temperature()
# 		file.write(str(country_data[x])+";")

# file.close()

def get_temperature():
	temperature = []

	def myreadlines(f, newline):
	  buf = ""
	  while True:
	    while newline in buf:
	      pos = buf.index(newline)
	      yield buf[:pos]
	      buf = buf[pos + len(newline):]
	    chunk = f.read(4096)
	    if not chunk:
	      yield buf
	      break
	    buf += chunk

	with open('data.txt') as f:
	  for line in myreadlines(f, ";"):
	    temperature.append(line)

	temperature.remove('')
	return temperature