mixed = [10, 4.97, True, "mountain", [9, 8, 7]]
print("list is the "+str(mixed)+"is heare")
li_str = list("cheese")
print(li_str)
print("e" in li_str)
print("a" not in li_str)

#LIST INDEXING
input=["tiger Shroff","Ranveer Kapur","KApil Sharma","Ranveer Singh"]
print(input[3])
print(input[-3])

#INDEXING AND SLICING
up_by_two = [[0, 2], [4, 6], [8, 10], [12, 14]]
print(up_by_two)
print(up_by_two[0])
print(up_by_two[3][1])
furniture = ["chair", "table", "desk", "lamp", "bed"]
print(furniture[-5])
print("Most people own at least " + str(up_by_two[0][1]) + " " + furniture[0] + "s.")
floats = [0.98, 8.76, 6.54, 4.32]
print(floats[1:])
print(floats[1:3])
print(floats[:2])
#RESININIG LIST NUMBER 
example=[2,4,6,8,0]
print(example)
example[4:7]=[5,7,9]
print(example)
#del method
char=["Kuldeep","Adity","Shubham","Marsh"]
print(char)
del char[3]
print(char)

#.remove
a=["Kuldeep","Ashish","Marsh","shubham","Prathmesh"]
a.remove("Marsh")
print(a)

#.append Adding the value in the list
a=["Kuldeep","Ashish","Marsh","shubham","Prathmesh"]
print(a)
a.append("Anibhav")
print(a)

#.insert Adding the indexing value
a=["kuldeep","Ashish","Marsh","shubham","Prathmesh"]
print(a)
a.insert(1,"vaibhav")
print(a)

#.sort
a=["kuldeep","Ashish","Marsh","shubham","Prathmesh"]
print(a)
a.sort()
print(a)

#Number sort
num= [5,4,3,6,1,5.77]
print(num)
num.sort()
print(num)


















