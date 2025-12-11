from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    d = [(0,1), (0,-1), (-1,0), (1,0)]
    queue = deque([(characterX, characterY, 0)])
    visited = set([(characterX, characterY)])

    def is_edge(x, y, lx, ly, rx, ry):
        if (x == lx or x == rx) and ly <= y <= ry:
            return True
        if (y == ly or y == ry) and lx <= x <= rx:
            return True
        return False
    
    def is_valid(x, y, nx, ny):
        # 조건 1
        for lx, ly, rx, ry in rectangle:
            if lx < nx < rx and ly < ny < ry:
                return False
        # 조건 2 
        for lx, ly, rx, ry in rectangle:
            if rx - lx == 1:
                if y == ny and ly < ny < ry:
                    if((lx == x and rx == nx) or (lx == nx and rx == x)):
                        return False
            elif ry - ly == 1:
                if x == nx and lx < nx < rx:
                    if((ly == y and ry == ny) or (ly == ny and ry == y)):
                        return False
        # 조건 3
        cnt = 0
        for lx, ly, rx, ry in rectangle:
            if is_edge(x, y, lx, ly, rx, ry) and is_edge(nx, ny, lx, ly, rx, ry):
                cnt += 1
            
        if cnt != 1:
            return False
        return True
        
    while queue:
        x, y, dis = queue.popleft()
        if (x, y) == (itemX, itemY):
            return dis 
        for k in range(4):
            nx, ny = x+d[k][0], y+d[k][1]
            if 0<nx<=50 and 0<ny<=50 and (nx, ny) not in visited:
                if is_valid(x, y, nx, ny):
                    queue.append((nx, ny, dis+1))
                    visited.add((nx, ny))
        
    return answer