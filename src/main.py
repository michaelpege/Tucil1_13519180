import math
import time
from itertools import permutations 

def readFromFile(name):
  filename = "../test/{}.txt".format(name)
  print("\nOpening file {}".format(filename))
  with open(filename) as f:
    lines = f.readlines()
    result = ""
    i = 0
    print("\nINPUT :\n")
    for line in lines:
      lines[i] = line.strip()
      print(line.rstrip("\n"))
      i+=1
  return (lines[:-2],lines[-1:][0])

def parseFile(name, dictMap):
  filename = "../test/{}.txt".format(name)
  with open(filename) as f:
    lines = f.readlines()
    for line in lines:
      line = list(line.rstrip("\n"))
      i = 0
      for c in line:
        if(c!=" " and c!="+" and c!="-"):
          line[i] = dictMap[line[i]]
        i+=1
      target = ''.join(str(e) for e in line)
      print(target)
  print("\n")

def generateDict(text):
  res = {}
  for i in text:
    res[i] = -1
  return res

def isNoFirstZero(res, case, result):
  valid = True
  length = len(case)
  for i in range(length):
    valid = res[case[i][0]]!=0
    if(not(valid)):
      break
  return valid

def checkPossibility(res, caseReversed, resultReversed):
  found = True
  length = len(resultReversed)
  carry = 0
  for i in range(length):
    temp = carry
    for word in caseReversed:
      if(i<len(word)):
        temp+=res[word[i]] #convert char to it's integer value
    carry = int(temp/10)
    temp = temp%10
    if(temp!=res[resultReversed[i]]):
      found = False
      break
  return found

def main():
  print("Enter filename : ")
  name = input()
  (case, result) = readFromFile(name) #reading file

  totalTime = time.time()

  case[len(case)-1] = case[len(case)-1][:-1] #removing +
  caseReversed = [""] * len(case)
  resultReversed = result[::-1]
  uniqueChar = result 
  i=0
  for a in case:
    caseReversed[i] = a[::-1]
    uniqueChar+=a
    i+=1

  uniqueChar = list(set(uniqueChar))
  totalChar = len(uniqueChar)
  res = generateDict(uniqueChar)
  totalCase = len(case)
  maxlength = len(result)

  found = False
  slots = [0,1,2,3,4,5,6,7,8,9]
  target = list(permutations(slots,totalChar))
  totalTest = 0
  
  for possibility in target:
    counter = 0
    #assgning possibility to dict
    for i in uniqueChar:
      res[i] = possibility[counter]
      counter+=1
    #checking if there's any leading 0
    valid = isNoFirstZero(res, case, result)
    if(not(valid)):
      continue
    #validating possibility
    found = checkPossibility(res, caseReversed, resultReversed)
    totalTest+=1
    if(found):
      break
  
  totalTime = time.time()-totalTime
  
  if(found):
    print("\nRESULT :\n")
    parseFile(name, res)
    print("Total Execution time : {:.6f}s".format(totalTime))
    print("Total Test Executed : {} possibilities".format(totalTest))
    print("Dictionary : {}\n".format(res))
  else:
    print("\nMaaf sepertinya algoritma saya tidak sempurna, atau test casenya salah (melebihi 10 unique character), jawaban tidak ditemukan\n")

main()