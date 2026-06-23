def Prod_of_digits(num):
    prod=1
    while num>0:
        prod=prod*(num%10)
        num=num//10
    return prod
num=int(input("Enter a number: "))
print(Prod_of_digits(num))
