'''
Every decimal number can be changed into its binary form. Suppose your computer has it’s own CoronaVirus, that eats binary digits from the right side of a number. Suppose a virus has 6 spikes, it will eat up 6 LSB binary digits in your numbers.
You will have a bunch of numbers, and your machine will have a virus with n spikes, you have to calculate what will be the final situation of the final numbers.
Input Format:
First line, a single Integer N
Second line N space separated integers of the bunch of values as array V
Third line a single integer n, the number of spikes in Corona for Computer
Output Format:
Single N space separated integers denoting the final situation with the array v.
Sample Input:
5
1 2 3 4 5
2
Output:
0 0 0 1 1
'''




def solution():
  finalOutput = []
  for number in numbers:
    binaryValue = bin(number)[2:]
    if len(binaryValue) <= spikes:
      finalOutput.append("0")
    else:
      finalOutput.append(binaryValue[:(len(binaryValue)-spikes)])
  return finalOutput


numberCount = int(input())
numbers = list(map(int, input().split()))
spikes = int(input())

output = solution()
print(" ".join(output))