

def generate_nums(num):
    nums = range(1, num + 1, 2)
    for i in nums:
        yield i

for i in generate_nums(15):
    print(i)

