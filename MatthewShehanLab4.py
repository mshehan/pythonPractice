####################################################################
##CIS 117 Internet Programming
##Lab #3: "JetStream Merger"
####################################################################
##This program takes input from the user.
##The user has a choice to add to either the Jet list
##or the Stream list.
##the user can also select to display each respective list
##and the merged list called JetStream
##Finally, the user may also choose to exit the program
####################################################################
##printList(lst)
##precondition: none
##postcondition: all items in list are printed to the screen
##
##isSorted(lst)
##precondition: none
##postcondition: returns true if all elements are sorted by increasing order
##               else returns false
##
##sortList(lst)
##precondition: none
##postcondition: sorts a list by increasing order
##
##jetStream(jet_list,stream_list)
##precondition: jet_list and stream_list must be ordered lists
##postcondition: returns a combination of jet_list and stream_list
##               this list is ordered
##
##quitProgram()
##preconditon: none
##postcondition: quits the program
##
##printMenu()
##preconditon: none
##postcondition: post a menu for the user to the screen
####################################################################

import sys

def printList(lst):
  print("[ ", end = "")
  for item in lst:
    print(item, end = " ")
  print("]")

def isSorted(lst):
  if(len(lst) == 0 or len(lst) == 1): 
    return True
  
  else:
    counter = 0
    end = -1
    i = 0
    for i in range(len(lst)):
      if lst[i] <= lst[end]:
        counter += 1
    return counter == len(lst)
    
def sortList(lst):
  start = 0
  end = -1

  if(isSorted(lst)):
    return lst

  while(start < len(lst) and lst[start] < lst[end]):
     start += 1

  if(not isSorted(lst)):
    temp = lst[end]
    lst.pop(end)
    lst.insert(start,temp)
    return lst

def jetStream(jet_list,stream_list):

  customer_list = list(jet_list)

  for item in stream_list:
    customer_list.append(item)
    sortList(customer_list)
  
  return customer_list

def quitProgram():
  sys.exit(0)

def printMenu():
  
  print("\n\n----------------------------------------\
\nPlease choose from the following options: \n\
1: add a value to the list called jet\n\
2: add a value to the list called stream\n\
3: print jet, stream, and the merged jetstream\n\
4: quit the program\n\
----------------------------------------\n\n")


def main():
  printMenu()
  choice = int(input("please input your selection: "))

  jet_list = []
  stream_list = []
  
  
  while choice < 100:

    if choice == 1:
      value = int(input("\nplease input the value you want to add to jet: "))
      jet_list.append(value)
      sortList(jet_list)

      print("here is the new jet list:", end = " ")
      printList(jet_list)
      
      printMenu()
      choice = int(input("please input your selection: "))

    elif choice == 2:
      value = int(input("please input the value you want to add to stream: "))
      stream_list.append(value)
      sortList(stream_list)

      print("here is the new stream list:", end = " ")
      printList(stream_list)

      printMenu()
      choice = int(input("please input your selection: "))

    elif choice == 3:
      print("jet:", end = " ")
      printList(jet_list)
      print("\nstream: ", end = " ")
      printList(stream_list)

      jetstream = jetStream(jet_list,stream_list)
      print("\njetstream: ", end = " ")
      printList(jetstream)

      printMenu()
      choice = int(input("please input your selection: "))

    elif choice == 4:
      print("quitting program...")
      quitProgram()

    else:
      print("\nthis value is not a choice, please input an appropriate\
 choice\n")
      choice = int(input("\nplease input your selection: "))


main()

################################################################
#RUN(number 1)
##----------------------------------------
##Please choose from the following options: 
##1: add a value to the list called jet
##2: add a value to the list called stream
##3: print jet, stream, and the merged jetstream
##4: quit the program
##----------------------------------------
##
##
##please input your selection: 3
##jet: [ -1 0 0 0 1 2 20 24 3000 ]
##
##stream:  [ 0 24 ]
##
##jetstream:  [ -1 0 0 0 0 1 2 20 24 24 3000 ]
##
##
##EMPTY_LIST RUN
##----------------------------------------
##Please choose from the following options: 
##1: add a value to the list called jet
##2: add a value to the list called stream
##3: print jet, stream, and the merged jetstream
##4: quit the program
##----------------------------------------
##
##
##please input your selection: 3
##jet: [ ]            
##
##stream:  [ ]
##
##jetstream:  [ ]
##
##
################################################################

