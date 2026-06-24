# Program: Reverse a Number using Function in Python
# Time Complexity: O(log n) where n = number of digits
# Space Complexity: O(1)
 """
    Returns the reverse of an integer.
    Works for positive numbers.
    Example: 123 -> 321,1200 -> 21
    """

def reverse_number(n):
    rev=0
    temp=n
    while temp>0:
        rev=rev*10+temp%10
        temp=temp//10
    if rev==n:
      print(f'{n} is palindrome number')
    else:
      print(f'{n} is not a palindrome number')
n=int(input("Enter a number:"))
reverse_number(n)
