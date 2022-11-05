from collections import defaultdict
def solution(record):
    # d = defaultdict(list)
    id_name = {}
    ans = []
    for i in record:
        s = i.split()
        if len(s) == 3:
            state,id,name = s[0],s[1],s[2]
            id_name[id] = name
        else:
            state,id = s[0],s[1]
    # print(id_name)
    
    for i in record:
        tmp = ''
        s = i.split()
        if len(s) == 3:
            state,id,name = s[0],s[1],s[2]
        else:
            state,id = s[0],s[1]
        
        if state == "Enter":
            tmp = id_name[id]+"님이"+" "+"들어왔습니다."
            ans.append(tmp)
            
        elif state == "Leave":
            tmp = id_name[id]+"님이"+" "+"나갔습니다."
            ans.append(tmp)

    return ans