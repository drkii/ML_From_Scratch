import csv
address = open("address.csv")
reader = csv.reader(address)
for row in reader:
    print(row)

for row in reader:
	print(" ".join(row))
