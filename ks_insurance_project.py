import csv

with open('insurance.csv') as insurance_data:
    insurance_reader = csv.DictReader(insurance_data)
    for row in insurance_reader:
        print(row)

#Organized by age, sex, bmi, children, smoker, region, charges
#We can analyze how each affects the cost of insurance
#There is no missing data
#Seven columns
#int, str, float types of data included