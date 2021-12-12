fibolist = []
term = int(input("Enter the number you're looking for"))
for i in range(term): fibolist.append(fibolist[-1]+fibolist[-2]) if i >= 2 else fibolist.append(1)
for i,num in enumerate(fibolist): print(i+1,num) if i+1 == term else print(i+1)