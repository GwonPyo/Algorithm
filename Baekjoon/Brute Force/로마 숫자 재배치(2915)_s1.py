# type 1
import sys
input = sys.stdin.readline

def checkIndex(string: str):
    index = 0
    for char in string:
        if char == "I":
            index += 1
        elif char == "X":
            index += 3
        elif char == "V":
            index += 16
        elif char == "L":
            index += 32
        elif char == "C":
            index += 64
    return index

oneUnitsRoma:list = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
twoUnitsRoma:list = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]

results: list = [0 for _ in range(128)]

for i in range(9):
    string = oneUnitsRoma[i]
    
    index = checkIndex(string)
    if results[index] == 0:
        results[index] = string
        
for i in range(9):
    index = checkIndex(twoUnitsRoma[i])
    if results[index] == 0:
        results[index] = twoUnitsRoma[i]
        
    for j in range(9):
        string = twoUnitsRoma[i]+oneUnitsRoma[j]
        
        index = checkIndex(string)
        if results[index] == 0:
            results[index] = string 

inputString:str = input().rstrip()
index = checkIndex(inputString)
print(results[index])

# type2
import sys
input = sys.stdin.readline

oneUnitsRoma:list = ['', "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
twoUnitsRoma:list = ['', "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]

inputString:str = sorted(input().rstrip())

for i in range(1, 100):
    string = twoUnitsRoma[i//10]+oneUnitsRoma[i%10]
    if inputString==sorted(string): 
        print(string)
        break