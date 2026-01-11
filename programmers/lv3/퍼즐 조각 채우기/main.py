from collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def find_blocks(board, flag):
    blocks = []
    n = len(board)
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] == flag:
                visited[i][j] = True
                queue = deque([(i,j)])
                block = [(i,j)]
                while queue:
                    r, c = queue.popleft()
                    for k in range(4):
                        nr, nc = r+dr[k], c+dc[k]
                        if 0<=nr<n and 0<=nc<n:
                            if not visited[nr][nc] and board[nr][nc] == flag:
                                block.append((nr,nc))
                                queue.append((nr,nc))
                                visited[nr][nc] = True
                blocks.append(block)
    return blocks

def normalize_block(block):
    r, c = zip(*block)
    h, w = max(r) - min(r) + 1, max(c) - min(c) + 1
    normalized_block = [[0]*w for _ in range(h)]
    for i, j in block:
        normalized_block[i-min(r)][j-min(c)] = 1
    return normalized_block

def rotate_block(block, empty_block):
    for k in range(4):
        block = list(map(list, zip(*block[::-1])))
        if block == empty_block:
            return True
    return False
    
def solution(game_board, table):
    answer = 0
    empty_blocks = find_blocks(game_board, 0)
    puzzle_blocks = find_blocks(table, 1)
    # 남은 공간 반복 확인
    for empty_block in empty_blocks:
        cnt = len(empty_block)
        empty_block = normalize_block(empty_block)
        # 퍼즐 확인
        for puzzle_block in puzzle_blocks:
            normalized_block = normalize_block(puzzle_block)
            # 퍼즐 회전
            if rotate_block(normalized_block, empty_block):
                puzzle_blocks.remove(puzzle_block)
                answer += cnt
                break
    return answer