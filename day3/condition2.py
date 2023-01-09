# while  조건:
#     실행할 코드 작성
# 1. 조건이 참이면 아래 코드가 실행됨
# 2. 조건이 거짓이면 while 이 끝남

# while 1>0:
#     print('안녕')

# while 1<0:
#     print('하이')

# for i in range(3):
#     print('for')

# i=0
# while i<3:
#     print('while')
#     i+=1

# 1. chatGPT 5번 출력
# i=0
# while i<5:
#     print('chatGPT')
#     i+=1

# 2. 1~10 중 짝수 출력
# i=1
# while i<11:
#     if i%2==0:
#         print(i)
#     i+=1

# 3. 1~20 중 4의 배수들의 합계
# i=1
# a=0
# while i<21:
#     if i%4==0:
#         a+=i
#     i+=1
# print(a)

# 4. 50~70 중 2와 3의 공배수
# i=50
# while i<71:
#     if i%2==0:
#         if i%3==0:
#             print(i)
#     i+=1

# 5. 100~110 중 홀수들의 곱
# i=100
# a=1
# while i<111:
#     if i%2==1:
#         a*=i
#     i+=1
# print(a)

6.
i=1
a=0
b=0
while i<101:
    if i%3==0:
        a+=i
while i<101:
    if i%7==0:
        b+=i
    i+=1
print(a-b)
        



    
        