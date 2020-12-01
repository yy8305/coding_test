def solution(participant, completion):
    """
        참여한 선수(array) = participant (participant >= 1, participant <= 100000)
        완주한 선수(array) = completion ( len(completion) == len(participant) -1 )
        etc) 동명이인 있음, 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자
        return = 완주하지 못한 선수
        return: string
    """

    for comp in completion:
        participant.remove(comp)

    answer = participant[0]
    return answer