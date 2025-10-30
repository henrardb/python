import math
import random
import time

luoshu = [[4,9,2],[3,5,7],[8,1,6]]
test = [[1,2,3],[4,5,6],[7,8,9]]

def fillSquare(square, iValue, jValue, fill):
  while(sum(math.isnan(i) for line in square for i in line) > fill):
    #print("i: ", iValue)
    #print("j: ",jValue)
    #print(displaySquare(square))
    #time.sleep(0.5)
    #print(sum(math.isnan(i) for line in square for i in line))
    possibleDirections = []
    if(iValue < (n - 1) and jValue < (n - 1)):
      possibleDirections.append("downRight")
    if(iValue < (n - 1) and jValue > 0):
      possibleDirections.append("downLeft")
    if(iValue > 0 and jValue < (n - 1)):
      possibleDirections.append("upRight")
    if(iValue > 0 and jValue > 0):
      possibleDirections.append("upLeft")

    whereToGo = random.choice(possibleDirections)

    if(whereToGo == 'downRight' and (iValue + jValue) == (n - 2)):
      newiValue = iValue + 1
      newjValue = jValue + 1
      square[newiValue][newjValue] = rule3(square[iValue][jValue], n, False)
      # print('downRight = n-2')

    if(whereToGo == 'downRight' and (iValue + jValue) != (n - 2)):
      newiValue = iValue + 1
      newjValue = jValue + 1
      square[newiValue][newjValue] = rule2(square[iValue][jValue], n, False)

      # print('downRight n != n-2')

    if(whereToGo == 'upLeft' and (iValue + jValue) == (n)):
      newiValue = iValue - 1
      newjValue = jValue - 1
      square[newiValue][newjValue] = rule3(square[iValue][jValue], n, True)
      # print('upleft =n')

    if(whereToGo == 'upLeft' and (iValue + jValue) != (n)):
      newiValue = iValue - 1
      newjValue = jValue - 1
      square[newiValue][newjValue] = rule2(square[iValue][jValue], n, True)
      # print('upleft n !=')

    if(whereToGo == 'downLeft'):
      newiValue = iValue + 1
      newjValue = jValue - 1
      square[newiValue][newjValue] = rule1(square[iValue][jValue], n, False)
      # print('downleft')

    if(whereToGo == 'upRight'):
      newiValue = iValue - 1
      newjValue = jValue + 1
      square[newiValue][newjValue] = rule1(square[iValue][jValue], n, True)
      # print('upright')

    iValue = newiValue
    jValue = newjValue
  return square
  


## Rules
def rule1(x, n, highRight):
  return((x + ((-1)**highRight) * n) % n**2)

def rule2(x, n, highLeft):
  return((x + ((-1)**highLeft)) % n**2)

def rule3(x, n, highLeft):
  return((x + ((-1)**highLeft * ( - n + 1))) % n**2)

def verif(square):
  total = []

  lineSum = [sum(square[i]) for i in range(0,len(square))]
  total.append(lineSum)

  colSum = [sum(col[i] for col in square) for i in range(0,len(square))]
  total.append(colSum)

  diag = sum((square[i][i]) for i in range(0,len(square)))
  total.append([diag])

  anti = sum(square[i][len(square) - 1 - i] for i in range(0,len(square)))
  total.append([anti])

  suite = [j for i in total for j in i]
  return len(set(suite)) == 1

def displaySquare(square):
  values = ['['+str(x)+']' for x in range(0, len(square))]
  line_format = "{:>6}" * (len(values) + 1)
  print(line_format.format("", *values))
  for value, line, in zip(values, square):
    print(line_format.format(value, *line))

## Fill empty array
n = 5
square = [[float('nan') for i in range(0,n)] for j in range(0,n)]

## Fill center cases
centerI = math.floor(n/2)
centerJ = math.floor(n/2)

square[centerI][centerJ] = (n**2 + 1) / 2
square[centerI - 1][centerJ] = n**2
square[centerI][centerJ + 1] = n**2 + 1 - n
square[centerI + 1][centerJ] = 1
square[centerI][centerJ - 1] = n

iValue = centerI
jValue = centerJ

finalSquare = fillSquare(square, iValue, jValue, (n**2)/2 - 4)
#time.sleep(5)
iValue = math.floor(n/2) + 1
jValue = math.floor(n/2)
finalSquare = fillSquare(finalSquare, iValue, jValue, 0)
finalSquare = [[n**2 if x == 0 else x for x in line] for line in finalSquare]

print(displaySquare(finalSquare))
print(verif(finalSquare))
#print(verif(luoshu))
#print(displaySquare(finalSquare))
#print(rule3(43,7,True))
