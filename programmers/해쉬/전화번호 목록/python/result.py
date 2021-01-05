#정답
def solution2(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

#정답
def solution(phone_book):
    """
        - phone_book의 길이는 1 이상 1,000,000 이하입니다.
        - 각 전화번호의 길이는 1 이상 20 이하입니다.

        (sorting 했기 때문에 이중 for문 불필요... 지금 항목과 다음 항목만 비교하면 될듯..)

        return: boolean
    """
    phone_book.sort()

    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i != j:
                if phone_book[i][:len(phone_book[j])] == phone_book[j]:
                    return False
    return True

if __name__ == "__main__":
    print(solution(['12','12']))
    print(solution(['119', '97674223', '1195524421']))
    print(solution(['123','456','789','12356']))
    print(solution(['12','123','1235','567','88']))
    print(solution(["113", "44", "4544"]))





