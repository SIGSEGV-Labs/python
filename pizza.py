size=input("what size pizza you want...(S/M/L)?")
bill=0
if(size=='s' or size =='S'):
  bill=bill+100
  print("Small size pizza is 100RS.")
elif size=='m' or size=='M':
  bill=bill+200
  print("medium size pizza is 200RS.")
else:
  bill=bill+300
  print("Large size pizza is 300RS.")
add_pepperoni=input("Do You Want pepperoni(Y/N)...?")
if add_pepperoni=='Y' or add_pepperoni=='y':
  if size=='S' or size=='s':
    bill=bill+30
  else:
    bill=bill+50
extra_cheese=input("Do you want extra cheese(Y/N)...?")
if extra_cheese=='Y' or extra_cheese=='y':
  bill=bill+20
print(f"(your final bill is {bill}")
