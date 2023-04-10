'''
튜플(tuple)
- python 에서 사용하는 자료구조 중 하나
- 값이 바뀌면 안되는 상황에서 사용함(값이 바뀌지 않음 리스트와 차이점)
- 문법
    list[1,2,3]
    대괄호
    tuple(1,2,3)
    소괄호
- 특징
 1. 인덱싱(indexing) 가능
    대괄호 이용
 2. list 용 method 사용 불가능
   - append, pop, sort, reverse... 등 사용 불가능
 3. Slicing(:) 
'''

a=[1,2,3]
b=(1,2,3)
# print(type(a))
# print(type(b))
# print(a[2])
# print(b[2])
a[2]=100
print(a)
# b[2]=100
# print(b)
print(b[:2])