# -*- coding: utf-8 -*-
# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

from array import array
from sys import stdin, stdout


class Stack:
    def __init__(self):

        self._arr = array("i", [0] * 10001)  # i == sint16
        self._top = -1

    def push(self, x):
        self._top += 1
        self._arr[self._top] = x

    def pop(self):
        if self.is_empty():  # 편의를 위해 empty 미사용
            stdout.write("-1" + "\n")
            return

        self.top()
        self._top -= 1

    def size(self):
        stdout.write(str(self._top + 1) + "\n")

    def empty(self):
        stdout.write(str(int(self._top == -1)) + "\n")

    def is_empty(self):
        return self._top == -1

    def top(self):
        if self.is_empty():  # 편의를 위해 empty 미사용
            stdout.write("-1" + "\n")
            return

        stdout.write(str(self._arr[self._top]) + "\n")


if __name__ == "__main__":
    MIS = lambda x: x.split(" ")
    N = int(stdin.readline())
    s = Stack()

    for _ in range(N):
        command = MIS(stdin.readline().rstrip("\n"))

        if command[0] == "push":
            sint = int(command[1])
            getattr(s, command[0])(sint)
            continue

        getattr(s, command[0])()
