def is_palindrome(num):
    if (num // 10 == 0 ) or (num % 10==0):
        return False
    temp = num
    reversed_num = 0

    while temp > 0:
        reversed_num = temp % 10 + reversed_num * 10
        temp = temp // 10
    if num == reversed_num:
        return True
    else:
        return False

# print(is_palindrome(202))

def infinite_palindrome():
    num = 0
    while True:
        if is_palindrome(num):
            i = yield num
            # print(i)
            if i is not None:
                num = i
        num+=1
# g = infinite_palindrome()


pal_gen = infinite_palindrome()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    pal_gen.send(10 ** (digits))
    if i >1000 :
        pal_gen.close()