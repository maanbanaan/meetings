import streamlit as st

NUM_TEAMS = 12

for i in range(1, NUM_TEAMS + 1):
    if i not in st.session_state:
        st.session_state[i] = 0

def click_button(team_number):
    st.session_state[team_number] = (st.session_state[team_number] + 1) % 3
col1, col2 = st.columns([1,1])
for i in range(1, NUM_TEAMS + 1):
    with col1:
        st.button(f'Status team {i}', on_click=click_button, args=[i])
    with col2:
        if st.session_state[i] == 0:
            # The message and nested widget will remain on the page
            st.write('Meeting not started.')
        elif st.session_state[i] == 1:
            st.write('Meeting in progress!')
        else:
            st.write('Meeting finished.')

with st.expander('Options'):
    row1 = st.columns(2)
    row2 = st.columns(2)
    row3 = st.columns(2)
