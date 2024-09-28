#print this pattern -> 1 4 7 10 13
for p in range(1,14,3):
  print(p)

#print this  pattern -> 1 3 7 11 13 15
for b in range(1,16,2):
  if b == 5 or b ==9:
    continue     #to skip the current iteration
  else: 
     print(b)  