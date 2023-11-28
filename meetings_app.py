import streamlit as st
import pandas as pd

# Create a DataFrame to store the meeting schedule
schedule_data = pd.DataFrame({
    'Team Number': range(1, 11),
    'Meeting Status': ['Not Started'] * 10
})

def toggle_status(team_number):
    current_status = schedule_data.loc[schedule_data['Team Number'] == team_number, 'Meeting Status'].values[0]
    
    if current_status == 'Not Started':
        schedule_data.loc[schedule_data['Team Number'] == team_number, 'Meeting Status'] = 'In Progress'
    elif current_status == 'In Progress':
        schedule_data.loc[schedule_data['Team Number'] == team_number, 'Meeting Status'] = 'Complete'
    elif current_status == 'Complete':
        schedule_data.loc[schedule_data['Team Number'] == team_number, 'Meeting Status'] = 'Not Started'

def main():
    st.title('Meeting Status App')

    # Display the table with a button for each row
    for index, row in schedule_data.iterrows():
        team_number = row['Team Number']
        meeting_status = row['Meeting Status']
        
        col1, col2, col3 = st.beta_columns([1, 1, 6])

        with col1:
            st.write(f"Team {team_number}")

        with col2:
            st.write(meeting_status)

        with col3:
            if st.button(f"Toggle Status ({team_number})", key=f"button_{team_number}"):
                toggle_status(team_number)

    # Display the updated table
    st.table(schedule_data)

if __name__ == '__main__':
    main()
