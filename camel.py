camcase =input("Enter something in Camelcase ") #camelCase
word=" "

for i in camcase:
	if i.isupper():
		word+="_"+i.lower()
	else:
		word+=i
print("snake_case : ",word)
