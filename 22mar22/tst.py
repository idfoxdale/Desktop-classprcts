files = open("test.txt", "r", encoding="utf8" )
data_files = files.read()
print("Data in file = ", data_files)
data_lst = data_files.split()
print("Convertd to List as strings = ", data_lst)
data_lst.insert(0, 5)
print("First insert res = ", data_lst)
data_lst.insert(0, 50)
print("Second insert res = ", data_lst)

files.close()


with open("test.txt") as f:
    lst = [int(x) for x in f.read().split()]
    print(lst)

print("List of integers = ", lst)   
lst.insert(0, 5)
print("inserting 5 at 0, new list - ", lst )

""" print(data_files)
tst_lst1 = [10, 20, 30, 40]
print(tst_lst1)
print(list(tst_lst1)) """