class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1- y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        visited = set()
        res = 0
        minHeap = [[0,0]]
        while len(visited) < n:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for nxtcost, node in adj[i]:
                if node not in visited:
                    heapq.heappush(minHeap, [nxtcost, node])

        return res
