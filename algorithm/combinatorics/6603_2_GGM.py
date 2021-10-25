# -*- coding: utf-8 -*-
# 속도를 더 빠르게 하기 위한 여러가지를 더 시도

import time
from sys import stdin, stdout
from array import array


def dfs(S, visited):
    # 가지 치기: 오름차순이 아닌 경우
    if len(visited) > 1:
        if visited[-1] < visited[-2]:
            return

    # 기저 사례: 끝까지 방문한 경우
    if len(visited) == 6:
        #  stdout.write(" ".join(map(str, visited)) + "\n")
        return

    # 완전 탐색
    for s in S:
        if s in visited:
            continue

        visited.append(s)
        dfs(S, visited)
        visited.pop()


def dfs_with_array(S, visited, depth):
    if depth > 1:
        if visited[depth - 1] < visited[depth - 2]:
            return

    if depth == 6:
        #  stdout.write(" ".join(map(str, visited)) + "\n")
        return

    for s in S:
        if s in visited:
            continue

        temp = visited[depth]
        visited[depth] = s
        dfs_with_array(S, visited, depth + 1)
        visited[depth] = temp


def dfs_within_for(S, visited):
    # 기저 사례: 끝까지 방문한 경우
    if len(visited) == 6:
        #  stdout.write(" ".join(map(str, visited)) + "\n")
        return

    # 완전 탐색
    for s in S:
        if s in visited:
            continue

        # 가지 치기
        if len(visited) > 0:
            if s < visited[-1]:
                continue

        visited.append(s)
        dfs_within_for(S, visited)
        visited.pop()


def dfs_with_o1visitied(S, path, visited):
    # 가지 치기: 오름차순이 아닌 경우
    if len(path) > 1:
        if path[-1] < path[-2]:
            return

    if len(path) == 6:
        #  stdout.write(" ".join(map(str, path)) + "\n")
        return

    for s in S:
        if visited[s]:
            continue

        visited[s] = 1
        path.append(s)
        dfs_with_o1visitied(S, path, visited)
        path.pop()
        visited[s] = 0


if __name__ == "__main__":
    MIS = lambda: map(int, stdin.readline().split())

    #  K, *S = MIS()
    #  visited = []
    #
    #  while K != 0:
    #      dfs(K, S, visited)
    #      K, *S = MIS()
    #      stdout.write("\n")

    e_K, e_S = 20, [i for i in range(1, 21)]

    # (1)
    visited = []
    s_time = time.time()
    dfs(e_S, visited)  # 기존 방법
    d_time = time.time() - s_time
    print(f"실행 시간: {d_time}")

    # (2) - (1) + Depth => 더 느려짐, depth가 더 메모리를 잡아먹어서?
    visited = array("b", [0] * 6)
    s_time = time.time()
    dfs_with_array(e_S, visited, 0)  # Visited 배열로 선언
    d_time = time.time() - s_time
    print(f"실행 시간: {d_time}")

    # (3) - (1) + 가지치기를 내부에서 수행
    visited = []
    s_time = time.time()
    dfs_within_for(e_S, visited)  # 기존 방법
    d_time = time.time() - s_time
    print(f"실행 시간: {d_time}")

    # (4) - Visited 복잡도를 O(1)로 수행하게
    # 기존 복잡도가 거의 O(1)에 가까워서 크게 의미가 없었던 것 같다.
    visited = array("b", [0] * 49)  # 독일 로또번호는 49까지
    path = []
    s_time = time.time()
    dfs_with_o1visitied(e_S, path, visited)  # 기존 방법
    d_time = time.time() - s_time
    print(f"실행 시간: {d_time}")
