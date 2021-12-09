def lowest_pos(d):
    m = float('inf')
    ans = None
    for k, v in d:
        if v < m:
            ans = k
            m = v
    return ans


graph = dict()
graph['n'] = {'a': 6, 'b': 2}
graph['a'] = {'k': 1}
graph['b'] = {'a': 3, 'k': 5}
graph['k'] = {}
costs = dict()
costs['n'] = 0
costs['a'] = 6
costs['b'] = 2
costs['k'] = float('inf')
parents = dict()
cur = lowest_pos(costs)
while cur is not None:
    negh = graph[cur]
    for i in negh:
