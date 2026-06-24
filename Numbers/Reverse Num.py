# Program: Reverse a Number using Function
# Works for +ve and numbers ending with 0
# Time: O(log n), Space: O(1)

    """
    Reverses digits of integer n
    123 -> 321
    """
def reverse_number(n):
    rev=0
    while n>0:
        rev=rev*10+n%10
        n=n//10
    print('Reverse number is:',rev)
n=int(input("Enter a number:"))
reverse_number(n)
