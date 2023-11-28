import streamlit as st

if 'button' not in st.session_state:
    st.session_state.button = 0

def click_button():
    st.session_state.button = (st.session_state.button + 1) % 3

for i in range(1, 14):
    st.button(f'Status team {i}', on_click=click_button)

if st.session_state.button == 0:
    # The message and nested widget will remain on the page
    st.write('Meeting not started.')
elif st.session_state.button == 1:
    st.write('Meeting in progress!')
else:
    st.write('Meeting finished.')
