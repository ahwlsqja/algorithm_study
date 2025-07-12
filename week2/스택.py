stack_list = []


def push_stack(X):
    stack_list.append(X)
    return 

def pop_stack():
    if len(stack_list) == 0:  # 스택이 비어있으면
        print(-1)
    else:
        popped_value = stack_list.pop()
        print(popped_value)
    return

def size_stack():
    print(len(stack_list))
    return 

def empty_stack():
    if len(stack_list) == 0:
        print(1)
    else:
        print(0)

    return 

def top_stack():
    if len(stack_list) == 0:
        print(-1)
    else:
        print(stack_list[len(stack_list)-1])
    return

N = int(input())

for _ in range(N):
    cmd = input()

    if cmd.split(' ')[0] == 'push':
        push_stack(int(cmd.split(' ')[1]))

    elif cmd == 'empty':
        empty_stack()

    elif cmd == 'pop':
        pop_stack()

    elif cmd == 'top':
        top_stack()

    elif cmd == 'size':
        size_stack()