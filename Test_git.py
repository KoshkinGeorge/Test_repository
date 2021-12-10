def lowest_pos(d):
    m = float('inf')
    ans = None
    for k, v in d.items():
        if v < m and k not in checked:
            ans = k
            m = v
    return ans


checked = set()
graph = dict()
graph['a'] = {'b': 1, 'c': 5}
graph['b'] = {'c': 6, 'f': 2, 'g': 10, 'e': 3}
graph['c'] = {'d': 7}
graph['d'] = {'f': 1}
graph['e'] = {'g': 8, 'h': 4}
graph['f'] = {'g': 5}
graph['h'] = {'g': 3}
costs = dict()
costs['a'] = 0
costs['b'] = 1
costs['c'] = 5
costs['d'] = float('inf')
costs['e'] = float('inf')
costs['f'] = float('inf')
costs['h'] = float('inf')
costs['g'] = float('inf')
cur = lowest_pos(costs)
while cur is not None:
    for k, v in graph[cur].items():
        if costs[k] > costs[cur] + graph[cur][k]:
            costs[k] = costs[cur] + graph[cur][k]
    checked.add(cur)
    cur = lowest_pos(costs)
    if cur == 'g':
        break
print('Easiest way: ', costs['g'])
