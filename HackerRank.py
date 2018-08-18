# N = int(input("number? "))
#
# if N % 2 != 0 or (N >= 6 and N <= 20):
#     print("Weird")
# else:
#     print("Not Weird")


# if __name__ == '__main__':
#     a = int(input("One"))
#     b = int(input("Two"))
#     print(a + b)
#     print(a - b)
#     print(a * b)

#
# def is_leap(year):
#     if year % 4 == 0 and year % 100 != 0:
#         return True
#     else:
#         if year % 400 == 0:
#             return True
#         else:
#             return False
#
#
#
# year = int(input("Year"))
# print(is_leap(year))

#A = [1,2,3,4,5]
#B = [6,7,8,9,10]
# happy = 0
#
# s = input()
# guess = input().split(" ")
# A = input().split(" ")
# B = input().split(" ")
#
# for g in guess:
#     if g in A:
#         happy += 1
#     elif g in B:
#         happy -= 1
#
# print(happy)
#

# N = int(input())
# set = set()
#
# for i in range(N):
#     set.add(input().lower())
#
# print(len(set))

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#
#     print(a // b)
#     print(a / b)
#


n = 5
s = ""

for i in range(1, n + 1):
    a = list(range(1, i + 1)) + list(range(i - 1, 0, - 1))
    print(map(int, a))
