#while loop
dec_int = 10
 
while dec_int != 0:
    print(dec_int)
    dec_int += 1
#for loop
words = "hello world"
 
for letter in words:
    print(letter)

user_str = input("Please enter a string.")
 
count = 0  # This variable will be used to hold the number of characters in the string.
# This for loop adds 1 to count for each character in user_str.
for char in user_str:
    count += 1
 
print(user_str)  
print(count)

#range with  1 arrgumnet
input = range(5)
for num in input:
    print(num)

#range with 2 arrgumments
input= range(4, 7)
for num in input:
    print(num)

#range with 3 arrgumnets
input=range(6, -1, -2)
for num in input:
    print(num)

















