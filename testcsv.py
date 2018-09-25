import csv

# file = open("flights.csv")
# reader = csv.reader(file, delimiter=",")
# for origin, dest, durat in reader:
#   print(f"From {origin} to {dest} in {durat} minutes.")
  

file = open("flights.csv", "r")
for line in file:
  print(line.split(","))

file = open("flights.csv", "r")
text = file.read()
print(text)