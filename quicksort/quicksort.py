def helper(nums, low, high):
    origin_low = low
    origin_high = high
    n = high - low
    if n <= 1:
        return
    pivot = low
    low = low + 1
    while low <= high:
        if nums[low] > nums[pivot] > nums[high]:
            nums[high], nums[low] = nums[low], nums[high]
            high -= 1
            low += 1
            continue
        if nums[high] >= nums[pivot]:
            high -= 1
            continue
        if nums[low] <= nums[pivot]:
            low += 1
            continue
    nums[pivot], nums[high] = nums[high], nums[pivot]
    middle = high
    helper(nums, origin_low, middle-1)
    helper(nums, middle+1, origin_high)

def sort(nums):
    helper(nums, 0, len(nums)-1)
    return nums