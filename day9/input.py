'''
input(입력)
- 문법
  input("입력할 때 쓰고 싶은 내용")
'''
# 입력한거=input("입력하셈: ")
# print(입력한거)
# for i in range(1,4):
#     이름=input("당신의 이름을 입력하세요: ")
#     str=f"{이름}님 반가워요!"
#     print(str)
# while True:
#     이름=input("당신의 이름을 입력하세요: ")
#     str=f"{이름}님 반가워요!"
#     print(str)

# name=input("당신의 이름을 입력하세요: ")
# age=input("나이를 알려주세요: ")
# fvr=input("좋아하는 걸 알려주세요: ")
# str=f"{name}님 반가워요! 당신은 {age}세이고, {fvr}을 좋아하시네요!"
# print(str)

# for i in range(1,6):
#     num1=input("첫 번째 수: ")
#     num2=input("두 번째 수: ")
#     str=f"첫 번째 수는 {num1}이며, 두 번째 수는 {num2}이기 때문에 두 수의 합은 {int(num1)+int(num2)}입니다."
#     print(str)

while True:
    첫번째수=input("첫 번째 수: ")
    두번째수=input("두 번째 수: ")
    str=f"첫 번째 수는 {첫번째수}이며, 두 번째 수는 {두번째수}, 그러므로 두 수의 합은 {int(첫번째수)+int(두번째수)}이고, 두 수의 차는 {int(첫번째수)-int(두번째수)}이며, 두 수의 곱은 {int(첫번째수)*int(두번째수)}이고, 첫 번째 수를 두 번째 수로 나는 몫은 {int(첫번째수)//int(두번째수)}이며, 나머지는 {int(첫번째수)%int(두번째수)}이다."
    print(str)