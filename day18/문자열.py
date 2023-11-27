# str="I am a boy"
# print(type(str))
# print(str)
# print(str[7])
# print(str[7:])
# print(str[:4])

# words=str.split("a")
# print(words)
# # print(words[3])

# addr1="www.google.com"
# addr2="www.naver.com"
# words=addr1.split(".")
# print(words[1])
# words=addr2.split(".")
# print(words[1])

# 민성="사과, 딸기, 바나나, 수박"
# 무경="복숭아, 딸기, 블루베리"
# a=민성.split(", ")
# b=무경.split(", ")
# words1=set(a)
# words2=set(b)
# print(words1&words2)
# print(words1|words2)

# 조예란❤️최민성

num1="090320-3812345"
num2="080709-4213568"
num3="791009-2812345"
num4="921122-1213568"
# num5="991122-5812345"
# num6="001225-6213568"

# def scni(scn):
#     a=scn.split("-")
#     if a[1][0]=="1" or a[1][0]=="3":
#         print("이 사람은 남자입니다.")
#     elif a[1][0]=="2" or a[1][0]=="4":
#         print("이 사람은 여자입니다.")
#     else:
#         print("올바르지 않은 주민번호입니다.")
# scni(num1)
# scni(num2)
# scni(num3)
# scni(num4)
# scni(num5)
# scni(num6)

def md(m):
    a=m.split("-")
    if a[0][:1]<"23":
        if 2023-(int(a[0][:1])+2000):
            print("미성년자입니다.")
    if a[0][:1]>"23":
        if 2023-(int(a[0][:1])+1900):
            print("성인입니다.")
md(num1)
md(num2)
md(num3)
md(num4)
        