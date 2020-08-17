import sys
sys.stdin = open("1284_input.txt", "r")

T = int(input())

result = []
for t in range(T):
    a_cost = 0
    b_cost = 0
    P, Q, R, S, W = map(int, input().split())
    a_cost = P*W
    if W < R:
        b_cost = Q
    else:
        b_cost = Q + (W-R) *S
    result = [a_cost] + [b_cost]
    print('#{} {}'.format(t+1, min(result)))



    # print(result)


# a_cost = []
# b_cost = []
# for i in cost_list:
#     for j in cost_list:
#         a_cost = cost_list[4] * cost_list[0]
#
#         if cost_list[4] < cost_list[2]:
#             b_cost = cost_list[1]
#         else:
#             b_cost = cost_list[1] + (cost_list[4]-cost_list[2])*1


# if a_cost < b_cost:
#     print('#{} {}'.format(i, a_cost))
# else:
#     print(b_cost)







