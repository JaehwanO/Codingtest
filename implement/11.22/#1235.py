n = int(input())
nums = []
for _ in range(n):
    nums.append((input()[::-1]))

# print(nums)

k = 0
for _ in range(len(nums[0])):
        duplicated = []
        for i in range(n):
            if nums[i][:k+1] not in duplicated:
                duplicated.append(nums[i][:k+1])
            else:
                k += 1
                break

            # print(duplicated)
print(k+1)