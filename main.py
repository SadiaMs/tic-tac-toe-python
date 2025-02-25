import streamlit as st

# Page Configuration
st.set_page_config(page_title="Tic Tac Toe", page_icon="🎮")

st.title("🎮 Tic-Tac-Toe Game")
st.write("Click on the grid to play.")

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

# Button Click Function
def button_click(index):
    if st.session_state.board[index] == "" and not st.session_state.winner:
        st.session_state.board[index] = st.session_state.current_player
        check_winner()
        if not st.session_state.winner:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# Display the Tic Tac Toe Board
cols = st.columns(3)
for i in range(9):
    with cols[i % 3]:
        if st.button(st.session_state.board[i] or " ", key=i):
            button_click(i)

# Display Winner
if st.session_state.winner:
    st.success(f"🎉 Player {st.session_state.winner} wins!")
    if st.button("Restart Game"):
        st.session_state.board = [""] * 9
        st.session_state.current_player = "X"
        st.session_state.winner = None
