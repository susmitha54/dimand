#Write a program that prints out a diamond shape using #.
# Hint - print(5 * "$") will print  - $$$$$
# Hint - print(5* "$ ") will print  - $ $ $ $ $

n = int(input("Enter the number of rows: "))
for i in range(n):
    print(" "*(n-i-1) + "# "*(i+1)) 
for i in range(n-1,-1,-1):
    print(" "*(n-i-1) + "# "*(i+1))