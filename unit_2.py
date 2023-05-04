import csv

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
with open('dataset.csv', 'r') as file:
    # create a reader object
    reader = csv.reader(file)
    # iterate over each row in the CSV file
    for row in reader:
        # do something with the data
        if isfloat(row[4]):
            print(row[4])


