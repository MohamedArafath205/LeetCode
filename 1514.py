class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for (u,v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))

        heap = [(-1.0, start_node)]
        visited = [False] * n

        while heap:
            curr_prob, node = heapq.heappop(heap)
            curr_prob = - curr_prob

            if node == end_node:
                return curr_prob

            if visited[node]:
                continue 
            visited[node] = True

            for neighbour, edge_prob in graph[node]:
                if not visited[neighbour]:
                    heapq.heappush(heap, (-(curr_prob * edge_prob), neighbour))

        return 0.0
