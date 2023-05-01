"""
딕셔너리(dictionary)       ※순서가 중요하지 않음
- python 에서 사용하는 자료구조 중 하나
- key 와 value 가 쌍으로 존재
- 문법=> 중괄호와 : 를 이용
- key 를 이용해서 indexing 가능
- indexing method 를 사용하는 방법
: get
- keys method 를 이용해서 dict. 내 key 값 모두를 확인할 수 있음
- values method 를 이용해서 dict. 내 value 값 모두를 확인할 수 있음
- value 를 수정하는 방법
    1) indexing 이용
    2) update method 이용
- key 와 value 쌍을 추가하는 방법
    1) indexing 이용
    2) update method 이용
- key 와 value 쌍을  삭제하는 방법
:del
- " key in dict " 구조로 사용 시 T/F 로 반환 가능
"""
sports={"손흥민":"축구", "류현진":"야구", "서장훈":"농구"}
# sports["서장훈"]="예능"
sports.update({"서장훈":"예능"})
# sports["김연아"]="피겨"
sports.update({"김연아":"피겨"})
del sports["서장훈"]
del sports["김연아"]
print(type(sports))
print(sports.get("류현진"))
print(sports["류현진"])
print(sports.keys())
print(sports.values())
print("손흥민" in sports)
print("강호동" in sports)

fruits={'orange':50, 'banana':100, 'apple':200}
fruit=input("This is fruit store. What do you want?: ")
if fruit in fruits:
    print(f"we have {fruit}. {fruits[fruit]} left.")
else:
    print(f"sorry, we don't have {fruit}")