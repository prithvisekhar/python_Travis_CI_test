st = input("Enter a word:")
j = -1
g = 0
for i in st:
    if i != st[j]:
      j = j - 1
      g = 1
      break
    j = j - 1
if g == 1:
    print("It's not a palindrome")
else:
    print("It's a palindrome")
