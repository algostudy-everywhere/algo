# 문제 이름 : DNA 비밀번호
# 문제 링크 : https://www.acmicpc.net/problem/12891
# 풀이 노트 : https://www.notion.so/do-yoongyo2/BOJ_12891_DNA-065ced1e4ae145c8939dc67e2e64ad68?pvs=4
#
# 평소에 문자열을 가지고 노는 것을 좋아하는 민호는 DNA 문자열을 알게 되었다.
# DNA 문자열은 모든 문자열에 등장하는 문자가 {‘A’, ‘C’, ‘G’, ‘T’} 인 문자열을 말한다.
# 예를 들어 “ACKA”는 DNA 문자열이 아니지만 “ACCA”는 DNA 문자열이다.
# 이런 신비한 문자열에 완전히 매료된 민호는 임의의 DNA 문자열을 만들고 만들어진 DNA 문자열의 부분문자열을 비밀번호로 사용하기로 마음먹었다.
# 하지만 민호는 이러한 방법에는 큰 문제가 있다는 것을 발견했다.
# 임의의 DNA 문자열의 부분문자열을 뽑았을 때 “AAAA”와 같이 보안에 취약한 비밀번호가 만들어 질 수 있기 때문이다.
# 그래서 민호는 부분문자열에서 등장하는 문자의 개수가 특정 개수 이상이여야 비밀번호로 사용할 수 있다는 규칙을 만들었다.
# 임의의 DNA문자열이 “AAACCTGCCAA” 이고 민호가 뽑을 부분문자열의 길이를 4라고 하자.
# 그리고 부분문자열에 ‘A’ 는 1개 이상, ‘C’는 1개 이상, ‘G’는 1개 이상, ‘T’는 0개 이상이 등장해야 비밀번호로 사용할 수 있다고 하자. 이때 “ACCT” 는 ‘G’ 가 1 개 이상 등장해야 한다는 조건을 만족하지 못해 비밀번호로 사용하지 못한다. 하지만 “GCCA” 은 모든 조건을 만족하기 때문에 비밀번호로 사용할 수 있다.
# 민호가 만든 임의의 DNA 문자열과 비밀번호로 사용할 부분분자열의 길이, 그리고 {‘A’, ‘C’, ‘G’, ‘T’} 가 각각 몇번 이상 등장해야 비밀번호로 사용할 수 있는지 순서대로 주어졌을 때 민호가 만들 수 있는 비밀번호의 종류의 수를 구하는 프로그램을 작성하자. 단 부분문자열이 등장하는 위치가 다르다면 부분문자열이 같다고 하더라도 다른 문자열로 취급한다.


n, m = map(int, input().split())
data = input()
A, C, G, T = map(int, input().split())
check = {"A": A, "C": C, "G": G, "T": T}    # dict 형태로 저장

cnt = 0


# 로직 : 첫 부분문자열을 확인한 뒤 다음 부분문자열과 m-1개가 동일하므로,
# 첫 부분문자열의 0번 문자열과 다음 부분문자열의 마지막 글자인 m번 문자열이 동일한지 비교하고
# 동일하면, is_nice flag가 True인지 체크한 뒤 cnt+1
# 다르면, 0번 문자열은 dict에 1올려주고, m번문자열은 -1을 수행한뒤 -> dict안에 element가 0이상인지 확인하고 플래그 반영
# 주의점 : 전체 data를 슬라이싱하지 않고, 인덱스로만 계산을 하기 때문에 인덱스 번호를 잘 기억해야함

# 1-1. 첫번째 부분문자열인 0-m을 확인
for i in range(0, m):
    check[data[i]] -= 1

# 1-2. 결과값인 check.values에 0이상이 항목이 있으면, 비밀번호 미통과 이기 때문에 is_nice가 not이다.
is_nice = not any(c > 0 for c in check.values())
if is_nice:
    cnt += 1

# 2-1. 첫 부분문자열의 i-m번 문자열과 다음 부분문자열의 마지막 글자인 i번 문자열이 동일한지 비교하기 위한 반복문 선언
for i in range(m, n):

    # 2-2. 동일하면, is_nice flag가 True인지 체크한 뒤 cnt+1
    if data[i-m] == data[i]:
        if is_nice:
            cnt += 1

    # 2-3. i-m번 문자열은 dict에 +1 수행, i번문자열은 -1을 수행
    else:
        check[data[i-m]] += 1
        check[data[i]] -= 1

        # 2-4. dict안에 element가 0이상인지 확인하고 플래그 반영
        # is_nice = not any(c > 0 for c in check.values())
        is_nice = all(c <= 0 for c in check.values())

        # 2-5. 플래그가 True면 cnt+1
        if is_nice:
            cnt += 1

print(cnt)
