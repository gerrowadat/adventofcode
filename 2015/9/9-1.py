import sys
from itertools import permutations

def main():
    with open(sys.argv[1]) as f:
        lines = [l.strip() for l in f.readlines()]

    cities = set()
    edges = {}

    # Enumerate Edges
    for l in lines:
        (city1, _, city2, _, distance) = l.split(' ')
        cities.add(city1)
        cities.add(city2)
        edges[(city1, city2)] = int(distance)
        edges[(city2, city1)] = int(distance)

    paths = {}

    min_total = None

    for path in permutations(cities):
        total = 0
        for stopnum in range(len(path)-1):
            total += edges[(path[stopnum], path[stopnum+1])]
        if min_total is None or total < min_total:
            min_total = total


    print(min_total)



if __name__ == '__main__':
    main()

