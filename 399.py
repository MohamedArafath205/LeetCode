class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graphRep = defaultdict(dict)
        for (var1, var2), value in zip(equations, values):
            graphRep[var1][var2] = value
            graphRep[var2][var1] = 1/value
            
            def BFS(s,e):
                if s not in graphRep or e not in graphRep:
                    return -1
                queue = deque([(s,1.0)])
                Vset = set()
                while queue:
                    var, value = queue.popleft()
                    Vset.add(var)
                    if (var == e):
                        return value
                    for nebVar in graphRep[var]:
                        if nebVar not in Vset:
                            queue.append((nebVar, value*graphRep[var][nebVar]))
                return -1
            
            result = []
            for q in queries:
                temp = BFS(q[0], q[1])
                result.append(temp)
        return result
