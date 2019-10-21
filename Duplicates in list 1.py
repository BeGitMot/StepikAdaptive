nums = [int(i) for i in input().split()]
print (*[n for n in set(nums) if nums.count(n) > 1])



