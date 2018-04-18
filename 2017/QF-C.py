import sys
from decimal import *
getcontext().prec = 25

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class Queue:
    def __init__(self):
        self.l = []

    def put(self, n):
        if (n == 0):
            return self
        for i in range(0, len(self.l)):
            if self.l[i][0] == n:
                self.l[i] = (n, self.l[i][1] + 1)
                return self
            elif self.l[i][0] > n:
                self.l.insert(i, (n, 1))
                return self
        self.l.append((n, 1))

    def pop(self):
        n, c = self.l.pop()
        if c > 1:
            self.l.append((n, c - 1))
        return n

    def put_with_count(self, n, c):
        if (n == 0):
            return self
        for i in range(0, len(self.l)):
            if self.l[i][0] == n:
                self.l[i] = (n, self.l[i][1] + c)
                return self
            elif self.l[i][0] > n:
                self.l.insert(i, (n, c))
                return self
        self.l.append((n, c))

    def pop_with_count(self):
        return self.l.pop()

    def empty(self):
        return len(self.l) == 0

def cunstruct_result_list(n):
    result = []
    q = Queue()
    q.put(n)
    max, min = 0, 0
    while not q.empty():
        n, c = q.pop_with_count()
        if n % 2 == 0:
            max, min = n / 2, n / 2 - 1
        else:
            max, min = n // 2, n // 2
        q.put_with_count(max, c)
        q.put_with_count(min, c)
        for i in range(0, len(result)):
            if result[i][0] == max and result[i][1] == min:
                result[i][2] += c
                break
            elif result[i][0] > max or result[i][1] > min:
                result.insert(i, [max, min, c])
                break
        else:
            result.append([max, min, c])
    return result

def solve(n, k):
    result = cunstruct_result_list(n)
    num = 0
    while len(result) != 0:
        max, min, c = result.pop()
        num += c
        if num >= k:
            return (max, min)

def main():
    t = int(input())
    for i in range(1, t + 1):
        #eprint(str(i))
        n, k = [Decimal(s) for s in input().split(" ")]
        max, min = solve(n, k)
        print("Case #{}: {} {}".format(i, max, min))

if __name__ == "__main__":
    main()
