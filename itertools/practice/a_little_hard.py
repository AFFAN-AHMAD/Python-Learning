"""
5. Use itertools.permutations() and itertools.product() together to solve a small constraint problem
— e.g., generate all valid 4-digit codes using digits 1–4 with no repeated digits,
where the code is divisible by 4.
"""

from itertools import (permutations, product)
# print(product())
#
listing = [i+1 for i in range(4)]
all_perms = permutations(listing)
# print(all_perms)
# all_perms = map()
tup = (1,2,3)
# str(tup)
# print()
new_list = []
for tup in all_perms:
    integ = ""
    print(tup)
    for num in tup:
        integ+=str(num)

    new_list.append(integ)
print(new_list)
all_perm = filter(lambda x: int(x)%4 == 0, new_list)
print(list(all_perm))