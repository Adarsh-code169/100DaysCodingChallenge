#Question 1 :-

#Subsequence

# Given a string S, print all its possible non-empty subsequences (non-contiguous sequences of characters) in lexicographical order. A String is said to be a subsequence of another String, if it can be obtained by deleting 0 or more character without changing its order
# Input
# The first line of input consists of a string representing a word made up of lowercase alphabetic characters.
# Output
# Print space separated non-empty subsequences of the string in lexicographical order
# Example
# Input :
# ab
# Output :
# a ab b

# Input :
# abc
# Output :
# a ab abc ac b bc c



#Code:
def generate_subsequences(s, index, current, result):
    if index == len(s):
        if current:
            result.append(current)
        return
    generate_subsequences(s, index + 1, current + s[index], result)
    generate_subsequences(s, index + 1, current, result)

s = input()
result = []
generate_subsequences(s, 0, "", result)
result.sort()
print(" ".join(result))
