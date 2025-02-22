# #Prefix Removals
#
# You are given a string
# s
# s consisting of lowercase letters of the English alphabet. You must perform the following algorithm on
# s
# s:
#
# Let
# x
# x be the length of the longest prefix of
# s
# s which occurs somewhere else in
# s
# s as a contiguous substring (the other occurrence may also intersect the prefix). If
# x
# =
# 0
# x=0, break. Otherwise, remove the first
# x
# x characters of s, and repeat.
#
# A prefix is a string consisting of several first letters of a given string, without any reorders. An empty prefix is also a valid prefix. For example, the string "abcd" has 5 prefixes: empty string, "a", "ab", "abc" and "abcd".
#
# For instance, if we perform the algorithm on
# s
# s = "abcabdc",
#
# Initially, "ab" is the longest prefix that also appears somewhere else as a substring in
# s
# s, so
# s
# s = "cabdc" after
# 1
# 1 operation.
# Then, "c" is the longest prefix that also appears somewhere else as a substring in
# s
# s, so
# s
# s = "abdc" after
# 2
# 2 operations.
# Now
# x
# =
# 0
# x=0 (because there are no non-empty prefixes of "abdc" that also appear somewhere else as a substring in
# s
# s), so the algorithm terminates.
#
# Find the final state of the string after performing the algorithm.
# Input
# The first line of the input contains a single integer
# t
# t (
# 1
# ≤
# t
# ≤
# 1
# 0
# 4
# 1≤t≤10
# 4
#  ) — the number of test cases.
#
# This is followed by
# t
# t lines, each containing a description of one test case. Each line contains a string
# s
# s. The given strings consist only of lowercase letters of the English alphabet and have lengths between
# 1
# 1 to
# 2
# ⋅
# 1
# 0
# 5
# 2⋅10
# 5
#   inclusive.
#
# It is guaranteed that the sum of lengths of
# s
# s over all test cases does not exceed
# 2
# ⋅
# 1
# 0
# 5
# 2⋅10
# 5
#  .
# Output
# For each test case, print a single line containing the string
# s
# s after executing the algorithm. It can be shown that such string is non-empty.
# Example
# Input
# 6
# abcabdc
# a
# bbbbbbbbbb
# codeforces
# cffcfccffccfcffcfccfcffccffcfccf
# zyzyzwxxyyxxyyzzyzzxxwzxwywxwzxxyzzw
# Output
# abdc
# a
# b
# deforces
# cf
# xyzzw
# Explanation
# The first test case is explained in the statement.
# In the second test case, no operations can be performed on
# s
# s.
# In the third test case,
# Initially,
# s
# s = "bbbbbbbbbb".
# After
# 1
# 1 operation,
# s
# s = "b".
# In the fourth test case,
# Initially,
# s
# s = "codeforces".
# After
# 1
# 1 operation,
# s
# s = "odeforces".
# After
# 2
# 2 operations,
# s
# s = "deforces".




#Code:

def longest_prefix_in_substring(s):
    n = len(s)
    for i in range(n):
        prefix = s[:i + 1]
        if s.find(prefix, i + 1) != -1:
            return i + 1
    return 0


def process_string(s):
    while True:
        x = longest_prefix_in_substring(s)
        if x == 0:
            break
        s = s[x:]
    return s


def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    results = []

    for i in range(1, t + 1):
        s = data[i]
        final_string = process_string(s)
        results.append(final_string)

    print("\n".join(results))


if __name__ == "__main__":
    main()
