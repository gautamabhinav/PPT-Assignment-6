def reconstruct_permutation(s):
    perm = []
    current = 0
    start = len(s)

    for c in s:
        if c == 'I':
            perm.append(current)
            current += 1
        elif c == 'D':
            perm.append(start)
            start -= 1

    perm.append(start)

    return perm

# Test case
s = "IDID"
perm = reconstruct_permutation(s)
print(perm)
