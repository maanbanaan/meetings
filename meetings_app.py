import streamlit as st
import pandas as pd
import gspread

for cred in st.secrets["google_creds"]:
    st.write(cred)

credentials = {cred: st.secrets["google_creds"][cred] for cred in st.secrets["google_creds"]}
st.write(credentials)
st.write(st.secrets["google_creds"])

schedule_data = pd.DataFrame({
    'Team Number': range(1, 11),
    'Meeting Status': ['Not Started'] * 10
})

def main():
    st.title('Meeting Status App')

    team_number = st.selectbox('Select Team Number:', range(1, 11))
    meeting_status = st.radio('Meeting Status:', ['Not Started', 'In Progress', 'Completed'])

    # Update the schedule_data DataFrame based on user input
    schedule_data.loc[schedule_data['Team Number'] == team_number, 'Meeting Status'] = meeting_status

    st.table(schedule_data)
    
if __name__ == '__main__':
    main()
