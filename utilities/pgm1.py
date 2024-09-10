import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime


events = {
    "meetings": [],
    "training": [],
    "project_deadlines": [],
    "internal_events": [],
    "client_presentations": [],
    "shift_schedules": [],
    "resources": set(),
    "conferences": [],
    "performance_reviews": [],
    "onboarding_sessions": []
}

employees = set()

blogs = []
def main():
    with st.sidebar:
        selected = option_menu(
            "IT Event Scheduler", 
            ["Home", "Meeting Management", "Employee Training", "Project Deadlines", 
             "Internal Events", "Client Presentations", "Shift Scheduling", 
             "Resource Allocation", "Conferences", "Performance Reviews", 
             "Onboarding Sessions", "Blog"], 
            icons=['house', 'check-square', 'book', 'flag', 'calendar', 'presentation', 'clock', 
                   'cloud-upload', 'globe', 'star', 'person-plus', 'journal'], 
            menu_icon="cast", 
            default_index=0,
            styles={
                "container": {"padding": "5px", "background-color": "#333"},
                "icon": {"color": "#FFFFFF", "font-size": "18px"}, 
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#444"},
                "nav-link-selected": {"background-color": "#1f77b4", "color": "white"},
            }
        )
    st.markdown(r"""
        <style>
        /* General layout and style */
        body {
            background-color: #212121; /* Dark background for the entire app */
            color: #FFFFFF; /* Light text for readability */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Modern font */
            background-image: url(r"C:\Users\SANDHYA M\Desktop\1.png");
            background-size: cover;
        }
        .main-title {
            color: #1f77b4;
            text-align: center;
            font-size: 36px;
            margin-bottom: 20px;
            padding: 10px;
            background-color: #333;
            border-radius: 10px;
        }
        .info-text {
            color: yellow;
            text-align: left;
            font-size: 18px;
            margin-bottom: 30px;
        }
        .subheader-text {
            color: #e67e22;
            font-size: 24px;
            margin-top: 20px;
            margin-bottom: 10px;
            padding: 5px 0;
            border-bottom: 2px solid #444;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            border-radius: 8px;
            width: 100%;
            padding: 10px;
            font-size: 16px;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #e67e22; /* Change color on hover for better UX */
        }
           
        input, textarea {
            border-radius: 5px;
            border: 1px solid #555;
            padding: 8px;
            margin-bottom: 15px;
            width: 100%;
            background-color: #333;
            color: white;
        }
        .data-container {
            background-color: #2b2b2b;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)


    if selected == "Home":
        home_page()
    elif selected == "Meeting Management":
        meeting_management()
    elif selected == "Employee Training":
        employee_training()
    elif selected == "Project Deadlines":
        manage_projects()
    elif selected == "Internal Events":
        internal_events()
    elif selected == "Client Presentations":
        client_presentations()
    elif selected == "Shift Scheduling":
        shift_scheduling()
    elif selected == "Resource Allocation":
        resource_allocation()
    elif selected == "Conferences":
        manage_conferences()
    elif selected == "Performance Reviews":
        performance_reviews()
    elif selected == "Onboarding Sessions":
        onboarding_sessions()
    elif selected == "Blog":
        blog_page()

def home_page():
    st.write('<h1 class="main-title">Welcome to IT Event Scheduler</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Manage your meetings, training sessions, project deadlines, and more with ease.</p>', unsafe_allow_html=True)
    st.write('<p class="subheader-text">Latest Blog Posts</p>', unsafe_allow_html=True)
    if blogs:
        for blog in blogs:
            st.write(f"{blog['title']}** - {blog['date']}")
            st.write(blog['content'])
            st.write("---")
    else:
        st.write("No blog posts available.")

def blog_page():
    st.write('<h1 class="main-title">Blog</h1>', unsafe_allow_html=True)
    
    # Blog creation form
    st.write('<p class="info-text">Create and view blog posts about recent and upcoming events.</p>', unsafe_allow_html=True)
    blog_title = st.text_input("Blog Title")
    blog_content = st.text_area("Blog Content")
    blog_date = st.date_input("Blog Date", value=datetime.now().date())
    
    # Create blog post
    if st.button("Post Blog"):
        if blog_title and blog_content:
            blogs.append({
                "title": blog_title, 
                "content": blog_content, 
                "date": blog_date.strftime('%Y-%m-%d')  # Format date for display
            })
            st.success("Blog Post Created!")
        else:
            st.error("Please fill in all fields.")
    
    # Display blog posts
    st.write('<p class="subheader-text">Blog Posts</p>', unsafe_allow_html=True)
    
    if blogs:
        # Display each blog post
        for blog in blogs:
            st.write(f"{blog['title']}** - {blog['date']}")
            st.write(blog['content'])
            st.write("---")
    else:
        st.write("No blog posts available.")


def meeting_management():
    st.write('<h1 class="main-title">Meeting Management</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Schedule and manage meetings with your team.</p>', unsafe_allow_html=True)

    meeting = st.text_input("Enter Meeting Name")
    participants = st.text_area("Enter Participants (comma separated)")
    date = st.date_input("Meeting Date")
    if st.button("Schedule Meeting"):
        meetings_tuple = (meeting, participants.split(','), date)
        events["meetings"].append(meetings_tuple)
        st.success("Meeting Scheduled!")
    
    st.write('<p class="subheader-text">Scheduled Meetings</p>', unsafe_allow_html=True)

    if events["meetings"]:
    
        for index, meeting in enumerate(events["meetings"]):
            st.write(f"*Meeting:* {meeting[0]}, *Participants:* {', '.join(meeting[1])}, *Date:* {meeting[2]}")
            
          
            if st.button(f"Update Meeting {index + 1}", key=f"update_{index}"):
                updated_meeting = st.text_input(f"Update Meeting Name", value=meeting[0])
                updated_participants = st.text_area(f"Update Participants", value=', '.join(meeting[1]))
                updated_date = st.date_input(f"Update Meeting Date", value=meeting[2])
                
                if st.button(f"Save Changes {index + 1}", key=f"save_{index}"):
                    events["meetings"][index] = (updated_meeting, updated_participants.split(','), updated_date)
                    st.success(f"Meeting {index + 1} Updated!")
            
           
            if st.button(f"Delete Meeting {index + 1}", key=f"delete_{index}"):
                events["meetings"].pop(index)
                st.warning(f"Meeting {index + 1} Deleted!")
                st.experimental_rerun()



def employee_training():
    st.write('<h1 class="main-title">Employee Training</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Organize training sessions for employees.</p>', unsafe_allow_html=True)

    session = st.text_input("Enter Training Session")
    trainer = st.text_input("Enter Trainer Name")
    date = st.date_input("Training Date")
    
    if st.button("Schedule Training"):
        events["training"].append({"session": session, "trainer": trainer, "date": date})
        st.success("Training Session Scheduled!")

    st.write('<p class="subheader-text">Scheduled Trainings</p>', unsafe_allow_html=True)

    # Display scheduled training sessions with Update and Delete options
    if events["training"]:
        for i, t in enumerate(events["training"]):
            st.write(f"Session: {t['session']}, Trainer: {t['trainer']}, Date: {t['date']}")
            
            # Add buttons for updating and deleting each training session
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button(f"Update {t['session']}"):
                    # Allow user to update the details
                    new_session = st.text_input(f"Update Session Name for {t['session']}", value=t['session'])
                    new_trainer = st.text_input(f"Update Trainer for {t['trainer']}", value=t['trainer'])
                    new_date = st.date_input(f"Update Date for {t['date']}", value=t['date'])
                    
                    if st.button(f"Confirm Update for {t['session']}"):
                        events["training"][i] = {"session": new_session, "trainer": new_trainer, "date": new_date}
                        st.success(f"Training session for {new_session} updated!")

            with col2:
                if st.button(f"Delete {t['session']}"):
                    # Delete the selected training session
                    events["training"].pop(i)
                    st.success(f"Training session {t['session']} deleted!")
                    
            st.write("---")
    else:
        st.write("No training sessions scheduled.")


def manage_projects():
    st.write('<h1 class="main-title">Project Management</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Manage your projects efficiently.</p>', unsafe_allow_html=True)
    events = {
    "projects": [],  # Initialize with an empty list for projects
    "conferences": []  # Initialize with an empty list for conferences
    }
    # Input fields for adding a new project
    project_name = st.text_input("Enter Project Name")
    project_manager = st.text_input("Enter Project Manager")
    deadline = st.date_input("Project Deadline")

    # Add project button
    if st.button("Add Project"):
        events["projects"].append({"name": project_name, "manager": project_manager, "deadline": deadline})
        st.success("Project Added Successfully!")

    st.write('<p class="subheader-text">Current Projects</p>', unsafe_allow_html=True)

    # Display the current list of projects with Update and Delete options
    if events["projects"]:
        for i, project in enumerate(events["projects"]):
            st.write(f"Project: {project['name']}, Manager: {project['manager']}, Deadline: {project['deadline']}")
            
            # Add buttons for updating and deleting each project
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button(f"Update {project['name']}"):
                    # Allow user to update the details
                    new_project_name = st.text_input(f"Update Project Name for {project['name']}", value=project['name'])
                    new_manager = st.text_input(f"Update Manager for {project['manager']}", value=project['manager'])
                    new_deadline = st.date_input(f"Update Deadline for {project['deadline']}", value=project['deadline'])
                    
                    if st.button(f"Confirm Update for {project['name']}"):
                        events["projects"][i] = {"name": new_project_name, "manager": new_manager, "deadline": new_deadline}
                        st.success(f"Project {new_project_name} updated successfully!")

            with col2:
                if st.button(f"Delete {project['name']}"):
                    # Delete the selected project
                    events["projects"].pop(i)
                    st.success(f"Project {project['name']} deleted successfully!")

            st.write("---")
    else:
        st.write("No projects currently available.")

def internal_events():
    st.title("Internal Events")
    st.write('<p class="info-text">Schedule and manage internal events.</p>', unsafe_allow_html=True)
    
    event_name = st.text_input("Enter Event Name")
    event_date = st.date_input("Event Date")
    if st.button("Schedule Event"):
        events["internal_events"].append((event_name, event_date))
        st.success("Internal Event Scheduled!")
    
    st.write('<p class="subheader-text">Internal Events</p>', unsafe_allow_html=True)
    for e in events["internal_events"]:
        st.write(f"Event: {e[0]}, Date: {e[1]}")

def client_presentations():
    st.title("Client Presentations")
    st.write('<p class="info-text">Organize and schedule client presentations.</p>', unsafe_allow_html=True)
    
    presentation_name = st.text_input("Enter Presentation Name")
    client_name = st.text_input("Enter Client Name")
    presentation_date = st.date_input("Presentation Date")
    if st.button("Schedule Presentation"):
        events["client_presentations"].append((presentation_name, client_name, presentation_date))
        st.success("Client Presentation Scheduled!")
    
    st.write('<p class="subheader-text">Client Presentations</p>', unsafe_allow_html=True)
    for p in events["client_presentations"]:
        st.write(f"Presentation: {p[0]}, Client: {p[1]}, Date: {p[2]}")

def shift_scheduling():
    st.title("Shift Scheduling")
    st.write('<p class="info-text">Manage employee shifts and schedules.</p>', unsafe_allow_html=True)
    
    employee_name = st.text_input("Enter Employee Name")
    shift_date = st.date_input("Shift Date")
    shift_time = st.text_input("Enter Shift Time")
    if st.button("Schedule Shift"):
        events["shift_schedules"].append((employee_name, shift_date, shift_time))
        st.success("Shift Scheduled!")
    
    st.write('<p class="subheader-text">Shift Schedules</p>', unsafe_allow_html=True)
    for s in events["shift_schedules"]:
        st.write(f"Employee: {s[0]}, Date: {s[1]}, Time: {s[2]}")

def resource_allocation():
    st.title("Resource Allocation")
    st.write('<p class="info-text">Allocate and manage resources.</p>', unsafe_allow_html=True)
    
    resource_name = st.text_input("Enter Resource Name")
    allocation_date = st.date_input("Allocation Date")
    if st.button("Allocate Resource"):
        events["resources"].add((resource_name, allocation_date))
        st.success("Resource Allocated!")
    
    st.write('<p class="subheader-text">Allocated Resources</p>', unsafe_allow_html=True)
    for r in events["resources"]:
        st.write(f"Resource: {r[0]}, Date: {r[1]}")

def manage_conferences():
    st.write('<h1 class="main-title">Conference Management</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Manage your conferences effectively.</p>', unsafe_allow_html=True)

    # Input fields for adding a new conference
    conference_name = st.text_input("Enter Conference Name")
    conference_date = st.date_input("Conference Date")
    location = st.text_input("Enter Conference Location")
    attendees = st.number_input("Number of Attendees", min_value=1, value=10)

    # Add conference button
    if st.button("Add Conference"):
        events["conferences"].append({
            "name": conference_name, 
            "date": conference_date, 
            "location": location, 
            "attendees": attendees
        })
        st.success("Conference Added Successfully!")

    st.write('<p class="subheader-text">Current Conferences</p>', unsafe_allow_html=True)

    # Display the current list of conferences with Update and Delete options
    if events["conferences"]:
        for i, conference in enumerate(events["conferences"]):
            st.write(f"Conference: {conference['name']}, Date: {conference['date']}, Location: {conference['location']}, Attendees: {conference['attendees']}")

            # Add buttons for updating and deleting each conference
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button(f"Update {conference['name']}"):
                    # Allow user to update the details
                    new_conference_name = st.text_input(f"Update Conference Name for {conference['name']}", value=conference['name'])
                    new_conference_date = st.date_input(f"Update Conference Date for {conference['date']}", value=conference['date'])
                    new_location = st.text_input(f"Update Location for {conference['location']}", value=conference['location'])
                    new_attendees = st.number_input(f"Update Number of Attendees for {conference['attendees']}", min_value=1, value=conference['attendees'])
                    
                    if st.button(f"Confirm Update for {conference['name']}"):
                        events["conferences"][i] = {
                            "name": new_conference_name, 
                            "date": new_conference_date, 
                            "location": new_location, 
                            "attendees": new_attendees
                        }
                        st.success(f"Conference {new_conference_name} updated successfully!")

            with col2:
                if st.button(f"Delete {conference['name']}"):
                    # Delete the selected conference
                    events["conferences"].pop(i)
                    st.success(f"Conference {conference['name']} deleted successfully!")

            st.write("---")
    else:
        st.write("No conferences currently available.")


def performance_reviews():
    st.title("Performance Reviews")
    st.write('<p class="info-text">Provide performance reviews for employees.</p>', unsafe_allow_html=True)
    
    employee_name = st.text_input("Enter Employee Name")
    employee_id = st.text_input("Enter Employee ID")
    performance_rating = st.slider("Rate Performance (1 to 5)", 1, 5)
    review_remarks = st.text_area("Enter Remarks")
    
    if st.button("Submit Review"):
    
        events["performance_reviews"].append({
            "employee_name": employee_name,
            "employee_id": employee_id,
            "rating": performance_rating,
            "remarks": review_remarks
        })
        st.success("Performance Review Submitted!")
    
  

for r in events["performance_reviews"]:
        st.write(f"Employee: {r['employee_name']}, ID: {r['employee_id']}, Rating: {r['rating']}/5")
        st.write(f"Remarks: {r['remarks']}")
        st.write("---")
def onboarding_sessions():
    st.title("Onboarding Sessions")
    st.write('<p class="info-text">Plan onboarding sessions for new employees.</p>', unsafe_allow_html=True)
    
    session_name = st.text_input("Enter Onboarding Session Name")
    session_date = st.date_input("Session Date")
    if st.button("Schedule Onboarding Session"):
        events["onboarding_sessions"].append((session_name, session_date))
        st.success("Onboarding Session Scheduled!")
    
    st.write('<p class="subheader-text">Scheduled Onboarding Sessions</p>', unsafe_allow_html=True)
    for s in events["onboarding_sessions"]:
        st.write(f"Session: {s[0]}, Date: {s[1]}")

if _name_ == '_main_':
    main()
