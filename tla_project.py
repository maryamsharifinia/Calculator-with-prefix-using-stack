
def faz_1(s):
    list_s = []
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    index = 0
    for i in range(0, len(s)):
        if index >= len(s):
            break
        i = index
        if s[i] == ' ':
            index += 1
            continue
        op = ''
        if s[i] in nums:
            j = i
            while s[j] in nums:
                op += s[j]
                j += 1
            index = j
            list_s.append(int(op))

        else:
            index += 1
            op = s[i]
            list_s.append(op)

    return list_s


def operatorpriority(x):
    if x in "+-":
        return 1
    elif x in "*/":
        return 2
    elif x in "^":
        return 3
    return 0


def faz_2(input):
    stack = []
    output = []
    for c in input[::-1]:
        if type(c) == int:
            output.append(c)
        elif c == ")":
            stack.append(c)
        elif c in "+-*/^":
            if c == "^":
                while operatorpriority(c) <= operatorpriority(stack[-1]):
                    output.append(stack.pop())
            else:
                while operatorpriority(c) < operatorpriority(stack[-1]):
                    output.append(stack.pop())
            stack.append(c)
        elif c == "(":
            while not len(stack) == 0:
                c1 = stack.pop()
                if c1 == ')':
                    break
                output.append(c1)
    while not len(stack) == 0:
        output.append(stack.pop())
    return output

def faz_3(tokens):
    stack = []
    for t in tokens:
        if t == '+':
            stack[-2:] = [stack[-1] + stack[-2]]
        elif t == '-':
            stack[-2:] = [stack[-1] - stack[-2]]
        elif t == '*':
            stack[-2:] = [stack[-1] * stack[-2]]
        elif t == '/':
            stack[-2:] = [stack[-1] / stack[-2]]
        else:
            stack.append(t)
    assert len(stack) == 1, 'Malformed expression'
    return stack[0]


if __name__ == '__main__':
    calc = faz_1("(2*2-(3/4) + 3)")
    tokens = faz_2(calc)
    print(faz_3(tokens))
