import matplotlib.pyplot as plt
import csv 
filename = "value.csv"
fields = [] 
rows = [] 
with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile) 
    for row in csvreader: 
    	fields.append(int(row[0]))
    	rows.append(int(row[1]))
print(fields)
print(rows)
plt.title('Graph using csv data')
plt.bar(fields,rows,color = 'green')
plt.show()