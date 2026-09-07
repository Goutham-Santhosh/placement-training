'''
Joseph is learning digital logic subject which will be for his next semester. He usually tries to solve unit
assignment problems before the lecture. Today he got one tricky question. The problem statement is “A
positive integer has been given as an input. Convert decimal value to binary representation. Toggle all bits of
it after the most significant bit including the most significant bit. Print the positive integer value after toggling
all bits”.
Constraints :
1<=N<=100
Example 1:
Input :
10 
Output :
5
'''




def convertToInteger(n):
  weight = 1
  n = n[::-1]
  sumVal = 0
  for val in n:
    sumVal += int(val)*weight
    weight *= 2
  return sumVal

def toggleBinary(n):
  newBinary = []
  for val in n:
    if val == "1":
      newBinary.append("0")
    else:
      newBinary.append("1")
  return "".join(newBinary)

def convertToBinary(n):
  return bin(int(n))[2:]

number = input()
binary = convertToBinary(number)
toggle = toggleBinary(binary)
integer = convertToInteger(toggle)
print(integer)