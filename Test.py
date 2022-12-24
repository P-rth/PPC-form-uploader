import os

os.system('cls||clear')
loc = "links.txt"
try:
    f = open(loc)
except:
    print("links.txt not found please enter location:")
    print("Go to file > right click while holding shift > copy as path > paste here")
    path = input("--> ")
    path = path.replace('"','')
    f = open(path)

links = f.read()
a = links.split(", ")



for i in range(0,len(a)):
    k = a[i]
    print(str(i)+") "+k)


input("Enter to continue")
