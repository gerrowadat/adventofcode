#!/usr/bin/env python3

class Graph(object):
    def __init__(self):
        # edges
        self._g = {}
        # paths through
        self._p = []

    def add_edge(self, a, b):
        if a not in self._g:
            self._g[a] = [b]
        else:
            self._g[a].append(b)

    def _paths_from(self, node):
        valid = list(self._g.get(node, []))
        valid.extend([x for x in self._g.keys() if node in self._g[x]])
        return valid

    def all_paths(self):
        visited = {}
        self._findpath('start', visited, [])
        return self._p

    def _findpath(self, this, visited, path):
        v = visited.get(this, 0)
        visited[this] = v + 1
        path.append(this)
        if this == 'end':
            self._p.append(list(path))
        else:
            for i in self._paths_from(this):
                # We can only visit small caves once.
                if i.islower() and visited.get(i, 0) > 0:
                    # We can visit this cave again if no other small cave has been visited twice.
                    if i in ('start', 'end') and visited.get(i, 0):
                        continue
                    if 2 in [visited[x] for x in visited.keys() if x.islower()] and i != 'end' :
                        continue
                self._findpath(i, visited, path)
        path.pop()
        visited[this] = visited[this] - 1


def main():
    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    g = Graph()

    for l in lines:
        (start, end) = l.split('-')
        g.add_edge(start, end)

    all_p = g.all_paths()

    for p in all_p:
        print(','.join(p))


if __name__ == '__main__':
    main()
