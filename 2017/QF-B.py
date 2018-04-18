import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def is_tidy(number_str):
    n = 0
    for c in number_str:
        nc = int(c)
        if nc < n:
            return False
        n = nc
    return True

def solve(number):
    while not is_tidy(number):
        for i in range(0, len(number) - 1):
            n1 = int(number[i])
            n2 = int(number[i + 1])
            if n1 > n2:
                number = number[:i] + str(n1 - 1) + '9' * (len(number) - 1 - i)
                number = number.lstrip('0')
                break
    return number

def main():
    t = int(input())
    for i in range(1, t + 1):
        #eprint(str(i))
        last_number_str = input()
        val = solve(last_number_str)
        print("Case #{}: {}".format(i, val))

if __name__ == "__main__":
    main()
