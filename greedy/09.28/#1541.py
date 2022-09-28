s = list(input().split('-'))
res = 0
nums = []
# print(s)
for i in s:
  num = i.split("+")
  x = 0
  for j in num:
    x += int(j)

  nums.append(x)
res = nums[0]
# print(nums)
for i in range(1,len(nums)):
  res -= nums[i]

print(res)
