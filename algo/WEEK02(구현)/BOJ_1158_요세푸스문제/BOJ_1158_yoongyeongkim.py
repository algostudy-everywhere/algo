# 문제 이름 : 요세푸스 문제
# 문제 링크 : https://www.acmicpc.net/problem/1158
# 풀이 노트 : https://www.notion.so/do-yoongyo2/BOJ_1158_-7a9656df4d2b4bc49b2eb381a4065fa1?pvs=4

# 요세푸스 문제는 다음과 같다.
# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다.
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
# 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.


# input을 n과 k에 저장
n, k = map(int, input().split())

# 현재 리스트에서 확인할 위치 지정하는 pointer 변수에 -1을 지정하는 이유 :
# pointer에 K를 더했을 때 인덱스 값으로 계산할 경우엔 k보다 -1씩 작아야 한다.
pointer = -1
data = [i for i in range(1, n + 1)]  # 1부터 n+1까지 리스트 생성
result = []

# data의 전체 수
for remaining in range(n, 0, -1):  # n개부터 시작해서 제거되면 -1씩 줄어 듦

    # pointer에 제거할 위치 지정을 위해 k 더하기
    pointer += k

    if pointer < remaining:
        result.append(str(data.pop(pointer)))  # join 함수를 사용하기 위해 str 형변환 해서 append
    else:
        pointer %= remaining
        result.append(str(data.pop(pointer)))

    # 인덱스 값을 고려해서 -1 빼기
    pointer -= 1

print("<" + ", ".join(result) + ">")
