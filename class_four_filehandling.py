#READ EACH ROW ROW AND PRINT IT
'''import csv
with open('Book1.csv','r') as f:
    f = csv.reader(f,delimiter=',')
    for row in f:
        if len(row)==2:
            print(row[0] + ',' + row[1])

#WRITE APPEND TWO MORE COUNTRIES AND CAPITALS TO FILE
country = ['Tripura', 'West Bengal']
capital = ['Agartala', 'Kolkata']

with open('Book1.csv', 'a', newline='') as f:
    w = csv.writer(f,delimiter=',')
    for i in range(len(country)):
        w.writerow([country[i], capital[i]])'''


import csv
#Define data
header = ['Name', 'Age', 'City']
data = [
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angles'],
    ['Charlie', 35, 'Chicago']
]

#specify the path to your csv file
file_path = 'people.csv'

#write data to csv file

with open(file_path,'w', newline='') as file:
    writer = csv.writer(file)

#write the header
    writer.writerow(header)

#write the data
    writer.writerows(data)

print(f"CSV file'{file_path}' has been created")

import csv
with open('people.csv','r') as f:
    f = csv.reader(f,delimiter=',')
    for row in f:
        if len(row)==3:
            print(row[0] + ',' + row[1]+ ',' + row[2])


