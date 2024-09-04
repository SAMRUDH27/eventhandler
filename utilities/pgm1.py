import streamlit as st
from datetime import datetime

# Initialize the session state for storing events
if 'events' not in st.session_state:
    st.session_state['events'] = []

# Function to add an event
def add_event():
    event_name = st.text_input('Event Name')
    event_date = st.date_input('Event Date')
    event_time = st.time_input('Event Time')

    if st.button('Add Event'):
        event = {
            'name': event_name,
            'date': event_date,
            'time': event_time,
            'datetime': datetime.combine(event_date, event_time)
        }
        st.session_state['events'].append(event)
        st.success('Event added!')

# Function to view and remove events
def view_events():
    st.write("### Scheduled Events:")
    events = sorted(st.session_state['events'], key=lambda x: x['datetime'])
    for idx, event in enumerate(events):
        st.write(f"{idx + 1}. **{event['name']}** on {event['date']} at {event['time']}")
        if st.button(f'Remove {event["name"]}', key=f'remove_{idx}'):
            st.session_state['events'].pop(idx)
            st.experimental_rerun()

# App Layout
st.title("Event Scheduler")
add_event()
view_events()
