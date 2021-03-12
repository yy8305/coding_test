# 문제
# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
#
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
#
# 제한사항
# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.

# 정답
def solution(genres, plays):
    # genres : 노래 장르
    # plays : 노래 재생된 횟수

    # 장르별로 더하기 (장르별로 재생된 횟수 구하기)
    total_music = dict()
    for gp in list(zip(genres, plays)):
        if total_music.get(gp[0]):
            total_music[gp[0]] = total_music.get(gp[0]) + gp[1]
    else:
        total_music[gp[0]] = gp[1]

    # 장르별로 재생된 횟수 리스트로 만들기
    total_list = list(map(lambda x: total_music[x], genres))
    # 노래별로 id 만들기 (순서대로)
    gp_idx = list(map(lambda x: x, range(0, len(genres))))
    # (장르, 횟수, id, 총재생횟수)를 한번에 묶기
    music = list(zip(genres, plays, gp_idx, total_list))

    # 아래 조건순으로 정렬
    # 1. 제일 많이 재생된 장르순으로
    # 2. 재생 횟수순으로
    # 3. id 순으로
    music = sorted(music, key=(lambda x: (-x[3], -x[1], x[2])))
    new_music = []
    for m in music:
        # 장르당 2개씩 추가하기
        if (len(list(filter(lambda x: x[0] == m[0], new_music))) < 2):
            new_music.append(m)

    answer = list(map(lambda x: x[2], new_music))
    return answer

result = solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
print(result)

# 뻘짓
def testcase1(genres, plays):
    # genres : 노래 장르
    # plays : 노래 재생된 횟수

    music_arr = list()

    # 장르, 횟수, id 묶어서 내림차순 정렬
    music = sorted(list(zip(genres, plays, list(map(lambda x: x, range(0, len(genres)))))), key=(lambda x: x[1]),
                   reverse=True)
    count = len(set(genres)) * 2  # 현재 장르 개수 / 장르 중복제거 * 2(장르별로 2개씩 고르니까)
    for key, val, idx in music:
        if count == 0:
            break
        else:
            # 장르별로 두개씩 추가
            if len(list(filter((lambda arr: key in arr), music_arr))) < 2:
                music_arr.append((key, val, idx))
                count -= 1

    idx = 0
    for m in music_arr:
        # 다음항목이 있는지 검사
        if idx + 1 < len(music_arr):
            # 전이랑 다음 항목이 다를 경우
            if (music_arr[idx][0] != music_arr[idx - 1][0] and music_arr[idx][0] != music_arr[idx + 1][0]) or (idx == 0 and music_arr[idx][0] != music_arr[idx + 1][0]):
                idx_val = music_arr[idx + 1]
                if idx + 1 < len(music_arr):
                    for n in range(idx + 1, len(music_arr)):
                        if music_arr[idx][0] == music_arr[n][0]:
                            music_arr[idx + 1] = music_arr[n]
                            music_arr[n] = idx_val
                            if music_arr[idx] == music_arr[idx + 1] and music_arr[idx][1] == music_arr[idx + 1][1] and music_arr[idx][2] > music_arr[idx + 1][2]:
                                idx_val = music_arr[idx + 1]
                                music_arr[idx + 1] = music_arr[idx]
                                music_arr[idx] = idx_val
                            break
            else:
                if music_arr[idx][0] == music_arr[idx + 1][0]:
                    if music_arr[idx][1] < music_arr[idx + 1][1]:
                        idx_val = music_arr[idx]
                        music_arr[idx] = music_arr[idx + 1]
                        music_arr[idx + 1] = idx_val
                    elif music_arr[idx][1] == music_arr[idx + 1][1] and music_arr[idx][2] > music_arr[idx + 1][2]:
                        idx_val = music_arr[idx]
                        music_arr[idx] = music_arr[idx + 1]
                        music_arr[idx + 1] = idx_val
        idx += 1

    print(music_arr)