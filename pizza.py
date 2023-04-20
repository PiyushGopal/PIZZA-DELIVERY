# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests
pricesmall = 15
pricemedium = 20
pricelarge = 25
if size == "S":
  if add_pepperoni == "Y":
   pricesmall +=2
  else:
   pricesmall +=0

  if extra_cheese == "Y":
   pricesmall +=1
  else:
   pricesmall +=0
  print(f"Your bill is ${pricesmall} ")
if size == "M":
  if add_pepperoni == "Y":
   pricemedium +=3
  else:
   pricemedium +=0

  if extra_cheese == "Y":
   pricemedium +=1
  else:
   pricemedium +=0
  print(f"Your bill is ${pricemedium} ")
if size == "L":
  if add_pepperoni == "Y":
   pricelarge +=3
  else:
   pricelarge +=0

  if extra_cheese == "Y":
   pricelarge +=1
  else:
   pricelarge +=0
  print(f"Your bill is ${pricelarge} ")


































