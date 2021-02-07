def test1(clothes):
    """
    14.3점..
    """
    answer = 0
    cnt_arr = {}
    for cloth in clothes:
        if cloth[1] in cnt_arr:
            cnt_arr[cloth[1]] = cnt_arr[cloth[1]] + 1
        else:
            cnt_arr[cloth[1]] = 1

    cnt_arr = sorted(cnt_arr.items(), key=(lambda x: x[1]))
    idx = 1
    for cnt in cnt_arr:
        answer += cnt[1] * idx
        idx += 1

    return answer


def solution(clothes):
    answer = 0

    cnt_arr = {}
    for cloth in clothes:
        if cloth[1] in cnt_arr:
            cnt_arr[cloth[1]] = cnt_arr[cloth[1]] + 1
        else:
            cnt_arr[cloth[1]] = 1

    for cnt in cnt_arr:
        if answer == 0:
            answer = cnt_arr[cnt]
        else:
            answer *= cnt_arr[cnt]

    for i in reversed(range(1, len(cnt_arr)+1) ):
        print(i)
    if len(cnt_arr) > 1:
        answer += len(clothes)

    return answer


if __name__ == "__main__":
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["green_sunglasses", "eyewear"]]))

    print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"], ["green_turban", "headgear"]]))

    print(solution([["crow_mask", "face"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["blue_tur", "sd"], ["gr_turban", "cxv"]]))