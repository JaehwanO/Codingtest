def solution(files):
    answer = []
    for file in files:
        left = 0 
        while left < len(file):
            if file[left].isdigit():
                break 
            left += 1
        right = left 
        while right < len(file):
            if not file[right].isdigit():
                break 
            right += 1
        head = file[:left]
        number = file[left:right]
        tail = file[right:]
        answer.append([head, number, tail])
    answer.sort(key = lambda x : (x[0].lower(), int(x[1])))
    answer = ["".join(i) for i in answer]
    return answer