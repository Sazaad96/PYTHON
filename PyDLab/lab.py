## Generator Function---------------------------------
import sys
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter>n):
           
     yield a
        a, b = b, a+b
        counter +=1
## Iterator object----------------------------------------
f = fibonacci(20)
print(f)

while True:
    try:
        print(next(f), end=' ')
    except StopIteration:
        break
    