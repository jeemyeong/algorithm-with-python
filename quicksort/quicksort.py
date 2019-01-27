def partition(nums, low, high):
    pivot = low
    low = low + 1
    while low <= high:
        if nums[high] >= nums[pivot]:
            high -= 1
            continue
        if nums[low] <= nums[pivot]:
            low += 1
            continue
        nums[high], nums[low] = nums[low], nums[high]
        low += 1
        high -= 1
    nums[pivot], nums[high] = nums[high], nums[pivot]
    return high

def helper(nums, low, high):
    if low >= high:
        return
    middle = partition(nums, low, high)
    helper(nums, low, middle-1)
    helper(nums, middle+1, high)

def sort(nums):
    helper(nums, 0, len(nums)-1)
    return nums