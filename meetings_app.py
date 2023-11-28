import streamlit as st
import requests
import pandas as pd

# Defining API to access spreadsheet
API = "https://api.apispreadsheets.com/data/PEiZQxeLHxAruOzL/"

NUM_TEAMS = 12

rows = dict()

if initialized not in st.session_state:
    st.session_state.initialized = False

if not st.session_state.initalized:
    # Getting initial status for each team
    r = requests.get("https://api.apispreadsheets.com/data/PEiZQxeLHxAruOzL/")
    initial_data = pd.DataFrame(r.json()['data'])
    st.session_state.initialized = True

# If False, the user can only view the team status, not change it
st.session_state.EDIT = False

# Required to enter edit mode
pw = 'HAABSA++'

for i in range(1, NUM_TEAMS + 1):
    if i not in st.session_state:
        st.session_state[i] = initial_data.loc[initial_data['team'] == i, 'state'].values[0]
    rows[i] = st.columns([0.2, 0.8])

def click_button(team_number):
    new_state = (st.session_state[team_number] + 1) % 3
    # Update session state
    st.session_state[team_number] = new_state

    # Update spreadsheet
    r = requests.post("https://api.apispreadsheets.com/data/PEiZQxeLHxAruOzL/", headers={}, json={"data": {"state":f"{new_state}"}, "query": f"select * from PEiZQxeLHxAruOzL where team='{team_number}'"})

user_input = st.text_input("Enter password to toggle editing", placeholder = 'Password')
if user_input == pw:
    st.success('Editing toggled')
    st.session_state.EDIT = not st.session_state.EDIT
elif user_input != "":
    st.error('Wrong password', icon="🤡")

for i in range(1, NUM_TEAMS + 1):
    with rows[i][0]:
        if st.session_state.EDIT:
            st.button(f'Status team {i}', on_click=click_button, args=[i])
        else: 
            st.write(f'Status team {i}')
    with rows[i][1]:
        if st.session_state[i] == 0:
            # The message and nested widget will remain on the page
            st.write(':red[Meeting not started.]')
        elif st.session_state[i] == 1:
            st.write(':orange[Meeting in progress!]')
        else:
            st.write(':green[Meeting finished.]')
