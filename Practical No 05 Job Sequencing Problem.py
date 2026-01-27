from typing import List, Tuple


def jobSequencing(deadline: List[int], profit: List[int]) -> List[int]:
    n = len(deadline)
    cnt = 0
    totProfit = 0

    jobs = [(profit[i], deadline[i]) for i in range(n)]

    jobs.sort(key=lambda x: x[0], reverse=True)

    slot = [0] * n
    for i in range(n):
        start = min(n, jobs[i][1]) - 1
        for j in range(start, -1, -1):

            if slot[j] == 0:
                slot[j] = 1
                cnt += 1
                totProfit += jobs[i][0]
                break

    return [cnt, totProfit]


if __name__ == "__main__":
    deadline = [2, 1, 2, 1, 1]
    profit = [100, 19, 27, 25, 15]
    ans = jobSequencing(deadline, profit)
    print(ans[0], ans[1])
