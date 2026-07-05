# friends = ["Kevin", "Karet", "Kalash", "Oscar"]
# # friends[1] = "Karen"
# # print(friends[1:2])
# lucky_numbers=[1,2,3,4,5]
#
# # extend
# friends.extend(lucky_numbers)
# # ! print(friends)
#
# # append
# new_friends_list = ["Kerate", "Lovish", "Karan", "bafana"]
# new_friends_list.append('karate kid')
# # print(new_friends_list)
# new_friends_list.remove("Kerate")
# # print(new_friends_list)
#
# print(new_friends_list)

# try:
#
#     nup = 10/0
#     myNumber = input("Enter a number:")
#     myNumber = float(myNumber)
#     print(myNumber)
# except ValueError:
#     print(ValueError)

SUITS = "♠ ♡ ♢ ♣".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
deck = [(s, r) for s in SUITS for r in RANKS]
print(deck)

listing = [1,2,3,4,5,6,7,8,9,10,11,12]
print(listing[0::4])