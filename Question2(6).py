# # #Range Sum Query-3

# # Given an list of n integers lst[] and multiple queries, each query asks for the sum of elements between two indices L and R (inclusive).

# # Write a program that efficiently answers multiple range sum queries on the list.
# Input
# The first line of input contains n space separated integers representing the elements of the list lst.
# The second line of input contains an integer q representing the number of queries.
# Next q lines contain q queries, where each query consists of two integers L and R, and you need to compute the sum of elements from index L to index R (inclusive).

# Constraints
# 1 ≤ n ≤ 105
# 1 ≤ q ≤ 105
# 1 ≤ lst[i] ≤ 106
# 0 ≤ L ≤ R < n
# Output
# For each query, output the sum of elements in the subarray lst[L] to lst[R] in a new line.

# Note
# Refer to the example test case for better understanding of input and output.
# Example
# Input
# 1 2 3 4 5
# 3
# 1 3
# 0 4
# 2 2

# Output
# 9
# 15
# 3


# Explanation
# Query 1: Sum of elements from index 1 to 3 -> lst[1] + lst[2] + lst[3] = 2 + 3 + 4 = 9
# Query 2: Sum of elements from index 0 to 4 -> lst[0] + lst[1] + lst[2] + lst[3] + lst[4] = 1 + 2 + 3 + 4 + 5 = 15
# Query 3: Sum of elements from index 2 to 2 -> lst[2] = 3



#Code:
# Your code here
listy=list(map(int,input().split()))
prefix_sum=[]

su=0
def prefix_sum_array(su):
    for i in range(len(listy)):
        su=su+listy[i]
        prefix_sum.append(su)

prefix_sum_array(su)
# print(prefix_sum)

def solve(L,R):
    if L==0:
        print(prefix_sum[R])
    else:
        ans=prefix_sum[R]-prefix_sum[L-1]
        print(ans)

q=int(input())

for i in range(q):
    L,R=map(int,input().split())
    solve(L,R)
