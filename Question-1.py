def moveZeroes(nums):
    j = 0  # Pointer to track the position for non-zero elements

    # Iterate through the array
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

    # Fill the remaining positions with zeroes
    while j < len(nums):
        nums[j] = 0
        j += 1
