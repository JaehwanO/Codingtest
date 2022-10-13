import sys
from collections import Counter

n = int(sys.stdin.readline())  # 학생 수
arr = list(map(int, sys.stdin.readline().split()))  # 학생 코딩 실력
arr.sort()
cnt_ = Counter(arr)  # 해당 점수에 해당하는 학생 수 얻기 
result = 0
# 학생을 한명 씩 돌린다.
for i, a in enumerate(arr):
    left, right = i + 1, n - 1
    while left < right:
        sum_ = arr[left] + arr[right] + arr[i]
        # 1. 점수 총합이 0인 경우, 같은 값이 있는 것에 대한 처리 필요
        if sum_ == 0:
            # 연속적으로 나오는 경우 처리
            #  left값과 right 갑이 같은 경우 해당 범위 저장. -4 -4 2 2 2 
            if arr[left] == arr[right]:
                result += right - left
                        # 다른 경우 right 값에 대한 개수 합
            else: 
                result += cnt_[arr[right]]
            left += 1
                # 2. 점수 총합이 0 보다 큰 경우 
        elif sum_ > 0:
            right -= 1
                # 3. 점수 총합이 0 보다 작은 경우
        elif sum_ < 0:
            left += 1

print(result)