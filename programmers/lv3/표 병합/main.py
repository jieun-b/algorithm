from collections import defaultdict

def solution(commands):
    answer = []
    table = [['EMPTY']*51 for _ in range(51)]
    parents = [[(r, c) for c in range(51)] for r in range(51)]
    
    def find(r, c):
        pr, pc = parents[r][c]
        if (pr, pc) != (r, c):
            parents[r][c] = find(pr, pc)  # 재귀로 루트 갱신 (경로 압축)
        return parents[r][c]
    
    def update_all(r, c, value):
        root = find(r,c)
        for i in range(51):
            for j in range(51):
                if find(i, j) == root:   
                    table[i][j] = value
        
    def merge(r1, c1, r2, c2):
        # 두 셀을 병합하는 것은 두 그룹을 병합하는 것과 같음
        # 각 그룹의 루트를 구한 뒤 두번째 그룹의 루트를 첫번째 그룹의 루트를 부모로 가지도록 설정
        root1 = find(r1, c1)
        root2 = find(r2, c2)
        if root1 == root2:
            return
        
        r1_root, c1_root = root1
        r2_root, c2_root = root2
        
        if table[r1_root][c1_root] == 'EMPTY' and table[r2_root][c2_root] != 'EMPTY':
            value = table[r2_root][c2_root]
        else:
            value = table[r1_root][c1_root]
            
        parents[r2_root][c2_root] = root1
        update_all(r1_root, c1_root, value) 
    

    def unmerge(r, c):
        # 해당 그룹의 루트 찾기
        root = find(r, c)
        to_unmerge = []
        for i in range(51):
            for j in range(51):
                # 해당 루트를 가지는 셀을 자기 자신을 루트로 하게 수정, 값도 초기화
                if find(i, j) == root: 
                    to_unmerge.append((i, j))  
                    
        for (i, j) in to_unmerge:            
            parents[i][j] = (i, j) 
            table[i][j] = 'EMPTY'
        
    for command in commands:
        command = list(command.split())
        if command[0] == 'UPDATE':
            if len(command) == 4: # "UPDATE r c value"
                r, c, value = int(command[1]), int(command[2]), str(command[3])
                # 해당 위치 값을 바꿀 때 병합된 셀인 경우 모든 값을 수정해야 함
                update_all(r,c,value)
            else: # "UPDATE value1 value2"
                value1, value2 = str(command[1]), str(command[2])
                for r in range(51):
                    for c in range(51):
                        if table[r][c] == value1:
                            table[r][c] = value2
        elif command[0] == 'MERGE':
            r1, c1, r2, c2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
            merge(r1, c1, r2, c2)
        elif command[0] == 'UNMERGE':
            r, c = int(command[1]), int(command[2])
            value = table[r][c]
            unmerge(r, c)
            table[r][c] = value
        elif command[0] == 'PRINT':
            r, c = int(command[1]), int(command[2])
            answer.append(table[r][c])
    return answer