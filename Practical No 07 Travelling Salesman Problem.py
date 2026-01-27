import sys
from functools import lru_cache

def tsp(distance):
    n = len(distance)
    VISITED_ALL = (1 << n) - 1

    @lru_cache(None)
    def dp(mask, pos):
        if mask == VISITED_ALL:
            return distance[pos][0]

        ans = sys.maxsize
        for city in range(n):
            if mask & (1 << city) == 0:
                new_ans = distance[pos][city] + dp(mask | (1 << city), city)
                ans = min(ans, new_ans)
        return ans

    return dp(1, 0)

if __name__ == "__main__":
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    print("Minimum travelling cost:", tsp(dist))
