#A
print(
    len(
        set(
            map(int, input().split())
        )
    )
)

#B
print(
    len(
        set(
            open("input.txt", "r").read().split()
        )
    )
)

#C
print(
    min(
        filter(
            lambda x: x%2==1,
            map(int, input().split())
        )
    )
)

#D
from itertools import repeat
print(
    any(
        map(
            lambda x: int(x()) == 0,
            repeat(input, int(input()))
        )
    )
)

#E
from functools import reduce
print(
    reduce(
        lambda x, y: x*(y**5),
        map(int, ['1']+input().split())
    )
)

#or

from functools import reduce
print(
    reduce(
        lambda x, y: x*y,
        map(int, input().split())
    )**5
)

#F
print(
    *map(
        lambda a, b: (a+b)%2,
        map(int, input().split()),
        map(int, input().split())
    )
)

#G
from itertools import accumulate
print(
    *accumulate(
        map(int, input().split()),
        lambda x, y: x+y
    )
)

#H
from itertools import accumulate
print(
    *accumulate(
        [1]+list(range(1, int(input())+1)),
        lambda x, y: x*y
    )
)

#I
from itertools import permutations
print(
    '\n'.join(
        map(
            ''.join,
            permutations(
                map(
                    str,
                    range(1, int(input())+1)
                )
            )
        )
    )
)

#J
from math import sqrt
print(2,
    *filter(
        lambda num:
        len(list(
            filter(
                lambda i: num%i==0,
                range(3, int(sqrt(num)+1), 2)
            )
        )) == 0,
        range(3, int(input())+1, 2)
    )
)
