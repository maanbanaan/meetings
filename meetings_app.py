import streamlit as st

NUM_TEAMS = 12

for i in range(1, NUM_TEAMS + 1):
    if i not in st.session_state:
        st.session_state[i] = 0

def click_button(team_number):
    st.session_state.button = (st.session_state[team_number] + 1) % 3

for i in range(1, 14):
    st.button(f'Status team {i}', on_click=click_button, args=[i])
    if st.session_state[i] == 0:
        # The message and nested widget will remain on the page
        st.write('Meeting not started.')
    elif st.session_state[i] == 1:
        st.write('Meeting in progress!')
    else:
        st.write('Meeting finished.')
