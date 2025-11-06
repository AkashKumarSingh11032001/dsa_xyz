# 1. print name N times using recursion
def print_name_n_times(name, n):
    if n <= 0:
        return
    print(f'{n} = {name}')
    n -= 1
    print_name_n_times(name=name, n=n)

# 2. print linerly from 1 to n
def print_1_to_n(i, n):
    if i > n:
        return
    print(i)
    i += 1
    print_1_to_n(i=i, n=n)

# 3. print from n to 1
def print_n_to_1(n):
    if n <= 0:
        return
    print(n)
    n -= 1
    print_n_to_1(n)

# 4. print 1 to n [backtraacking]
def print_1_to_n_bt(i):
    if i <= 1:
        return
    print_1_to_n_bt(i=i-1)
    print(i)

# 5. print n to 1 [backtracking]
def print_n_to_1_bt(n):
    if n < 1:
        return
    print(n)
    print_n_to_1_bt(n - 1)


def main():
    print_name_n_times('Akash', 5)
    print_1_to_n(1, 10)
    print_n_to_1(10)
    print_1_to_n_bt(3)
    print_n_to_1_bt(3)


if __name__ == "__main__":
    main()
