def fib_calc(n, m):
    fib_list = [0, 1]  
    fib1_factors = []
    fib2_factors = []

    for _ in range(max(n, m)):
        fib_list.append(fib_list[-1] + fib_list[-2])
        
    fib1 = fib_list[n - 1]
    fib2 = fib_list[m - 1]

    for i in range(fib1):
        if fib1 % (i + 1) == 0:
            if fib1 != i + 1:
                fib1_factors.append(i + 1)
        
    for i in range(fib2):
        if fib2 % (i + 1) == 0:
            if fib2 != i + 1:
                fib2_factors.append(i + 1)
    print max(list(set(fib1_factors).intersection(fib2_factors)))

fib_calc(11, 16)
