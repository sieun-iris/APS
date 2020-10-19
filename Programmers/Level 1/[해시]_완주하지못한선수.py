participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']


def solution(participant, completion):
    participant.sort()
    completion.sort()

    if participant[-1] != completion[-1]:
        return participant[-1]
    else:
        for i in range(len(completion)):
            if participant[i] != completion[i]:
                return participant[i]