def sum_of_digits(num):
    sum=0
    while num>0:
        sum=sum+num%10
        num=num//10
    return sum
num=int(input("Enter a number: "))
print(sum_of_digits(num))
