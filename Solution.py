def f(n):
    if n == 0:
        return 0
    return f(n-1) + 100


n = int(input("enter : "))
print(f(n))

###################second method

# var1 = int(input("Enter number : "))
# var2 = var1*100
# print(var2)
