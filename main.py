#Given a non-empty array of integers, every element appears twice except for one. Find that single one.
def single_number(integers):
  list = []
  repeats = []
  for i in range (0, len(integers)):
    list.append(integers[i])
  for x in range (0, len(integers)):
    for y in range (x+1, len(list)):
      if list[y]==integers[x]:
        repeats.append(list[y])
  for a in range (len(integers)-1, -1,-1):
    for b in range (0, len(repeats)):
      if integers[a]==repeats[b] and a <= len(list):
        list[a] = -1
        
  for x in range (0, len(list)):
    if(list[x] != -1):
      return list[x]
pass

list = [4,1,2,1,2]
list2 = [2,2,1]
single_number(list)
single_number(list2)