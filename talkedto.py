from __future__ import division
import csv

with open('notes.csv', 'rU') as csvfile:
	reader = csv.DictReader(csvfile)
	
	sisters = dict()
	for row in reader:
		adpi = row['Author']
		if adpi in sisters:
			if row['PNM Name'] in sisters[adpi]:
				continue
			else:
				sisters[adpi].append(row['PNM Name'])
			#add PNM name to her list
		else:
			sisters.setdefault(adpi, [])
			sisters[adpi].append(row['PNM Name'])

	for recruiter in sisters:
		x = recruiter.replace(" ", "_")
		filename = x + ".txt"
		temp_file = open(filename, "w+")
		temp_file.write("ADPi: " + recruiter + " talked to: \n")
		for pnms in sisters[recruiter]:
			temp_file.write(pnms + "\n")
