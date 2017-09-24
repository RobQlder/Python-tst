import csv

with open('/Users/rzmcgu/temp/SaturdayGoldLotto.csv', 'rb') as infile:
	reader = csv.reader(infile)

	data = []
	for row in reader:
		data.append(row[1])
	for item in data:
		print(item)

infile.close()