from collections import deque

friends = deque(("Agrima", "Shruti", "Meghna", "Meher"))

def get_friend():
    yield from friends

def greet(g):
    while True:
        try:
            val = next(g)
            yield f"Hello {val}"
        except StopIteration:
            pass

friends_gene = get_friend()
g = greet(friends_gene)
print(next(g)) # Agrima
print(next(g)) # Shruti