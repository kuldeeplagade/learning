#STRING METHODS
a="The uper case method"
print(a.upper())
print(a)

a="THE LOWER METHOD IS USED"
print(a.lower())
print(a)

#JOIN STRING
print("".join(["one","two","three"]))
print(",".join(["one","two","three"]))
print(".".join(["one","two","three"]))
print("  ".join(["one","two","three"]))

#MULTIPLE STRING METHODS
mixed_case = "A Song of Ice and Fire"
print(mixed_case.isupper())  
print(mixed_case.islower())  
print(mixed_case.upper())  
print(mixed_case.lower())  
print(mixed_case.istitle())  
title_case = mixed_case.title()
print(title_case)  
print(mixed_case.startswith("A"))  
print(mixed_case.endswith("e"))  
words = mixed_case.split()
print(words)  
print("".join(words).isalpha()) 

#MULTIPLE STRING METHOD 
the_string = "North Dakota"
print(the_string.rjust(17))  
print(the_string.ljust(17, "*"))  
center_plus = the_string.center(16, "+")  
print(center_plus)
print(the_string.lstrip("North"))
print(center_plus.rstrip("+"))  
print(center_plus.strip("+"))  
print(the_string.replace("North", "South"))  











