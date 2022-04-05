input = __import__('sys').stdin.readline
input()
A = set(input().split())
input()
M = input().split()
print("\n".join(['1' if i in A else '0' for i in M]))
