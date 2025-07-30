x=int(input("How many times do you want your coin to be tossed?"))
import random 
heads= 0
tails = 0
for i in range(x):
  toss = random.randint(0,1)
  if toss == 0:
	  	print("heads")
	  	heads += 1
  else:
	  	print("tails")
	  	tails += 1
	  	
print("Percentage of heads:", (heads/x)*100,
"%")
print("Percentage of tails:",(tails/x)*100,
"%")