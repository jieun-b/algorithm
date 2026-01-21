def solution(name):
    answer = 0
    move = len(name)-1
    for l in range(len(name)):
        answer += min(ord(name[l]) - ord('A'), ord('Z') - ord(name[l]) + 1)
        r = l + 1
        while(r < len(name) and name[r] == 'A'):
            r += 1
        move = min(move, l*2+len(name)-r, l+2*(len(name)-r))
    answer += move
    return answer