import streamlit as st
import requests
import pandas as pd
import gspread

def load_data(credentials, sheet_name):
    gc = gspread.service_account_from_dict(credentials)
    sh = gc.open(sheet_name)
    wks = sh.worksheet("Sheet1")
    raw_data = wks.get_all_values()
    st.session_state.data = pd.DataFrame(raw_data[1:], columns = raw_data[0])
    # return pd.DataFrame(wks.get_all_values())

def click_button(team_number):
    new_state = (st.session_state[team_number] + 1) % 3
    # Update session state
    st.session_state[team_number] = new_state

    # Update spreadsheet
    wks.update(range_name = f'B{team_number + 1}', values = new_state)
    
    # r = requests.post("https://api.apispreadsheets.com/data/PEiZQxeLHxAruOzL/", headers={}, json={"data": {"state":f"{new_state}"}, "query": f"select * from PEiZQxeLHxAruOzL where team='{team_number}'"})

def submit():
    st.session_state.user_input = st.session_state.widget
    st.session_state.widget = ''

google_credentials = {cred: st.secrets["google_creds"][cred] for cred in st.secrets["google_creds"]}

# Password to enter edit mode
pw = st.secrets["DB_PASS"]

# # Defining API to access spreadsheet
# API = "https://api.apispreadsheets.com/data/PEiZQxeLHxAruOzL/"

if 'initialized' not in st.session_state:
    st.session_state.initialized = False

if not st.session_state.initialized:
    # Getting initial status for each team
    load_data(google_credentials, st.secrets.sheet_name)
    st.session_state.initialized = True

# Setting number of teams
NUM_TEAMS = len(st.session_state.data)

# If False, the user can only view the team status, not change it
st.session_state.EDIT = False

# Setting up formatting
rows = dict()
for i in range(1, NUM_TEAMS + 1):
    if i not in st.session_state:
        st.session_state[i] = st.session_state.data.loc[st.session_state.data['team'] == i, 'state'].values[0]
    rows[i] = st.columns([0.2, 0.8])

if 'user_input' not in st.session_state:
    st.session_state.user_input = ''

st.text_input("Enter password to toggle editing", key = 'widget', on_change = submit)

if st.session_state.user_input == pw:
    st.success('Editing toggled')
    st.session_state.EDIT = not st.session_state.EDIT
elif st.session_state.user_input != "":
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
