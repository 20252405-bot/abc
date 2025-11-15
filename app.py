import streamlit as st
import random
import time

# 게임 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "tower_positions" not in st.session_state:
    st.session_state.tower_positions = []

# 타워 디펜스 맵
map_size = 10
enemy_path = [(i, map_size - 1 - i) for i in range(map_size)]  # 적의 이동 경로

# 게임 시작
st.title("🏰 간단한 타워 디펜스 게임")
st.write("타워를 배치하여 적을 막아보세요! 적이 지나가면 게임 오버.")

# 타워 배치
def add_tower(x, y):
    if (x, y) not in st.session_state.tower_positions:
        st.session_state.tower_positions.append((x, y))
        st.session_state.score += 1

# 적의 이동
def move_enemy():
    if len(enemy_path) > 0:
        enemy = enemy_path.pop(0)
        if enemy in st.session_state.tower_positions:
            st.session_state.score -= 1  # 타워에 막혔을 때 점수 감소
            st.session_state.game_over = True
        return enemy
    return None

# 타워 배치 인터페이스
x = st.slider("타워 배치 (X 좌표)", 0, map_size - 1)
y = st.slider("타워 배치 (Y 좌표)", 0, map_size - 1)

if st.button("타워 배치"):
    add_tower(x, y)

# 적 이동 및 게임 상태 확인
enemy = move_enemy()

# 게임 맵 표시
st.write("맵:")
for row in range(map_size):
    row_str = ""
    for col in range(map_size):
        if (col, row) in st.session_state.tower_positions:
            row_str += "🛡️"  # 타워
        elif enemy and (col, row) == enemy:
            row_str += "👾"  # 적
        else:
            row_str += "⬜"  # 빈 공간
    st.write(row_str)

# 게임 상태
if st.session_state.game_over:
    st.balloons()
    st.success(f"게임 오버! 최종 점수: {st.session_state.score}")
    if st.button("게임 다시 시작"):
        st.session_state.score = 0
        st.session_state.game_over = False
        st.session_state.tower_positions = []
        enemy_path = [(i, map_size - 1 - i) for i in range(map_size)]
else:
    st.write(f"현재 점수: {st.session_state.score}")
