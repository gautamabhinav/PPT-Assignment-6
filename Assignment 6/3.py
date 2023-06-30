def valid_mountain_array(arr):
    if len(arr) < 3:
        return False

    i, n = 0, len(arr) - 1

    while i < n and arr[i] < arr[i + 1]:
        i += 1

    if i == 0 or i == n:
        return False

    while i < n and arr[i] > arr[i + 1]:
        i += 1

    return i == n

# Test case
arr = [2, 1]
result = valid_mountain_array(arr)
print(result)
