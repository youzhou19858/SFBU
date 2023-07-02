import collections
import heapq


def networkDelayTime(times, n, k):
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    # Priority queue: [(time_cost, node)]
    queue = [(0, k)]
    dist = {node: float('inf') for node in range(1, n+1)}
    dist[k] = 0

    while queue:
        time_cost, node = heapq.heappop(queue)

        if time_cost != dist[node]:
            continue

        for v, w in graph[node]:
            if time_cost + w < dist[v]:
                dist[v] = time_cost + w
                heapq.heappush(queue, (dist[v], v))

    max_delay = max(dist.values())
    return max_delay if max_delay < float('inf') else -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2

print(networkDelayTime(times, n, k))
