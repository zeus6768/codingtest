def star_triangle(n):
    if n == 0:
        return
    star_triangle(n - 1)
    print("*" * n)
    
n = int(input())

star_triangle(n)