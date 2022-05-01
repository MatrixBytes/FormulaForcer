import itertools
import string    
import time     

data = {
    'a': 21,
    'b': 22,
    'c': 18,
    'd': 22
}

result = 83

def force(data, result):
    ops = ['+', '-', '/', '*']
    length = 0

    while True:
        length += 1
        for num in itertools.product(data.keys(), repeat = length): 
            for op in ops:
                if eval(op.join([str(data[x]) for x in num])) == result:
                    return op.join([str(x) for x in num])

if __name__ == "__main__":
    print(force(data, result))