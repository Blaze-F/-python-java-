any_list = [0 for i in range(0, 7)]
print(any_list)
changes = [1 for i in range(0, 3)]
print(changes)
any_list[2:5] = changes
print(any_list)
any_list[2:6] = changes
print(any_list)

"""
[0, 0, 0, 0, 0, 0, 0]
[1, 1, 1]
[0, 0, 1, 1, 1, 0, 0]
[0, 0, 1, 1, 1, 0]
"""

from string import ascii_lowercase

print(ascii_lowercase[0:2])
print(ascii_lowercase[3])
