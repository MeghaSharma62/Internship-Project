
import json
import csv
 
 
# Opening JSON file and loading the data
# into the variable data
with open('a.json') as json_file:
    data = json.load(json_file)
 
employee_data = data['Titles']

# now we will open a file for writing
data_file = open('so.csv', 'w')
 
# create the csv writer object
csv_writer = csv.writer(data_file)