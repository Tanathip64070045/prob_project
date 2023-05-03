import csv
with open('dataset.csv', 'r') as file:
    # create a reader object
    reader = csv.reader(file)
    # iterate over each row in the CSV file
    for row in reader:
        # do something with the data
        print(row)