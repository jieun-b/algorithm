def solution(word):
    answer = 0
    
    dictionary = []
    alphabets = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(cur):
        if len(cur) == 5:
            return
        for alphabet in alphabets:
            dictionary.append(cur+alphabet)
            dfs(cur+alphabet)
            
    dfs('')
    
    answer = dictionary.index(word) + 1
    return answer