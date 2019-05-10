a = 10;
if a > 5:
    print("wow")


n = -2
if n > 0:
    print("양수")
elif n == 0:
    print("0")
else:
    print("음수")


# spam : 100
# egg : 500
# sagetti : 2000
price = 0
goods = "spam"
if goods == "spam":
    price = 100
elif goods == "egg":
    price = 500
elif goods == "spagetti":
    price = 2000

print(price)

# 삼항 연산자
# print(a > 5 ? "big" : "small")
print("big" if a > 5 else "small")

