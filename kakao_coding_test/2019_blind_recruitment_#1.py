def solution(N, stages):
    failure_rate = {}
    stages_len = len(stages)

    for i in range(1, N+1):
        if stages_len != 0:
            stage_count = stages.count(i)
            failure_rate[i] = stage_count/stages_len
            stages_len -= stage_count
        else:
            failure_rate[i] = 0

    answer = sorted(failure_rate.keys(), key=lambda key: failure_rate[key], reverse=True)

    return answer