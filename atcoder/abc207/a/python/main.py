list_num = list(map(int, input().split()))
list_num.sort()
nums = list_num[-2:]
print(nums[0] + nums[1])
