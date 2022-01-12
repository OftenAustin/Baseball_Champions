with open("winners.txt","r") as f: winners,team = [s.strip().replace("\t", " ") for s in  f.readlines()],input("What team do you want to search for? ").strip() 
indices = [winners.index(i) for i in winners if team == i[4:].strip()]
if indices == [] or len(team) < 4:print("Team not found")
else:
  for number in indices: print(winners[number][:4])

""" Run if you dare (one line madness) """


# f = open("winners.txt","r"); winners,team = [s.strip().replace("\t", " ") for s in  f.readlines()],input("What team do you want to search for? ").strip(); f.close(); indices = [winners.index(i) for i in winners if team == i[4:].strip()]; (print("Team not found") if indices == [] else [print(winners[number][:4]) for number in indices])

# Same program just on one line
