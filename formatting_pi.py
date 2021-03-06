#!/usr/bin/env python
from math import pi

print(pi)

print("2 places: {:.2f}".format(pi))
print("3 places: {:.3f}".format(pi))
print("4 places: {:.5f}".format(pi))

s1 = "2 places: {:.2f}".format(pi)
s2 = "3 places: {:.3f}".format(pi)
s3 = "4 places: {:.5f}".format(pi)

f1 = round(pi, 3)
print(f1)


person = 'Bob'
dog = 'Sal'

#       0      1
print("{:20s} and {:20s} are playing fetch".format(
    #  0     1
    person, dog)
)

big_number = 20395820395820395820395
print("{:,d}".format(big_number))
print("{big_number:,d}")

print("{:x}".format(big_number))
print("{:b}".format(big_number))


print(f"2 places: {pi:.2f}")  # python >= 3.6
print(f"3 places: {pi:.3f}")
print(f"4 places: {pi:.5f}")
x = f"2 + 2 = {2 + 2}"
print(x)
print(x)















