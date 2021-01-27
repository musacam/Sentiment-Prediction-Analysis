# --------------------------- Regex text history of present illness csv for test and train data ------------------------------

import re
import csv

csv_file = input('Enter the name of your input file: ')
txt_file = input('Enter the name of your output file: ')
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()

with open(txt_file, 'r') as file:
    data = file.read().replace('\n', '')
    file.close()
    
# Take all of the string between brief hospital course and medications on admission
myt = re.findall(r"(?<=Brief Hospital Course:)(.*?)(?=Medications on Admission:)", data)

with open(txt_file, 'w') as f1:
    for line in myt:
        f1.write(line)
        f1.write('\n')