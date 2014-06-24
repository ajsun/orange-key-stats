import csv

data_11 = {}
data_1 = {}
data_3 = {}

dates = []

read_file = raw_input("What file do you want to read? ")
out_file = raw_input("Where do you want to write it to? ")

def store_data(row, data):
	if row[2] not in data:
		data[row[2]] = int(row[0])
	else:
		data[row[2]] = data[row[2]] + int(row[0])

# reads data as number in party, time, date
try:
	with open(read_file ,"r") as okdata:
		reader = csv.reader(okdata, delimiter=',')
		for row in reader:
			if row[2] not in dates:
				dates.append(row[2])
			if '11:15' in row[1]:
				store_data(row, data_11)
			if '1:00' in row[1]:
				store_data(row, data_1)
			if '3:30' in row[1]:
				store_data(row, data_3)
except IOError:
	print "No such read file"
	exit()

try:
	with open(out_file, "r+") as okout:
		for date in dates:
			okout.write(date + ' ')
			try:
				okout.write(str(data_11[date]) + ' ')
			except KeyError:
				okout.write("0 ")
			try:
				okout.write(str(data_1[date]) + ' ')
			except KeyError:
				okout.write("0 ")
			try:
				okout.write(str(data_3[date]) + ' ')
			except KeyError:
				okout.write("0 ")
			okout.write('\n')
except IOError:
	print "No such out file"
	exit()



