# Formula factorial 
def factorial(n): 
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#Find zero
def find_zero(f):
    arr = [int(i) for i in str(f)]
    count = 0
    for l in arr[::-1]:
        if l == 0:
            count += 1
        else:
            break
    print("Factorial Result is {0} and Total Zero {1}".format(f,count))

n = int(input("enter the number"))
find_zero(factorial(n))


