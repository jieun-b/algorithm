def solution(sizes):
    a, b = 0, 0
    for size in sizes:
        size.sort()
        a = max(a, size[0])
        b = max(b, size[1])
    return a * b