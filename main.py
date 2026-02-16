print("enter min to max range.")

x=int(input("enter min range: "))
y=int(input("enter max range: "))
sqr=[]
even=[]
odd=[]
for i in range(x,y+1):
    i=i*i
    sqr.append(i)
 
print(f"squares '{x}' to '{y}' are '{sqr}'.")

for j in sqr:
    if j%2 == 0:
        even.append(j)
    else:
        odd.append(j)

print(f"even squares: {even}. odd squares: {odd}.")