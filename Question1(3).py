# #Favorite Sequence
#
#
# Input
# 6
# 7
# 3 4 5 2 9 1 1
# 4
# 9 2 7 1
# 11
# 8 4 3 1 2 7 8 7 9 4 2
# 1
# 42
# 2
# 11 7
# 8
# 1 1 1 1 1 1 1 1
# Output
# 3 1 4 1 5 9 2
# 9 1 2 7
# 8 2 4 4 3 9 1 7 2 8 7
# 42
# 11 7
# 1 1 1 1 1 1 1 1
# Explanation
# In the first test case, the sequence
# a
# a matches the sequence from the statement. The whiteboard states after each step look like this:
# [3]⇒[3,1]⇒[3,4,1]⇒[3,4,1,1]⇒[3,4,5,1,1]⇒[3,4,5,9,1,1]⇒[3,4,5,2,9,1,1].


#Code:
import math
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    l=[]
    for i in range(math.ceil(n/2)):
        if i!=(n-1-i):
            l.extend([arr[i],arr[n-1-i]])
        else:
            l.append(arr[i])
    print(*l)
