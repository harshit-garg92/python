def generate(limit):
    for i in range(2,limit+1,2):
        yield i

for num in generate(10):
    print(num)

