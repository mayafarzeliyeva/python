a=input("Enter something:")
b=" "
for i in a :
	if i in ["A","I","O","U","E","a","i","e","o","u"]:
		continue
	else:
		b=b+i
print("text=: ",b)
