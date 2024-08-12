def func(x,y=[4,3]):
    y.append(x)
    return y
print(func(2,[3,4]))