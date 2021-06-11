import sys
sys.stdin = open("input.txt", "r")

diary = list(input())

for idx, i in enumerate(diary, 1):
    diary_dict = {idx: i}

    key_list = []
    if 'p' in diary_dict.values():
        key_list += diary_dict.keys()

    for j in key_list:
        print(j)
        # j는 input값 중 p의 위치값들 (p의 위치값을 뽑는것까지는 했는데, 이를 가지고 연산하는 법을 모르겠음)
        # 이 위치값-1의 i가 위치값+1의 i와 동일할 경우(즉, p의 앞 뒤 값이 같은 경우)를 찾아내고 싶음

        # 처음에는 p를 찾기 위해 index를 쓰고자 했는데, 그러면 가장 앞에 나오는 p값의 위치만 출력됨 (뒤에 나오는 p의 위치값은 안나옴)
        # 때문에 enumerate를 사용했는데 애초에 이게 맞는 접근인지도 잘 모르겠음


