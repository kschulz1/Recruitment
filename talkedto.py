from __future__ import division
import csv
import os.path

#Ultimately want to run this from bash script and first delete all created Group_.txt files

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

	
	with open('members.csv', 'rU') as groupnums:
		reader2 = csv.DictReader(groupnums)
		
		for row in reader2:
			if row['Name'] in sisters:
				group = row['Group']
				y = group.replace(" ", "_")
				group_filename = y + ".txt"
				if os.path.exists(group_filename):
					with open(group_filename, "a") as myfile:
						myfile.write("ADPi: " + row['Name'] + " talked to: " + "\n")
				else:
					temp_file = open(group_filename, "w+")
					temp_file.write("ADPi: " + row['Name'] + " talked to: " + "\n")
			else:
				print(row['Name'])
			
		for recruiter in sisters:
			x = recruiter.replace(" ", "_")
			filename = x + ".txt"
			temp_file = open(filename, "w+")
			temp_file.write("ADPi: " + recruiter + " talked to: \n")
			for pnms in sisters[recruiter]:
				temp_file.write(pnms + "\n")
