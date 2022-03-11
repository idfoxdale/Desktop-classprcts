Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
my_set = {0, 'apple', 3.5}
print(my_set)
{0, 3.5, 'apple'}
print(type(my_set))
<class 'set'>


def myfunctlen(n):
    return len(n)

x = map(myfunctlen, ('apple', 'banana', 'cherry'))

# map(function, iterables)
# map(function, iterable[, iterable1, iterable2,..., iterableN])

def mynewfunctinclambda(m):
    p = lambda m: m + 3
    q = p(m)
    print("hello this is an expression " + str(q))

mynewfunctinclambda(3) 
