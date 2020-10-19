phone_book = [119, 97674223, 1195524421]


def solution(phone_book):
    a = min(phone_book)
    for i in range(len(phone_book)):
        if phone_book[i] == a:
            pass
        elif a in phone_book[i]:
            return False
    return True

