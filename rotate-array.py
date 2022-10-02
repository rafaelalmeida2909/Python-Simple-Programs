def rotate ( nums, k) -> None:
    l = len(nums)
    k = k % l
    if l != 1 and k != 0:
        nums[:] = nums[-k:] + nums[:-k]
    return nums
print(rotate([1,2,3,4],2))