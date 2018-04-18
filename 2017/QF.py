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
        new_pancakes = Pancakes(self)
        for i in range(position, position + flipper_width):
            new_pancakes.cakes[i] = not new_pancakes.cakes[i]
        return new_pancakes

    def find_next_flip_position(self, flipper_width):
        times = len(self.cakes) // flipper_width
        for time in range(1, times + 1):
            for position in range(0, len(self.cakes) - flipper_width * time + 1):
                next = self.flip(flipper_width * time, position)
                #eprint(next)
                #eprint(str(self.border_count()) + "->" + str(next.border_count()))
                if self.border_count() - next.border_count() == 2 and self.happy_count() - next.happy_count() < flipper_width * time :
                    return position
        return None


    def border_count(self):
        last = True
        count = 0
        for c in self.cakes:
            if c != last:
                count += 1
                last = c
        if not self.cakes[len(self.cakes) - 1]:
            count += 1
        return count

    def happy_count(self):
        return self.cakes.count(True)

    def len(self):
        return len(self.cakes)


def iter(pancakes, flipper_width, current_flip_times):
    position = pancakes.find_next_flip_position(flipper_width)
    if position is None:
        return 'IMPOSSIBLE'
    new_pancakes = pancakes.flip(flipper_width, position)
    #eprint(new_pancakes)
    if new_pancakes.is_happy():
        return current_flip_times + 1
    else:
        return iter(new_pancakes, flipper_width, current_flip_times + 1)

def solve(pancakes, flipper_width):
    if pancakes.is_happy():
        return 0
    if flipper_width > pancakes.len():
        return 'IMPOSSIBLE'
    return iter(pancakes, flipper_width, 0)

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
