i = int(input("Enter how many friends : "))
m = []
for a in range(0,i):
     b = input("Enter the name of friend ") 
     m.append(b)
#print(m)
for d in m :
    with open("name.txt","a") as f:
         print(d,file=f)#Here file=f is used so that the input can be written in the created file. 
    with open("gmail.txt","a") as g:
         print(d+"@gmail.com",file=g)#Here file=g is used so that the input can be written in the created file. 

    
