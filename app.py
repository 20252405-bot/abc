import streamlit as st

# 맵 설정 (0=빈칸, 1=벽, 2=먹이)
map_layout = [
    [1,1,1,1,1,1,1],
    [1,2,0,0,0,2,1],
    [1,0,1,1,0,0,1],
    [1,0,0,0,0,0,1],
    [1,2,0,1,0,2,1],
    [1,1,1,1,1,1,1]
]

rows = len(map_layout)
cols = len(map_layout[0])

# 세션 상태 초기화
if 'pacman_pos' not in st.session_state:
    st.session_state.pacman_pos = [3,3]  # 초기 위치
if 'score' not in st.session_state:
    st.session_state.score = 0

# 이동 함수
def move(direction):
    r, c = st.session_state.pacman_pos
    if direction == "UP":
        new_r, new_c = r-1, c
    elif direction == "DOWN":
        new_r, new_c = r+1, c
    elif direction == "LEFT":
        new_r, new_c = r, c-1
    elif direction == "RIGHT":
        new_r, new_c = r, c+1
    else:
        return
    
    # 벽 체크
    if map_layout[new_r][new_c] != 1:
        st.session_state.pacman_pos = [new_r, new_c]
        # 먹이 체크
        if map_layout[new_r][new_c] == 2:
            st.session_state.score += 1
            map_layout[new_r][new_c] = 0

# 버튼으로 이동 제어
st.title("🎮 스트림릿 팩맨")
st.write(f"현재 점수: {st.session_state.score}")

col1, col2, col3 = st.columns(3)
with col2:
    if st.button("↑"): move("UP")
col_left, col_middle, col_right = st.columns(3)
with col_left:
    if st.button("←"): move("LEFT")
with col_middle:
    st.write(" ")
with col_right:
    if st.button("→"): move("RIGHT")
with col2:
    if st.button("↓"): move("DOWN")

# 맵 표시
def display_map():
    display = ""
    for r in range(rows):
        for c in range(cols):
            if [r,c] == st.session_state.pacman_pos:
                display += "😋"  # 팩맨
            elif map_layout[r][c] == 1:
                display += "⬛"  # 벽
            elif map_layout[r][c] == 2:
                display += "🍎"  # 먹이
            else:
                display += "⬜"  # 빈 공간
        display += "\n"
    st.text(display)

display_map()
