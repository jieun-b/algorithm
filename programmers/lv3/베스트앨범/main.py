from collections import defaultdict

def solution(genres, plays):
    answer = []
    musics = defaultdict(list)
    cnt = defaultdict(int)
    for i in range(len(genres)):
        musics[genres[i]].append([plays[i], i])
        cnt[genres[i]] += plays[i]
    
    cnt = list(cnt.items())
    cnt.sort(key=lambda x: (-x[1], x[0]))
    for genre in cnt:
        music_list = musics[genre[0]]
        if len(musics[genre[0]]) == 1:
            answer.append(music_list[0][1])
        else:
            music_list.sort(key=lambda x: (-x[0], x[1]))
            answer.append(music_list[0][1])
            answer.append(music_list[1][1])
    return answer