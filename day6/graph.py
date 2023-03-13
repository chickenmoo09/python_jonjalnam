'''
모듈(module) 설치
 - 터미널 창에서 pip 설치 명령어 사용
 ex) pip install 모듈이름
 - 설치된 모듈을 확인하고 싶을 때
 ex) pip list
 => matplotlib
모듈 불러오기
 - import 모듈이름
모듈 사용하기
 - 모듈이름.메소드()
 - 모듈이름.변수
'''
import matplotlib.pyplot as plt

# import matplotlib.pyplot
# matplotlib.pyplot.figure()
# matplotlib.pyplot.plot([0,1,2],[0,1,2])
# #                         x       y
# matplotlib.pyplot.show()

# import matplotlib.pyplot
# matplotlib.pyplot.figure()
# matplotlib.pyplot.plot([0,1,2],[1,3,5])
# #                         x       y
# matplotlib.pyplot.show()

# plt.figure()
# x=[0,1,2]
# y=[1,2,3]
# plt.plot(x,y,'ro')
# plt.show()

# plt.figure()
# x1=[0,100]
# y1=[0,100]
# x2=[0,100]
# y2=[0,50]
# plt.plot(x1,y1,'r',x2,y2,'b')
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.title("y=x, ""y=1/2x")
# plt.show()

# x=[]
# y=[]
# for i in range(100):
#     x.append(i)
#     y.append(-3*i+5)
# plt.figure()
# plt.plot(x,y,'r')
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.title("y=-3X+5")
# plt.show()

# x=[]
# y=[]
# for i in range(-100,100):
#     x.append(i)
#     y.append(i*i)
# plt.figure()
# plt.plot(x,y,'r')
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.title("y=x²")
# plt.show()

x1=[]
y1=[]
x2=[]
y2=[]
for i in range(-100,100):
    x1.append(i)
    y1.append(i*i)
    x2.append(i)
    y2.append(3*i)
plt.figure()
plt.plot(x1,y1,'r',x2,y2,'b')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("y=x², y=3x")
plt.show()