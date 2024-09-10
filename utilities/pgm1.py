import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime


events = {
    "meetings": [],
    "training": [],
    "project_deadlines": [],
    "internalevent": [],
    "clientpresentation": [],
    "shift_schedules": [],
    "resources": set(),
    "conferences": [],
    "performancereview": [],
    "onboardingsession": []
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
        homepage()
    elif selected == "Meeting Management":
        meetingmanagement()
    elif selected == "Employee Training":
        employetraining()
    elif selected == "Project Deadlines":
        manageproject()
    elif selected == "Internal Events":
        internalevent()
    elif selected == "Client Presentations":
        clientpresentation()
    elif selected == "Shift Scheduling":
        shiftscheduling()
    elif selected == "Resource Allocation":
        resourceallocation()
    elif selected == "Conferences":
        manageconference()
    elif selected == "Performance Reviews":
        performancereview()
    elif selected == "Onboarding Sessions":
        onboardingsession()
    elif selected == "Blog":
        blogpage()

def homepage():
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

def blogpage():
    st.write('<h1 class="main-title">Blog</h1>', unsafe_allow_html=True)
    
    # Blog creation form
    st.write('<p class="info-text">Create and view blog posts about recent and upcoming events.</p>', unsafe_allow_html=True)
    blogtitle = st.text_input("Blog Title")
    blogcontent = st.text_area("Blog Content")
    blogdate = st.date_input("Blog Date", value=datetime.now().date())
    
    # Create blog post
    if st.button("Post Blog"):
        if blogtitle and blogcontent:
            blogs.append({
                "title": blogtitle, 
                "content": blogcontent, 
                "date": blogdate.strftime('%Y-%m-%d')  # Format date for display
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


def meetingmanagement():
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



def employetraining():
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


def manageproject():
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

def internalevent():
    st.title("Internal Events")
    st.write('<p class="info-text">Schedule and manage internal events.</p>', unsafe_allow_html=True)
    
    event_name = st.text_input("Enter Event Name")
    event_date = st.date_input("Event Date")
    if st.button("Schedule Event"):
        events["internalevent"].append((event_name, event_date))
        st.success("Internal Event Scheduled!")
    
    st.write('<p class="subheader-text">Internal Events</p>', unsafe_allow_html=True)
    for e in events["internalevent"]:
        st.write(f"Event: {e[0]}, Date: {e[1]}")

def clientpresentation():
    st.title("Client Presentations")
    st.write('<p class="info-text">Organize and schedule client presentations.</p>', unsafe_allow_html=True)
    
    presentation_name = st.text_input("Enter Presentation Name")
    client_name = st.text_input("Enter Client Name")
    presentation_date = st.date_input("Presentation Date")
    if st.button("Schedule Presentation"):
        events["clientpresentation"].append((presentation_name, client_name, presentation_date))
        st.success("Client Presentation Scheduled!")
    
    st.write('<p class="subheader-text">Client Presentations</p>', unsafe_allow_html=True)
    for p in events["clientpresentation"]:
        st.write(f"Presentation: {p[0]}, Client: {p[1]}, Date: {p[2]}")

def shiftscheduling():
    st.title("Shift Scheduling")
    st.write('<p class="info-text">Manage employee shifts and schedules.</p>', unsafe_allow_html=True)
    
    empname = st.text_input("Enter Employee Name")
    shiftdate = st.date_input("Shift Date")
    shifttime = st.text_input("Enter Shift Time")
    if st.button("Schedule Shift"):
        events["shift_schedules"].append((empname, shiftdate, shifttime))
        st.success("Shift Scheduled!")
    
    st.write('<p class="subheader-text">Shift Schedules</p>', unsafe_allow_html=True)
    for s in events["shift_schedules"]:
        st.write(f"Employee: {s[0]}, Date: {s[1]}, Time: {s[2]}")

def resourceallocation():
    st.title("Resource Allocation")
    st.write('<p class="info-text">Allocate and manage resources.</p>', unsafe_allow_html=True)
    
    resourcename = st.text_input("Enter Resource Name")
    allocatedate = st.date_input("Allocation Date")
    if st.button("Allocate Resource"):
        events["resources"].add((resourcename, allocatedate))
        st.success("Resource Allocated!")
    
    st.write('<p class="subheader-text">Allocated Resources</p>', unsafe_allow_html=True)
    for r in events["resources"]:
        st.write(f"Resource: {r[0]}, Date: {r[1]}")

def manageconference():
    st.write('<h1 class="main-title">Conference Management</h1>', unsafe_allow_html=True)
    st.write('<p class="info-text">Manage your conferences effectively.</p>', unsafe_allow_html=True)

    # Input fields for adding a new conference
    conferencename = st.text_input("Enter Conference Name")
    conferencedate = st.date_input("Conference Date")
    location = st.text_input("Enter Conference Location")
    attendees = st.number_input("Number of Attendees", min_value=1, value=10)

    # Add conference button
    if st.button("Add Conference"):
        events["conferences"].append({
            "name": conferencename, 
            "date": conferencedate, 
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
                    newconfname = st.text_input(f"Update Conference Name for {conference['name']}", value=conference['name'])
                    newconfdate = st.date_input(f"Update Conference Date for {conference['date']}", value=conference['date'])
                    newlocation = st.text_input(f"Update Location for {conference['location']}", value=conference['location'])
                    newattende = st.number_input(f"Update Number of Attendees for {conference['attendees']}", min_value=1, value=conference['attendees'])
                    
                    if st.button(f"Confirm Update for {conference['name']}"):
                        events["conferences"][i] = {
                            "name": newconfname, 
                            "date": newconfdate, 
                            "location": newlocation, 
                            "attendees": newattende
                        }
                        st.success(f"Conference {newconfname} updated successfully!")

            with col2:
                if st.button(f"Delete {conference['name']}"):
                    # Delete the selected conference
                    events["conferences"].pop(i)
                    st.success(f"Conference {conference['name']} deleted successfully!")

            st.write("---")
    else:
        st.write("No conferences currently available.")


def performancereview():
    st.title("Performance Reviews")
    st.write('<p class="info-text">Provide performance reviews for employees.</p>', unsafe_allow_html=True)
    
    empname = st.text_input("Enter Employee Name")
    employee_id = st.text_input("Enter Employee ID")
    performrate = st.slider("Rate Performance (1 to 5)", 1, 5)
    reviewremark = st.text_area("Enter Remarks")
    
    if st.button("Submit Review"):
    
        events["performancereview"].append({
            "empname": empname,
            "employee_id": employee_id,
            "rating": performrate,
            "remarks": reviewremark
        })
        st.success("Performance Review Submitted!")
    
  

for r in events["performancereview"]:
        st.write(f"Employee: {r['empname']}, ID: {r['employee_id']}, Rating: {r['rating']}/5")
        st.write(f"Remarks: {r['remarks']}")
        st.write("---")
def onboardingsession():
    st.title("Onboarding Sessions")
    st.write('<p class="info-text">Plan onboarding sessions for new employees.</p>', unsafe_allow_html=True)
    
    sessioname = st.text_input("Enter Onboarding Session Name")
    sessiondate = st.date_input("Session Date")
    if st.button("Schedule Onboarding Session"):
        events["onboardingsession"].append((sessioname, sessiondate))
        st.success("Onboarding Session Scheduled!")
    
    st.write('<p class="subheader-text">Scheduled Onboarding Sessions</p>', unsafe_allow_html=True)
    for s in events["onboardingsession"]:
        st.write(f"Session: {s[0]}, Date: {s[1]}")

if __name__ == '_main_':
  main()
