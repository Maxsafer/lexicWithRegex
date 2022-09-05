import re
from os import listdir

def lexLuthor(inputText):
  # iteramos sobre input
  for y,string in enumerate(inputText):
    subStrings = string.split()
    for x,subStr in enumerate(subStrings):
      if re.match("[0-9]+(\.[0-9]+(E(\+|\-)?[0-9]+)|\.[0-9]+|E(\+|\-)?[0-9]+)", subStr):
        print(f'Token: REAL, Lexema: {subStr} on line {y}')
      
      elif re.match("\<|\>|\==", subStr):
        print(f'Token: OPREL, Lexema: {subStr} on line {y}')
      
      elif re.match("\=", subStr):
        print(f'Token: ASIG, Lexema: {subStr} on line {y}')
      
      elif re.match("^([a-zA-Z$][a-zA-Z\\d$]*)$", subStr):
        print(f'Token: ID, Lexema: {subStr} on line {y}')
  
      elif re.match("[0-9]+", subStr):
        print(f'Token: ENT, Lexema: {subStr} on line {y}')
      
      elif re.match("[\+ \- \* \/ \% \** \++ \--]", subStr):
        print(f'Token: OPAR, Lexema: {subStr} on line {y}')
  
      else:
        print(f'Token: ERR, Lexema: {subStr} not recognized on line {y}')
      
      if x != len(subStrings)-1: print(f'Token: SPACE, Lexema:  on line {y}')
    print('')

def inputText():
  inputStrings = []
  files = []
  counter = 0
  for file in listdir('./'):
    if file.endswith(".txt"):
      counter += 1
      print(f'{counter}. {file}')
      files.append(file)
  chosen = int(input())-1
  f = open(f'{files[chosen]}', "r")
  for row in f:
    inputStrings.append(row.replace("\n", ""))
  return inputStrings
  
if __name__ == '__main__':
  reconocidos = [" ", "id", "ent", "real", "<", "<=", ">", ">=", "==", "=", "+", "-", "*", "/", "%", "**", "++", "--"]
  inputText = inputText()
  lexLuthor(inputText)