import random

computer = random.choice([-1, 0,1])
youstr = input("Enter your choice: ")
youdict = {"s": 1, "w": -1, "g":0}
reversedict = {1: "sanke", -1: "water", 0: "gun"}


you = youdict[youstr]

print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

if(computer==you):
    print("its a draw")
else:
  if(computer==-1 and you==0):
     print("you lose")
  elif(computer ==-1 and you ==1):
     print("you win")
  elif(computer==1 and you==-1):
     print("you lose")
  elif(computer==1 and you==0):
     print("you win")
  elif(computer==0 and you==1):
     print("you lose")
  elif(computer==0 and you==-1):
     print("you win")
  else:
     print("something went wrong")
 