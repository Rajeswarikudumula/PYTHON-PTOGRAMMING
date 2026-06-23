a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
for i in range(1,min(a,b)+1):
  if a%i==0 and b%i==0:      
    hcf=i
print("hcf is:",hcf)
print("LCM is:",(a*b)//hcf)
