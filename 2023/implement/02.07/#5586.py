string = input()
JOI = 0
IOI = 0

for i in range(len(string)-2):
    answer = ''
    answer += string[i] + string[i+1] + string[i+2] #3글자가!
    
    if answer == 'JOI':
        JOI += 1
    if answer == 'IOI':
        IOI += 1
        
print(JOI)
print(IOI)