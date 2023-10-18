'''segunda parte guia 7'''


# 1.
def ceros(nums: list) -> list:
    idx = 0
    while idx < len(nums):
        if nums[idx] % 2 == 0:
            nums.insert(idx, 0)
            nums.pop(idx + 1)
            idx += 1
        else:
            idx += 1
    print(nums)
    return nums


# 2.
def ceros2(numes: list) -> list:
    nums = numes
    idx = 0
    while idx < len(nums):
        if nums[idx] % 2 == 0:
            nums.insert(idx, 0)
            nums.pop(idx + 1)
            idx += 1
        else:
            idx += 1
    print(nums)
    return nums
