####################################################################
##CIS 117 Internet Programming: Python
##Lab #6: "Christmas Card: Message Class"
####################################################################
## the message class provides two functions, append and toString
## this class creates a message object that stores a Sender and
## a receiver.
## the user can choose to add a body to the message using the
## append function or to convert the message into a string
## using the toString function
##
## append(self,line)
## precondition: none
## postcondition: adds a line to the body of the message
##
## toString(self)
## precondition: none
## postcondition: returns the sender, receiver, and body of the
## message as a string.
####################################################################

class Message:
  def __init__(self,send,recieve):
    self._sender = str(send) + "\n"
    self._recipient = str(recieve) + "\n"
    self._body = ""

  def append(self, line):
      if self._body == "":
        self._body = str(line) + "\n"
      else:
        self._body = self._body + str(line) + "\n"

  def toString(self):
    return "From: "+ self._sender + "\n" + "To: "+ self._recipient\
           + "\n" + self._body
  


###############################
##         |Test Run| 
##          --------
##
###############################
##From: Bob
##
##To: Santa
##
##For Christmas, I would like:
##Video games
##World peace
##############################
