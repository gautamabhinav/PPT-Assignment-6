from collections import Counter

def findOriginalArray(changed):
    # Check if the length of the changed array is odd
    if len(changed) % 2 != 0:
        return []

    # Sort the changed array in ascending order
    changed.sort()

    # Create a counter to keep track of the frequency of each element in the changed array
    counter = Counter(changed)

    original = []

    for num in changed:
        # Check if the current number has already been used
        if counter[num] == 0:
            continue

        # Check if the double of the current number is present in the counter
        if counter[2 * num] == 0:
            return []

        # Append the current number to the original array
        original.append(num)

        # Decrement the counters for the current number and its double
        counter[num] -= 1
        counter[2 * num] -= 1

    return original

# Test case
changed = [1, 3, 4, 2, 6, 8]
result = findOriginalArray(changed)
print(result)
