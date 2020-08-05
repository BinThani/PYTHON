# Sum from n to 1
def sums(n):
    if n == 1:
        return 1
    else:
        return n+sums(n-1)

print(sums(3))
