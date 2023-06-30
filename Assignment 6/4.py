def find_max_length(nums):
    max_length = 0
    count = 0
    count_dict = {0: -1}

    for i in range(len(nums)):
        count += 1 if nums[i] == 1 else -1

        if count in count_dict:
            max_length = max(max_length, i - count_dict[count])
        else:
            count_dict[count] = i

    return max_length

# Test case
nums = [0, 1]
result = find_max_length(nums)
print(result)
