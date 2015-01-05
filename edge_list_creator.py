import csv

def pairing(source):
	result = []
	for item1 in range(len(source)):
		for item2 in range(item1+1, len(source)):
			result.append([source[item1], source[item2],edgeType])
	return result

filename = raw_input('file name? ')

edgeType = raw_input("edge type? Directed or Undirected? ")

f = open (filename, 'rb')

csv_f = csv.reader(f, quoting=csv.QUOTE_ALL)

temp_list = []
for row in csv_f:
	row = [var for var in row if var]
	temp_list.append(pairing(row))

final_list = []
for itemlist in temp_list:
	for item in itemlist:
		final_list.append(item)

new_filename = "done_" + filename

with open(new_filename, 'wb') as csvfile:
    rowwriter = csv.writer(csvfile, delimiter=',', quotechar=' ')
    rowwriter.writerow(['Source,Target,Type']) 
    for row in final_list:
    	rowwriter.writerow(row)
