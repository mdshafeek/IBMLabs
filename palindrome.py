my_str = input("Enter a String: ")
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
    print("Palindrome!")
else:
    print("Not a Palindrome!")
