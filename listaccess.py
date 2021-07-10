from listoperations import *
l1=[]
n=int(input("list size"))
for i in range(0,n):
    ele=int(input())
    l1.append(ele)
print(list_sum(l1))
print(list_sort(l1))
st=input()
print(string_list_conversions(st))
"""
list size5
3
2
1
5
4
15
[1, 2, 3, 4, 5]
welocme to cse a
['w', 'e', 'l', 'o', 'c', 'm', 'e', ' ', 't', 'o', ' ', 'c', 's', 'e', ' ', 'a']
"""
