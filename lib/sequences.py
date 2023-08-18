def print_fibonacci(n):
    if n <= 0:
        print([])
        return
    elif n == 1:
        print([0])
        return
    elif n == 2:
        print([0, 1])
        return

    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_val = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_val)

    print(fibonacci_sequence)
