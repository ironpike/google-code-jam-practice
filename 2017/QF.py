import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class Pancakes:
    def __init__(self, pancakes):
        self.cakes = []
        if isinstance(pancakes, str):
            for c in pancakes:
                self.cakes.append(c == '+')
        elif isinstance(pancakes, Pancakes):
            self.cakes = list(pancakes.cakes)
    
    def __str__(self):
        return ''.join(['+' if x else '-' for x in self.cakes])
    
    def is_happy(self):
        if False in self.cakes:
            return False
        return True
    
    def flip(self, flipper_width, position):
        for i in range(position, position + flipper_width):
            self.cakes[i] = not self.cakes[i]

    def find_next_flip_position(self, flipper_width):
        times = len(self.cakes) // flipper_width
        for time in range(1, times + 1):
            for position in range(0, len(self.cakes) - flipper_width * time + 1):
                if self.is_good_position_check1(position, position + flipper_width * time):
                    if self.is_good_position_check2(position, position + flipper_width):
                        return position
        return None
    
    def is_good_position_check2(self, start, end):
        for i in range(start, end):
            if not self.cakes[i]:
                return True
        return False

    def is_good_position_check1(self, start, end):
        last = self.cakes[start - 1] if start != 0 else True
        if last != self.cakes[start]:
            if end == len(self.cakes):
                if not self.cakes[end - 1]:
                    return True
            elif self.cakes[end - 1] != self.cakes[end]:
                return True
        return False

    def len(self):
        return len(self.cakes)

def solve(pancakes, flipper_width):
    if flipper_width > pancakes.len():
        return 'IMPOSSIBLE'
    i = 0
    while not pancakes.is_happy():
        position = pancakes.find_next_flip_position(flipper_width)
        if position is None:
            return 'IMPOSSIBLE'
        pancakes.flip(flipper_width, position)
        eprint(pancakes)
        i = i + 1
    else:
        return i

def main():
    t = int(input())
    for i in range(1, t + 1):
        #eprint(str(i))
        pancakes_str, flipper_width = [s for s in input().split(" ")]
        pancakes = Pancakes(pancakes_str)
        val = solve(pancakes, int(flipper_width))
        print("Case #{}: {}".format(i, val))

if __name__ == "__main__":
    main()
