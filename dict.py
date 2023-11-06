#simple Example 
'''dict={"kuldeep":"Good Morning",
      "Ashish" : "Good AfteNoon",
      "Vaibhav" : "Good Night"}
print(dict["Vaibhav"])

dict1={1:"kuldeep",2:"Ashish",3:"Aniket",4:"vaibhav"}
print(dict1)
print(dict1[3])

#keys
info={'name':"karan",'age':"19",'eligible':True}
print(info)
print(info.keys())

for key in info.keys():
    print(f"The values of the key is {key} is {info[key]}")

#items
info={'name':"karan",'age':"19",'eligible':True}
print(info)
print(info.items())
for key,value in info.items():
    print(f"The values of the key is {key} is {value}")

#Example
# example solution
dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(dictionary["a"])
print("a" in dictionary)
print("b" not in dictionary)

#Methods
famous_songs = {"Queen": "Bohemian Rhapsody",
                "Bee Gees": "Stayin' Alive",
                "U2": "One",
                "Michael Jackson": "Billie Jean",
                "The Beatles": "Hey Jude",
                "Bob Dylan": "Like A Rolling Stone"}  
print(len(famous_songs))  
for key in famous_songs.keys(): 
    print(key)
print(famous_songs.values())  
for key, value in famous_songs.items():  
    print(key, value)
print(famous_songs.get("Promise of the Real", "That is not a key that appears in the dictionary."))

#.fromkey()
ex ={}.fromkeys(["Name"],"Ashish",)
print(ex)'''

#example
for key, value in {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant").items():
    print(key, value)
 
fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
print(fast_food_items.pop("McDonald's"))
 
fast_food_items.popitem()
print(fast_food_items)



















