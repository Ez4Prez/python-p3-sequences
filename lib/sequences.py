#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return

    fib_sequence = [0, 1]

    while len(fib_sequence) < length:
        added_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(added_num)

    print(fib_sequence[:length])


    