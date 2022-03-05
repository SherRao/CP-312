'''
CP 312 Assignment #1

Nausher Rao 190906250
'''
import timeit
import time

y = '''
def y(n):
    sum = 0;
    for i in range(n):
        sum += 1;
''';

g = '''
def g(n):
    sum = 0;
    for i in range(n):
        for j in range(n):
            sum += 1;
''';

h = '''
def h(n):
    sum = 0;
    for i in range(n):
        for j in range(n*n):
            sum += 1;
'''

k = '''
def k(n):
    sum = 0;
    for i in range(n):
        for j in range(i):
            sum += 1;
''';

l = '''
def l(n):
    sum = 0;
    for i in range(n):
        for j in range(i*i):
            for p in range(j):
                sum += 1;
''';

m = '''
def m(n):
    sum = 0;
    for i in range(n):
        for j in range(i*i):
            if(j%i==0):
                for p in range(j):
                    sum += 1;
''';

def a():
    print("============== Part A ==============");
    for n in [10000, 20000, 30000, 40000, 50000]:
        result = timeit.timeit(f'''y({n})''', number=1, setup=y);
        print(f"n = {n}, time = {result * 1000}ms");

    print();

def b():
    print("============== Part B ==============");
    for n in [100, 200, 400, 800, 1600]:
        result = timeit.timeit(f'''g({n})''', number=1, setup=g);
        print(f"n = {n}, time = {result * 1000}ms");

    print();

def c():
    print("============== Part C ==============");
    for n in [10, 30, 90, 270, 810]:
        result = timeit.timeit(f'''h({n})''', number=1, setup=h);
        print(f"n = {n}, time = {result * 1000}ms");

    print();

def d():
    print("============== Part D ==============");
    for n in [100, 200, 400, 800, 1600]:
        result = timeit.timeit(f'''k({n})''', number=1, setup=k);
        print(f"n = {n}, time = {result * 1000}ms");

    print();

def e():
    print("============== Part E ==============");
    for n in [5, 15, 25, 75, 125]:
        result = timeit.timeit(f'''l({n})''', number=1, setup=l);
        print(f"n = {n}, time = {result * 1000}ms");

    print();

def f():
    print("============== Part F ==============");
    for n in [5, 15, 25, 75, 125]:
        result = timeit.timeit(f'''m({n})''', number=1, setup=m);
        print(f"n = {n}, time = {result * 1000}ms");

    print();


def main():
    a();
    b();
    c();
    d();
    e();
    f();

main();