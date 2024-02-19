import csv
with open(r"C:\pf\Python\Python\csvfiles\population_by_zip_2000.csv","r") as csv_file:
    reader=csv.DictReader(csv_file,delimiter=",")
    print(reader.fieldnames)
    info=[row for row in reader]
    print(info[:10])