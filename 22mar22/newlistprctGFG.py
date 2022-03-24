from operator import ne


List = []
print("Blank list: ")
print(List)

List.append(20)
print("List 1st operation ", List)

List.append(30)
print("List 2nd append operation ", List)

newstring = "newstring"
List.append(newstring)
print("List newstring append operation ", List)

Listnew = [["Apple", "Bnana", "1000", 1000], ["Almond", "Figs", 20, "40"]]

print(Listnew)
print(len(Listnew))
print("The size of list 'List' is ", (len(List)))

List.insert(0,4)
print(List)
newlist = List.copy()
print( "new list copied ", newlist)
necpy = newlist.copy()
necpy.reverse()
print(necpy)
f = open("test.txt")
mynewlist = [int(x) for x in f.read().split()]
necpy.extend(mynewlist)
print(necpy)
necpy.extend([int(x) for x in f.read().split()])
print("new reslt", necpy)