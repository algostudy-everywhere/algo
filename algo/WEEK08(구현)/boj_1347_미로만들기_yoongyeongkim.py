# 움직임 횟수 입력
n = int(input())

# 이동 경로 입력
move = list(str(input()))

# 방향 이동을 위한 리스트 설정 (남, 서, 북, 동 순서)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 시작 위치 설정 (0, 0)
current_position = [[0, 0]]

# 초기 바라보는 방향 설정 (남쪽)
direction = 0

# 현재 위치 좌표
x = 0
y = 0

# 이동 경로에 따른 위치 변화 처리
for step in move:
    if step == 'F':  # 앞으로 이동
        x += dx[direction % 4]
        y += dy[direction % 4]
        current_position.append([x, y])
    elif step == 'R':  # 오른쪽 회전
        direction = (direction + 1) % 4
    else:  # 왼쪽 회전
        direction = (direction + 3) % 4

# x와 y 좌표 따로 저장
x_coords = [pos[0] for pos in current_position]
y_coords = [pos[1] for pos in current_position]

# x와 y의 길이 계산
x_length = len(set(x_coords))
y_length = len(set(y_coords))

# x와 y의 최소값 계산
x_min = min(x_coords)
y_min = min(y_coords)

# 최소값이 0보다 작으면 절대값만큼 더해서 시작 위치를 0으로 고정
x_offset = abs(x_min) if x_min < 0 else 0
y_offset = abs(y_min) if y_min < 0 else 0

# x와 y의 길이값을 기반으로 보드 생성
board = [['#'] * y_length for _ in range(x_length)]

# 방문한 위치를 '.'로 표시
for pos in current_position:
    board[pos[0] + x_offset][pos[1] + y_offset] = '.'

# 결과 출력
for row in board:
    print(''.join(row))
