from typing import Any
from collections import deque

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        visited_roots = list()
        stack = deque([self._root])

        while len(stack) != 0:
            cur_root = stack.popleft()
            if cur_root not in visited_roots:
                visited_roots.append(cur_root)
                vals_for_stack = cur_root.outbound
                vals_for_stack.reverse()
                stack.extendleft(vals_for_stack)

        return visited_roots



    def bfs(self) -> list[Node]:
        visited_roots = list()
        stack = deque([self._root])

        while len(stack) != 0:
            cur_root = stack.popleft()
            if cur_root not in visited_roots:
                visited_roots.append(cur_root)
                vals_for_stack = cur_root.outbound
                stack.extend(vals_for_stack)

        return visited_roots


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)

g = Graph(a)

print(g.bfs())


