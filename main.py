import streamlit as st

# Page Configuration
st.set_page_config(page_title="🎮 Tic-Tac-Toe", page_icon="❌⭕", layout="centered")

# Title
st.title("🎮 Tic-Tac-Toe Game")
st.write("Click a box to make your move!")

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None

# Winning Combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]  # Diagonals
]

# Function to check winner
def check_winner():
    for combo in winning_combinations:
        a, b, c = combo
        if (st.session_state.board[a] == 
            st.session_state.board[b] == 
            st.session_state.board[c] != ""):
            st.session_state.winner = st.session_state.board[a]
            return

# Button Click Function (One-Click Play)
def button_click(index):
    if st.session_state.board[index] == "" and not st.session_state.winner:
        st.session_state.board[index] = st.session_state.current_player
        check_winner()
        if not st.session_state.winner:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# Display the Tic Tac Toe Board with Stylish Buttons
st.markdown("---")
cols = st.columns(3)
for i in range(9):
    with cols[i % 3]:
        btn_style = f"""
        <style>
            .stButton > button {{
                width: 100px;
                height: 100px;
                font-size: 30px;
                font-weight: bold;
                color: black;
                border-radius: 10px;
                border: 2px solid #333;
                background: #ddd;
                transition: 0.3s;
            }}
            .stButton > button:hover {{
                background: #bbb;
            }}
        </style>
        """
        st.markdown(btn_style, unsafe_allow_html=True)
        if st.button(st.session_state.board[i] or " ", key=i):
            button_click(i)

st.markdown("---")

# Display Winner or Turn Announcement
if st.session_state.winner:
    st.success(f"🎉 Player {st.session_state.winner} wins!")
else:
    st.info(f"🔄 Player {st.session_state.current_player}'s turn")

# Restart Button
if st.button("🔄 Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.experimental_rerun()

