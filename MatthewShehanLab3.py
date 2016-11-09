####################################################################
# CIS 117 Internet Programming
# Lab #3: "Super Secret Password"
####################################################################
# This program checks to see if a user provided password
# is super secret enough.
# a password is considered super secret if:
#   1) the password is at least 8 char long
#   2) the password has one uppercase and one lowercase char
#   3) the password has at least one digit
# else the program prompts the user to re-enter
# until the password becomes super secret enough
####################################################################

PASS_LEN = 8

def is_Password(word):
  isUpperCase = False
  isLowerCase = False
  isDigit = False

  for i in range(len(word)):

    if word[i].isupper():
      isUpperCase = True

    elif word[i].islower():
      isLowerCase = True

    elif word[i].isdigit():
      isDigit = True 

  if (isUpperCase and isLowerCase and isDigit and (len(word) >= PASS_LEN)):
    return True

  else:
    return False

def main():

  password1 = input("Please enter a new super secret password: ")
  password2 = input("Please re-enter the password: ")

  while(not is_Password(password1) or password1 != password2):

    if(password1 != password2):
      print("\nthe two passwords do not match\n")

    elif(not is_Password(password1)):
      print("\nThe password is not super secret enough\n")

    password1 = input("Please enter a new super secret password: ")
    password2 = input("Please re-enter the password: ")
    
  print("good job, that password word is super secret")

main()



##########################################################################
#------
#RUN
#------
#
#Please enter a new super secret password: passwor
#Please re-enter the password: passwor
#
#The password is not super secret enough
#
#Please enter a new super secret password: nouppercase1
#Please re-enter the password: nouppercase1
#
#The password is not super secret enough
#
#Please enter a new super secret password: NOLOWER1
#Please re-enter the password: NOLOWER1
#
#The password is not super secret enough
#
#Please enter a new super secret password: 12345678
#Please re-enter the password: 12345678
#
#The password is not super secret enough
#
#Please enter a new super secret password: notmatching
#Please re-enter the password: nope
#
#the two passwords do not match
#
#Please enter a new super secret password: yesthisWorks1
#Please re-enter the password: yesthisWorks1
#good job, that password word is super secret
##########################################################################
