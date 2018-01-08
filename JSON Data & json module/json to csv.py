employee_data = '{"employee_details":[{"employee_name": "James", "email": "james@gmail.com", "job_profile": "Sr. Developer"},{"employee_name": "Smith", "email": "Smith@gmail.com", "job_profile": "Project Lead"},.....]}'

import json
import csv

f = open('new_states.json')
data = json.load(f)
f.close()

f=csv.writer(open('test.csv','wb+'))

for item in data:
    f.writerow([item['pk'], item['model']] + item['fields'].values())


# employee_parsed = json.loads(employee_data)
# emp_data = employee_parsed['employee_details']
#
# # open a file for writing
# employ_data = open('EmployData.csv', 'w')
#
# # create the csv writer object
# csvwriter = csv.writer(employ_data)
#
# count = 0
# for emp in emp_data:
#       if count == 0:
#              header = emp.keys()
#              csvwriter.writerow(header)
#              count += 1
#       csvwriter.writerow(emp.values())

#employ_data.close()

# inputFile = open('new_states.json', 'r') #open json file
# outputFile = open('states.csv', 'w') #load csv file
# data = json.load(inputFile) #load json content
#
# inputFile.close() #close the input file
#
# output = csv.writer(outputFile) #create a csv.write
# output.writerow(data[0].keys())  # header row
#
# for row in data:
#    output.writerow(row.values()) #values row
#

