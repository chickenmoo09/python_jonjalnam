import matplotlib.pyplot as plt
# x=[]
# y=[]
# for i in range(-10,11):
#     x.append(i)
#     y.append(i*i*i)
# plt.figure()
# plt.plot(x,y)
# plt.show()

# x=[]
# y=[]
# for i in range(-10,11):
#     x.append(i)
#     y.append(2**i)
# plt.figure()
# plt.plot(x,y)
# plt.show()

# x1=[]
# y1=[]
# y2=[]
# y3=[]
# y4=[]
# for i in range(-10,11):
#     x1.append(i)
#     y1.append(i*i)
#     y2.append(i)
#     y3.append(i*-1)
#     y4.append(i*-i)
# plt.figure()
# plt.plot(x1,y1,x1,y2,x1,y3,x1,y4)
# plt.show()

# figure,axes=plt.subplots(2,1)
# fruits=["apple","banana","cherry","orange"]
# counts=[4,6,5,10]
# bar_color=["red","yellow","purple","orange"]
# axes[0].barh(fruits,counts,color=bar_color)
# axes[1].bar(fruits,counts,color=bar_color)
# plt.show()

figure,axes=plt.subplots(2,2)
x1=[]
y1=[]
x2=[]
y2=[]
for i in range(-10,11):
    x1.append(i)
    y1.append(i)
    x2.append(i)
    y2.append(i*i)
fruits=["apple","banana","cherry","orange"]
counts=[4,6,5,10]
bar_color=["red","yellow","purple","orange"]
axes[0,0].barh(fruits,counts,color=bar_color)
axes[1,0].bar(fruits,counts,color=bar_color)
axes[0,1].plot(x1,y1)
axes[1,1].plot(x2,y2)
plt.show()