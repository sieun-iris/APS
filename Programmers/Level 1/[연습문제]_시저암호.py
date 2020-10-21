def solution(s, n):
    cap = ['A', 'B', 'C', 'D', 'E',
           'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']

    low = ['a', 'b', 'c', 'd', 'e',
          'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o',
          'p', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z']

    result = []
    for i in s:
        if i == ' ':
            result.append(' ')
        elif i in cap:
            if cap.index(i) + n >= 26:
                result.append(cap[abs((26 - n) - cap.index(i))])
            else:
                result.append(cap[cap.index(i) + n])
        elif i in low:
            if low.index(i) + n >= 26:
                result.append(low[abs((26 - n) - low.index(i))])
            else:
                result.append(low[low.index(i) + n])

    return "".join(result)