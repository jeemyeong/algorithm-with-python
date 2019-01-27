def partition1(nums, low, high):
    pivot = low
    low += 1
    while low <= high:
        if nums[low] <= nums[pivot]:
            low += 1
            continue
        if nums[high] >= nums[pivot]:
            high -= 1
            continue
        nums[high], nums[low] = nums[low], nums[high]
        low += 1
        high -= 1
    nums[pivot], nums[high] = nums[high], nums[pivot]
    return high

def partition2(nums, low, high):
    pivot = high
    high -= 1
    while low <= high:
        if nums[low] <= nums[pivot]:
            low += 1
            continue
        if nums[high] >= nums[pivot]:
            high -= 1
            continue
        nums[high], nums[low] = nums[low], nums[high]
        low += 1
        high -= 1
    nums[pivot], nums[low] = nums[low], nums[pivot]
    return low

def helper(nums, low, high, partition):
    if low >= high:
        return
    middle = partition(nums, low, high)
    helper(nums, low, middle-1, partition)
    helper(nums, middle+1, high, partition)

def sort(nums, partition):
    helper(nums, 0, len(nums)-1, partition)
    return nums