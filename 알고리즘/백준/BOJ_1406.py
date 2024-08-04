import sys


initial_string = sys.stdin.readline().rstrip()
n = int(input())


left_stack = list(initial_string)
right_stack = []

for _ in range(n):
    enter = sys.stdin.readline().rstrip().split()
    if enter[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif enter[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif enter[0] == 'B':
        if left_stack:
            left_stack.pop()
    elif enter[0] == 'P':
        left_stack.append(enter[1])


sys.stdout.write(''.join(left_stack + list(reversed(right_stack))))
