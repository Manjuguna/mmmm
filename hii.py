l=input("input a letter of the alphabet:")
if l in('a','e','i','o','u'):
    print("%s is a vowel."%l)
elif l=='y':
    print("sometimes y stand for vowel,stand for constant")
else:
    print("%s is a constant."%l)
