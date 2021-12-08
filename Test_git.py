import random
from collections import deque


graph = deque()
way = dict()
way['a'] = ['b', 'd']
way['c'] = ['d', 'c']
way['b'] = ['c', 'd']
way['d'] = ['a', 'b', 'c', 'd', 'e']
graph += way['a']
checked = dict(zip(('a', 'b', 'c', 'd'), ([False for i in range(4)])))
while graph:
    el = graph.popleft()
    if not checked[el] and 'e' not in way[el]:
        graph += way[el]
        checked[el] = True
    elif 'e' in way[el]:
        graph = []
        print("Finished!")