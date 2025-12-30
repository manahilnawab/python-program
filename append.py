thislist=["apple","banana","cherry"]
thislist.append("orange")
print(thislist)
thislist.insert(2,"mango")
print(thislist)
tropical=["mango","pineapple"]
thislist.extend(tropical)
print(thislist)

thislist.remove("banana")
print(thislist)
thislist.pop(2)
print(thislist)
del thislist[0]
print(thislist)
thislist.clear()
print(thislist)

