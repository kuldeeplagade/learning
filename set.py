#Methods
'''Name ={"kuldeep","Ashish","Adity"} #add
Name.add("Shubham")
print(Name)

Name ={"kuldeep","Ashish","Adity"} #remove
Name.remove("Adity")
print(Name)

Name ={"kuldeep","Ashish","Adity"} #discard
Name.discard("Avinash")# not remove but no error
print(Name)

#clear
#Name ={"kuldeep","Ashish","Adity"}
#Name.clear()
#print(Name)

Name ={"kuldeep","Ashish","Adity"} #discard
Name.discard("Avinash")# not remove but no error
print(Name)

#copy
Name ={"kuldeep","Ashish","Adity"} #discard
set=Name.copy()
print(set)

#union
name1={"kuldeep","Ashish","Vaibhav"}
name2={"Adity","Shubham","Prathamesh"}
set=name1.union(name2)
print(set)

#intersection
name1={"Kuldeep","Ashish","Vaibhav",}
name2={"Adity","Shubham","Prathamesh","Kuldeep"}
set=name1.intersection(name2)
print(set)'''

#difrrence
name1={1,2,3,4,}
name2={5,6,7,8,9}     
set=name1.difference(name2)  #name2-name1
print(set)








































