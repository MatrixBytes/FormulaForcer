import itertools
import string    
import time     
from colorama import Fore

data = {
    'h': 5,
    'g': 8,
    'p': 10,
}

result = 20

tasks = [[{'h': 3, 'g': 4, 'p': 10}, 6]]

def force(data, result, tasks, todo = 1):
    data['2'] = 2
    data['0.5'] = 0.5
    ops = ['+', '-', '/', '*']
    length = 0
    did = 0
    
    while True:
        length += 1
        for num in itertools.product(data.keys(), repeat = length): 
            for op in ops:
                if eval(op.join([str(data[x]) for x in num])) == result:
                    form = op.join([str(x) for x in num])

                    done = 0

                    for probe in tasks:
                        for val in probe[0].keys():
                            form = form.replace(val, str(probe[0][val]))
                        if eval(form) == probe[1]:
                            done += 1
                    
                    if len(tasks) == done:
                        did += 1
                        print(f'{Fore.CYAN}[{Fore.LIGHTMAGENTA_EX}FF{Fore.CYAN}] {Fore.LIGHTMAGENTA_EX}Found a right formula! {op.join([str(x) for x in num])} [{did}/{todo}]')

                        if did == todo:
                            return
                    #else:
                    #    print(f'{Fore.CYAN}[{Fore.LIGHTMAGENTA_EX}FF{Fore.CYAN}] {Fore.LIGHTMAGENTA_EX}Failed, only {done}/{len(tasks)} tests passed! {op.join([str(x) for x in num])}')

if __name__ == "__main__":
    force(data, result, tasks, todo = 100)
