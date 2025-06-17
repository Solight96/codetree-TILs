text = input()
pattern = input()


def start_index(a, b):
    for i in range(len(text)):
        is_partial = True
        if b[0] == a[i]:
            for j in range(1, len(pattern)):
                if i+j >= len(text) or b[j] != a[i+j]:
                    is_partial = False
                    break
            if is_partial:
                return i
    return -1

si = start_index(text, pattern)
print(si)