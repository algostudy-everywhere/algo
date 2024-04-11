# 문제 이름 : 방 번호
# 문제 링크 : https://www.acmicpc.net/problem/1475
# 풀이 노트 : https://www.notion.so/do-yoongyo2/BOJ_1475_-18fd7bea7e9c456ca0b5b83c12e9e3c6?pvs=4
#
# 다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.
# 다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다.
# 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오.
# (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)


import math

data = input()  # return <class 'str'>
count_number = {str(i): 0 for i in range(9)}    # 딕셔너리 생성 - 키 : 0부터 8까지/ 밸류 : 모두 0

for character in data:
    if character == "9":
        count_number["6"] += 1
    else:
        count_number[character] += 1

count_number["6"] = math.ceil(count_number["6"] / 2)
print(max(count_number.values()))