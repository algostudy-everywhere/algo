# 문제 이름 : 그룹 단어 체커
# 문제 링크 : https://www.acmicpc.net/problem/1316
# 풀이 노트 : https://www.notion.so/do-yoongyo2/BOJ_1316_-c4d3281b48ce445cbc17a4a809d5a19c?pvs=4
#
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만,
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.


n = int(input())
data = []

for _ in range(n):
    word = input()
    data.append(word)

cnt = 0

for word in data:
    check_set = set()  # 다시 나오면 안되는 글자들 모음

    # flag(is_bad)를 사용하여 for문이 정상적으로 빠져나온 것인지 break로 인해 나온 것인지 구분
    is_bad = False

    # 한 글자일 경우 무조건 단어로 체킹
    if len(word) == 1:
        cnt += 1
    else:  # 두글자 이상인 단어만 체크하기 시작
        for j in range(1, len(word)):
            if word[j] == word[j-1]:
                continue
            else:
                # 앞글자와 다르기 때문에 해야할 일
                # 1. 앞글자를 check_list에 append 하기
                # 2. 뒷글자를 check_list에 있는지 확인하기
                check_set.add(word[j-1])
                if word[j] in check_set:
                    is_bad = True
                    break
        if not is_bad:
            cnt += 1
print(cnt)