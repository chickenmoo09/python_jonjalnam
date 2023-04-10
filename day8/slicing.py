'''
 • 리스트 slice 하는 방법
→ ":" rlgh tkdyd  1   ~   10
                이상     미만
'''
# #  0 1 2 3
# a=[1,2,3,4]
# print(a[1:3])
# print(a[:2])
# print(a[2:])
# print(a[:])
# # → [2, 3]
# #   [1, 2]
# #   [3, 4]
# #   [1, 2, 3, 4]

# b=[]
# for i in range(10):
#     b.append(i)
# print(b[:3])
# print(b[2:5]+b[8:])
# # → [0, 1, 2]
# # → [2, 3, 4, 8, 9]

# c=[]
# for i in range(1,21):
#     if i%2==0:
#         c.append(i)
# c.reverse()
# print(c[:3])
# #  → [20, 18, 16]

# d=[]
# for i in range(100,200):
#     if i%5==0:
#         if i%6==0:
#                 d.append(i)
# d.pop()
# d.append(210)
# d.reverse()
# print(d[:])
# # → [210, 150, 120]