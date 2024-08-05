import numpy as np


def func1():
    a = np.linspace(1, 10, num=10)
    print(a)

def func2():
    a = np.zeros((3, 3), dtype=int)
    print(a)

def func3():
    a = np.random.randint(1, 10+1, size=(5, 5))
    print(a)

def func4():
    a = np.random.randint(0, 1+1, size=(4, 4))
    print(a)

def func5():
    a = np.random.randint(1, 10+1, size=(5))
    print(a)
    b = np.random.randint(1, 10+1, size=(5))
    print(b)
    print(f'a + b = {a + b}')
    print(f'a - b = {a - b}')
    print(f'a * b = {a * b}')

def func6():
    a = np.random.random(size=7)
    print(a)
    b = np.random.random(size=7)
    print(b)
    print(f'Dot product: {np.dot(a, b)}')

def func7():
    a = np.random.randint(1, 10+1, size=(2, 2))
    print(a)
    b = np.random.randint(1, 10+1, size=(2, 3))
    print(b)
    print(np.dot(a, b))

def func8():
    a = np.random.randint(1, 10+1, size=(3, 3))
    print(a)
    print(f'Inverse matrix: {np.linalg.inv(a)}')

def func9():
    a = np.random.rand(4, 4)
    print(a)
    print(f'Transported: {a.T}')

def func10():
    a = np.random.randint(1, 10+1, size=(3, 4))
    print(a)
    b = np.random.randint(1, 10+1, size=4)
    print(b)
    print(f'a * b: {a*b}')

def func11():
    a = np.random.randint(0, 1+1, size=(2, 3))
    print(a)
    b = np.random.randint(0, 1+1, size=3)
    print(b)
    print(f'a * b: {np.dot(a, b)}')

def func12():
    a = np.random.randint(1, 10+1, size=(2, 2))
    print(a)
    b = np.random.randint(1, 10+1, size=(2, 2))
    print(b)
    print(f'Primary multiplication: {a*b}')

def func13():
    a = np.random.randint(1, 10+1, size=(2, 2))
    print(a)
    b = np.random.randint(1, 10+1, size=(2, 2))
    print(b)
    print(f'Result: {np.dot(a, b)}')

def func14():
    a = np.random.randint(1, 100+1, size=(5, 5))
    print(a)
    print(f'Sum: {a.sum()}')

def func15():
    a = np.random.randint(1, 10+1, size=(4, 4))
    print(a)
    b = np.random.randint(1, 10+1, size=(4, 4))
    print(b)
    print(f'Difference: {a - b}')
    
def func16():
    a = np.random.rand(3, 3)
    print(a)
    print(a.sum(axis=1).reshape(-1, 1))

def func17():
    a = np.random.randint(1, 100+1, size=(3, 4))
    print(a)
    print(a**2)

def func18():
    a = np.random.randint(1, 50+1, size=4)
    print(a)
    print(a ** 0.5)

if __name__ == '__main__':
    # func1()
    # func2()
    # func3()
    # func4()
    # func5()
    # func6()
    # func7()
    # func8()
    # func9()
    # func10()
    # func11()
    # func12()
    # func13()
    # func14()
    # func15()
    # func16()
    # func17()
    # func18()