# -*- coding: utf-8 -*-
# 49개의 숫자중 k(k > 6)개의 숫자를 골라 집합 S를 만든 다음 만들 수 있는 경우의 수를 출력
# S는 오름차순으로 주어진다.

from sys import stdin, stdout


def dfs(K, S, visited):
    # 가지 치기: 오름차순이 아닌 경우
    if len(visited) > 1:
        if visited[-1] < visited[-2]:
            return

    # 기저 사례: 끝까지 방문한 경우
    if len(visited) == 6:
        stdout.write(" ".join(map(str, visited)) + "\n")
        return

    # 완전 탐색
    for s in S:
        if s in visited:
            continue

        visited.append(s)
        dfs(K, S, visited)
        visited.pop()


if __name__ == "__main__":
    MIS = lambda: map(int, stdin.readline().split(" "))

    K, *S = MIS()
    visited = []

    while K != 0:
        dfs(K, S, visited)
        K, *S = MIS()
        stdout.write("\n")
