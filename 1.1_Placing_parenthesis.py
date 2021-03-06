def check(_str):
    result = []
    opening = "([{"
    closing = ")]}"
    numbers = []
    for i in range(len(_str)):
        if _str[i] not in opening and _str[i] not in closing:
            continue
        else:
            if _str[i] in opening:
                result.append(_str[i])
                numbers.append(i + 1)
            else:
                if len(result) == 0:
                    return i + 1
                top = result.pop()
                numbers.pop()
                if (top == "(" and _str[i] != ")") or \
                        (top == "[" and _str[i] != "]") \
                        or (top == "{" and _str[i] != "}"):
                    return i + 1

    if len(result) == 0:
        return "Success"
    else:
        return numbers[-1]


assert check("{}([]") == 3
assert check("(((((((((((((((()))") == 13
assert check("([]") == 1
assert check("]]]") == 1
assert check("([](){([])})") == "Success"
assert check("()[]}") == 5
assert check("{{[()]]") == 7
assert check("{{{[][][]") == 3
assert check("{*{{}") == 3
assert check("[[*") == 2
assert check("{*}") == "Success"
assert check("{{") == 2
assert check("{}") == "Success"
assert check("") == "Success"
assert check("}") == 1
assert check("*{}") == "Success"
assert check("{{{**[][][]") == 3


def check_2(s):
    a = []
    for i, c in enumerate(s):
        if c in '([{':
            a += [(i + 1, c)]
        elif c in ')]}' and (a == [] or c != {'[': ']', '(': ')', '{': '}'}[a.pop()[1]]):
            return i + 1
    return "Success" if a == [] else a[-1][0]


print(check_2(input()))
