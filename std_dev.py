import csv
import math

with open('data.csv', newline='') as f:
  reader = csv.reader(f)
  fileData = list(reader)

data = fileData[0]

#finds mean of dataset
def mean():
  sum = 0
  for number in data:
    sum += int(number)
  mean = sum/len(data)
  return mean

#(difference between each number and mean) squared
def squaringOfMeanDiff():
  mean_of_data = mean()
  list_of_mean_differences_squared = []
  for number in data:
    mean_diff = int(number) - mean_of_data
    list_of_mean_differences_squared.append((mean_diff*mean_diff))

  return list_of_mean_differences_squared

#mean of squared diffs
def meanOfSquaredDiffs():
  diffs_squared = squaringOfMeanDiff()
  sum = 0
  for number in diffs_squared:
    sum += int(number)
  mean = sum/len(diffs_squared)
  return mean

#square root of mean of squared diffs
def dataSTDEV():
  meanToBeSQRTd = meanOfSquaredDiffs()
  standard_dev = math.sqrt(meanToBeSQRTd)
  print("Standard Deviation of the dataset is: ", str(standard_dev)) 

dataSTDEV()