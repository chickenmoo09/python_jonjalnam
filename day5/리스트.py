'''
   리스트(list)

 - 열거형 변수를 나타내는 자료구조 중 하나
 - 대괄호를 이용해서 표현
 - 각 요소는 쉼표로 구분
 - 비어있는 리스트는 "[]" 로 표현
 - 메소드를 가짐
 <특징1>
  맨 오른쪽에 요소를 추가할 떄 append 메소드 사용
 <특징2>
  맨 오른쪽 요소를 삭제할 떄 pop 메소드 사용
 <특징3>
  리스트 전체를 비울 때는 clear 메소드 사용
 <특징4>
  오름차순 정렬할 때 sort 메소드 사용
 <특징5>
  리스트를 거꾸로 정렬할 때 reverse 메소드 사용
'''
# a=1
# b="리스트"
# c=[1,2,3,4]
# print(c)
# d=["사과","바나나","귤"]
# print(d)
# e=[1,"apple",2,"banana"]
# print(e)
# f=[]
# print(f)
# f.append(100)
# print(f)
# f.append(50)
# print(f)
# f.append(1)
# print(f)

# f.pop()
# print(f)
# f.pop()
# print(f)
# f.pop()
# print(f)

# g=[100,50,1]
# g.clear()
# print(g)

# h=[2,4,1,3]
# h.sort()
# print(h)
# i=["orange","cherry","apple"]
# i.sort()
# print(i)

# j=[2,4,1,3]
# j.reverse()
# print(j)

# Q1.
# j=[2,4,1,3]
# j.sort()
# j.reverse()
# print(j)

# Q2.
# k=[]
# for i in range(1,21):
#   if i%3==0:
#     k.append(i)
#     k.sort()
#     k.reverse()
# print(k)


# def gugudan(dan):
#   for i in range(1, 10):
#     return result

'''
  Indexing(인덱싱)
 - a=["가","나","다"]
       L  to  R
       0    1    2
       R  to  L
       -1   -2   -3
 - 요소를 이용해서 indexing 값을 찾는다.
                 ( L to R )
  Count(카운트)
   -> 요소가 리스트 안에 몇 개 인지 알려줌 (100을 해도 error가 나지 않음)
  Insert(인서트)
   -> 리스트 안에 원하는 자리에 원하는 갚을 추가할 때 사용 ( 자리, 값 ) 값에 자리보다 큰 값을 넣으면 그 값을 맨 뒤에 넣는다.
  Remove(리무브)
   -> 리스트 안에 원하는 값을 삭제할 때 사용
  Extend(익스텐드)
   -> 리스트와 리스트를 연결할 때 사용(잘 안씀)
  +(더하기)
   -> 리스트와 리스트를 연결할 때 사용(extend와 같음)
  Len(랜)
   -> 리스트의 길이를 알고싶을 때 사용
'''
# a=["가","나","다"]
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[-1])
# print(a[-2])
# print(a[-3])

# c=[1,2,3,4]
# print(c.index(3))
# print(c.index(4))
# print(c.index(100))

# c=[1,2,3,4,3]
# print(c.count(3))
# print(c.count(1))
# print(c.count(100))

# d=[1,2,3]
# d.insert(100,1)
# print(d)
# d.insert(1,100)
# print(d)

# e=[1,2,100,3]
# e.remove(100)
# print(e)
# e.remove(1)
# print(e)

# f=[1,2]
# g=[3,4]
# f.extend(g)
# print(f)
# g.extend(f)
# print(g)

# h=[1,2]
# i=[3,4]
# print(h+i)
# print(i+h)
# print(h+i+[5,6])

# k=[1,2,3]
# print(len(k))
# print(len(k+k))

# Q1. 내림차순으로 정렬한 뒤 하나씩 꺼내서 출력하기
# fruits=["banana","cherry","apple"]
# fruits.sort()
# fruits.reverse()
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

# Q2. indexing을 for을 써서
# fruits=["banana","cherry","apple"]
# fruits.sort()
# fruits.reverse()
# for i in range(3):
#   print(fruits[i])

# Q3. 숫자 없이 
# fruits=["banana","cherry","apple"]
# fruits.append("watermelon")
# fruits.sort()
# fruits.reverse()
# for i in range(len(fruits)):
#   print(fruits[i])

# Q4. 더 간단하게
# fruits=["banana","cherry","apple"]
# fruits.sort()
# fruits.reverse()
# for fruit in fruits:
#   print(fruit)