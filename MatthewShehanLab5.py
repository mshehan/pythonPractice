####################################################################
##CIS 117 Internet Programming
##Lab #5: "File Identity"
####################################################################
##This program takes input from the user.
##The user puts in a file path and the program
##reads through the file until it reaches EOF
##it checks to see on each line matches required
##identifier for a proper line
##it then outputs the line on which the proper line
##appears
####################################################################

def isIdentifier(line):
  index = 0
  line = line.strip()
  flag = False

  for index in range(len(line)):

    if(line[index].isalpha()):
      index += 1
      
    elif(line[index].isdigit()):
      index += 1
      
    elif (line[index] == "_"):
      index += 1

    else:
      return flag

  return not flag

def openFile(text_file):
  outfile = open(str(text_file),"r")
  return outfile

def readFile(outfile):
  line = outfile.readline()
  return line

def locationFind(text_file, word):
  count = 1
  wordloc = []
  outfile = open(text_file, "r")
  line = outfile.readline()
  while line != "":
    line.strip()
    if(isIdentifier(line) and word == line):
      wordloc.append(count)
    line = outfile.readline()
    count += 1
  return wordloc
##############################################
#this function was used for testing
def printFile(text_file):
  outfile = open(str(text_file),"r")
  line = outfile.readline()
  while line != "":
    line.strip()
    if isIdentifier(line):
      print(line, end = "")
    line = outfile.readline()
###############################################


def main():


  sherlock = dict()
  fileName = input("Please write the file path for the file you want to\
 access: ")
  fileName = str(fileName)
                   
  outfile = openFile(fileName)
  line = readFile(outfile)
  while line != "":
    if isIdentifier(line):
      sherlock[line.strip()] = locationFind(fileName,line)
    line = readFile(outfile)
  for (key,value) in sorted(sherlock.items()):
    print("%s: %s"% (key,value))
  

 
main()


