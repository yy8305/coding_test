import time

start = time.time()

def test1(participant, completion):
    """
        정확성: 50.0
        효율성: 0.0
        합계: 50.0 / 100.0

        0.0009970664978027344
    """

    for comp in completion:
        participant.remove(comp)

    answer = participant[0]
    return answer

def test2(participant, completion):
    """
        정확성: 40.0
        효율성: 40.0
        합계: 80.0 / 100.0
    """

    answer = set(participant) - set(completion)

    return ((answer == set()) and list([c for c in completion if participant.count(c) > 1])[0] or answer.pop())

def test3(participant, completion):
    """
        정확성: 50.0
        효율성: 40.0
        합계: 90.0 / 100.0

        0.0010008811950683594
    """

    answer = set(participant) - set(completion)

    if(answer == set()):
        for i in completion:
            participant.remove(i)

    return ((answer == set()) and participant[0] or answer.pop())

def test4(participant, completion):
    """
        정확성: 50.0
        효율성: 50.0
        합계: 100.0 / 100.0

        0.00099945068359375
    """

    participant.sort()
    completion.sort()

    for p,c in zip(participant,completion):
        if p != c:
            return p

    return participant[-1]

#정답
def solution(participant, completion):
    """
        참여한 선수(array) = participant (participant >= 1, participant <= 100000)
        완주한 선수(array) = completion ( len(completion) == len(participant) -1 )
        etc) 동명이인 있음, 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자
        return = 완주하지 못한 선수
        return: string
    """

    participant.sort()
    completion.sort()

    for p,c in zip(participant,completion):
        if p != c:
            return p

    return participant[-1]


if __name__ == "__main__":
    print(solution(["leo", "kiki", "eden"],["eden", "kiki"])) # 결과: leo
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"])) # 결과: vinko
    print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])) # 결과: mislav

    print("time :", time.time() - start)