def addition(a,b):
    return(a+b)
def subtraction(a,b):
    return(a-b)
def multiplication(a,b):
    return(a*b)
def division(a,b):
    return(a/b)
print("menu")
print("operation:\n1.addition\n2.subtraction\n3.multiplication/n4.division")
ch=int(input("\n enter your choice:"))
    
x=int(input("enter first value"))
y=int(input("enter second value"))
if ch==1:
      print("sum:",addition(x,y))
elif ch==2:
      print("difference:",subtraction(x,y))
elif ch==2:
      print("product:",multiplication(x,y))
elif ch==4:
      print("ratio:",division(x,y))
exit()
