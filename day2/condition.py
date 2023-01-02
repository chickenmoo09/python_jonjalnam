'''조건문
1. if / else
    if 조건:
        print(참일 때 실행할 것 작성)
    else 조건:
        print(거짓일 때 실행할 것 작성)
    elif 또 다른 조건:
        print(조건은 거짓 또 다른 조건이 참일 때 작성)
2. for
    for 변수 in range (반복 숫자):
        print(실행할 내용) ex) 34

    for 변수는 0부터 시작한다.

    for 변수 in range (시작, 까지)
        print(실행할 내용)
    *1씩 증가, 시작에 1 넣으면 1부터 시작할 수 있음 ㅋ ex) 41

    for 변수 in range (시작, 끝, 증감):
        print(실행할 내용)
'''
# apple=10
# orange=20
# if apple>orange:
#     print("사과가 큼")
# else:
#     print("오렌지가 큼")

# a=5
# b=5
# if a>b:
#     print("a가 큼")
# elif a<b:
#     print("b가 큼")
# else:
#     print("같음")3

# for i in range (3):
#     print("hi")

# for i in range (1,11):
#     print(i)

# for i in range (2,11,2):
#     print(i)

# for i in range (1,11,2):
#     print(i)

# 1.
# for i in range (1,11):
#     if i%2==1:
#         print(i)

# 2.
# for i in range (1,11):
#     if i%3!=0:
#         print(i)

# 3.
# for i in range (50,101):
#     if i%3==0:
#         if i%4==0:
#             print(i)

# 4.
# a=1
# for i in range (1,21):
#     if i%7==0:
#         a*=i
# print(a)

# 5.
# a=0
# for i in range (50,61):
#     if i%4!=0:
#         a+=i
# print(a)

6.
a=0
b=0
for i in range (1,101):
    if i%2==0:
        a+=i
    if i%2==1:
        b+=i
print(a-b)       


