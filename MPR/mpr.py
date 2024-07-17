import math
import pandas as pd

n1 = 89
n2 = 18

half = [n1]
double = [n2]

while(min(half) > 1):
  half.append(math.floor(min(half)/2))

while(len(double) < len(half)):
  double.append(max(double) * 2)

table = pd.DataFrame(zip(half, double))

table = table.loc[table[0] %2 != 0,:]
response = sum(table.loc[:,1])

print(response)