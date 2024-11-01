import tkinter as tk
from tkinter import ttk, messagebox
import os
import csv
from datetime import datetime
from PIL import Image, ImageTk
import numpy as np

class Backend:
    """Handles backend operations like data loading, saving, and admin verification."""
    def __init__(self, filename="rikami.csv"):  
        self.filename = filename

    def load_student_data(self):
        """Loads all student data from the CSV file."""
        students = []
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    #print(f"Loaded student roll number: '{row['Roll No.']}'")  # Debug print
                    students.append(row)      
            return students
        except FileNotFoundError:
            print("File not found.")
            return []

    def get_student_by_roll(self, roll_number):
        """Retrieves student data based on the roll number."""
        students = self.load_student_data()
        found_student = None  # Initialize a variable to hold the found student

        for student in students:
            print('student roll are ',student['Roll No.'])
            # Check if the roll number matches
            if str(student['Roll No.']).strip() == str(roll_number):
                found_student = student
                break  # Exit the loop once the student is found

        if found_student:
            print(f"Found student with Roll No: '{roll_number}'")  # Print only when found
            return found_student
        else:
            print(f"No student found with Roll No. {roll_number}")  # Print only if not found
            return None

    def update_student_info(self, roll, field, new_value):
        """Updates a student's information in the CSV file."""
        students = self.load_student_data()
        updated = False
        for student in students:
            if student["Roll No."] == roll:
                if field in student:
                    student[field] = new_value
                    updated = True
                    print(f"Updated {field} for Roll No. {roll} to {new_value}.")
                    break
        if updated:
            self.save_student_data(students)
            #self.open_student_profile(roll)
        else:
            print(f"Field '{field}' not found or Roll No. '{roll}' not found.")

    def save_student_data(self, students):
        if students and isinstance(students, list) and len(students) > 0:
            fieldnames = students[0].keys()  # Get keys from the first student's dictionary
            with open('rikami.csv', 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for student in students:
                    writer.writerow(student)
        else:
            print("No student data to save.")

    def verify_admin(self, username, password):
        """Verifies admin credentials."""
        return username == "admin" and password == "admin123" 

def mark_attendance(self, roll, status):
    """Marks attendance for a student and updates their attendance record."""
    students = self.load_student_data()
    for student in students:
        if student["Roll No."] == roll:
            attendance_record = student.get("attendance_count", 0)
            student["attendance_count"] = int(attendance_record) + 1
            total_classes = 100 
            student["average_attendance"] = f"{(int(attendance_record) + 1) / total_classes * 100:.2f}%"
            print(f"Marked {status} for Roll No. {roll} on {datetime.now()}.")

            # Store attendance record in attendance_records.txt
            with open("attendance_records.txt", "a") as file:
                file.write(f"{datetime.now()}: Marked {status} for Roll No. {roll}\n")
            break
    self.save_student_data(students)


class WelcomePage(tk.Frame):
    """Welcome page with search functionality."""
    def __init__(self, master, show_page):
        super().__init__(master)
        self.master = master
        self.show_page = show_page
        self.configure(bg="#f8f8f8")



        # Welcome Text
        welcome_label = tk.Label(self, text="Welcome", font=("Arial", 24), bg="#f8f8f8", fg="black")
        welcome_label.pack(pady=20)

        # Main Frame for Search
        main_frame = tk.Frame(self, bg="#f8f8f8")
        main_frame.pack(pady=40)

        # Search Entry
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(main_frame, textvariable=self.search_var, font=("Arial", 16), width=30, justify='center')
        search_entry.insert(0, "Enter here to Search")
        search_entry.configure(state='disabled')

        def on_click(event):
            search_entry.configure(state='normal')
            search_entry.delete(0, "end")

        search_entry.bind("<Button-1>", on_click)
        search_entry.grid(row=0, column=0, padx=10, pady=10)

        # Search Button
        search_button = tk.Button(main_frame, text="Search", font=("Arial", 12), bg="#444", fg="white", width=10, 
                                   command=self.search_student)
        search_button.grid(row=1, column=0, padx=10, pady=10)

        # Dropdown for Search Criteria
        self.search_by_var = tk.StringVar(value="by Roll Number")
        search_by_dropdown = ttk.Combobox(main_frame, textvariable=self.search_by_var, state="readonly", font=("Arial", 12))
        search_by_dropdown['values'] = ("by Name", "by Number", "by Roll Number")
        search_by_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Refresh Label (Placeholder)
        refresh_label = tk.Label(self, text="Refresh", font=("Arial", 10), fg="blue", bg="#f8f8f8", cursor="hand2")
        refresh_label.pack(anchor='ne', padx=20, pady=10)

    def search_student(self):
        """Searches for a student and displays their profile."""
        search_criteria = self.search_by_var.get()
        search_term = self.search_var.get().strip()
        backend = Backend()  # Create an instance of the backend
        student_data = None
        if search_criteria == "by Name":
            for student in backend.load_student_data():
                if search_term.lower() in student["Name of Student"].lower():
                    student_data = student
                    break
        elif search_criteria == "by Number":
            for student in backend.load_student_data():
                if search_term in student["Student Mo."] or search_term in student["Parents Mo."]:
                    student_data = student
                    break
        elif search_criteria == "by Roll Number":
            student_data = backend.get_student_by_roll(search_term)

        if student_data:
            self.show_page("StudentProfile", student_data)
        else:
            messagebox.showinfo("Not Found", "No student found matching the criteria.")

class StudentProfile(tk.Frame):
    """Displays a student's profile."""
    def __init__(self, master, show_edit_page):
        super().__init__(master)
        self.master = master
        self.show_edit_page = show_edit_page
        self.configure(bg="#f8f8f8")

        # ... (Header Frame and Navigation Buttons - Same as in WelcomePage) ... 

        # Profile Page Title
        profile_label = tk.Label(self, text="Student Profile", font=("Arial", 24), bg="#f8f8f8", fg="black")
        profile_label.pack(pady=20)

        # Main Frame for Profile Information
        main_frame = tk.Frame(self, bg="#f8f8f8")
        main_frame.pack(pady=20)

        # Left Frame for Profile Picture
        left_frame = tk.Frame(main_frame, bg="#f8f8f8")
        left_frame.pack(side=tk.LEFT, padx=20)

        # Load Profile Picture
        try:
            img = Image.open("profile.jpg")
            img = img.resize((150, 150), Image.LANCZOS)
            profile_pic = ImageTk.PhotoImage(img)
            profile_pic_label = tk.Label(left_frame, image=profile_pic, bg="#f8f8f8")
            profile_pic_label.image = profile_pic  # Keep a reference
            profile_pic_label.pack()
        except Exception as e:
            print(f"Error loading profile picture: {e}")
                # Right Frame for Profile Information
        right_frame = tk.Frame(main_frame, bg="#ffffff", relief=tk.RIDGE, borderwidth=2, padx=10, pady=10, width=400, height=400)
        right_frame.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)

        # NAME
        self.name_label = tk.Label(right_frame, text="NAME:", font=("Arial", 12), bg="#ffffff", fg="black")
        self.name_label.grid(row=0, column=0, sticky='w', pady=5)

        self.name_value = tk.Label(right_frame, font=("Arial", 12, "bold"), bg="#ffffff", fg="black")
        self.name_value.grid(row=0, column=1, sticky='w', pady=5)

        # Roll Number
        self.roll_label = tk.Label(right_frame, text="Roll Number:", font=("Arial", 12), bg="#ffffff", fg="green")
        self.roll_label.grid(row=1, column=0, sticky='w', pady=(2,5))

        self.roll_value = tk.Label(right_frame, font=("Arial", 24, "bold"), bg="#ffffff", fg="black")
        self.roll_value.grid(row=1, column=1, sticky='w', pady=5)

        # Enrollment Number
        self.enrollment_label = tk.Label(right_frame, text="Enrollment Number:", font=("Arial", 10), bg="#ffffff", fg="black")
        self.enrollment_label.grid(row=2, column=0, sticky='w', pady=5)

        self.enrollment_value = tk.Label(right_frame, font=("Arial", 10), bg="#ffffff", fg="black")
        self.enrollment_value.grid(row=2, column=1, sticky='w', pady=5)

        # Student Contact
        self.contact_label = tk.Label(right_frame, text="Student Contact:", font=("Arial", 10), bg="#ffffff", fg="black")
        self.contact_label.grid(row=3, column=0, sticky='w', pady=5)

        self.contact_value = tk.Label(right_frame, font=("Arial", 10), bg="#ffffff", fg="gray")
        self.contact_value.grid(row=3, column=1, sticky='w', pady=5)

        # Parents Contact Number
        self.parent_contact_label = tk.Label(right_frame, text="Parents Contact Number:", font=("Arial", 10), bg="#ffffff", fg="black")
        self.parent_contact_label.grid(row=4, column=0, sticky='w', pady=5)

        self.parent_contact_value = tk.Label(right_frame, font=("Arial", 10), bg="#ffffff", fg="gray")
        self.parent_contact_value.grid(row=4, column=1, sticky='w', pady=5)

        # Email
        self.email_label = tk.Label(right_frame, text="Email:", font=("Arial", 10), bg="#ffffff", fg="black")
        self.email_label.grid(row=5, column=0, sticky='w', pady=5)

        self.email_value = tk.Label(right_frame, font=("Arial", 10), bg="#ffffff", fg="gray")
        self.email_value.grid(row=5, column=1, sticky='w', pady=5)

        # University ID
        self.university_id_label = tk.Label(right_frame, text="University ID:", font=("Arial", 10), bg="#ffffff", fg="black")
        self.university_id_label.grid(row=6, column=0, sticky='w', pady=5)

        self.university_id_value = tk.Label(right_frame, font=("Arial", 10), bg="#ffffff", fg="gray")
        self.university_id_value.grid(row=6, column=1, sticky='w', pady=5)
        # Edit Information Button
        self.edit_button = tk.Button(self, text="Edit Information", font=("Arial", 12), bg="#444", fg="white", command=self.edit_information)
        self.edit_button.pack(pady=10)

        # Refresh Label (Placeholder)
        refresh_label = tk.Label(self, text="Refresh", font=("Arial", 10), fg="blue", bg="#f8f8f8", cursor="hand2")
        refresh_label.pack(anchor='ne', padx=20, pady=10)

    def load_student_data(self, student_data):
        """Loads student data into the profile labels."""
        # Update profile labels with student data
        self.name_value.config(text=student_data.get("Name of Student"))
        self.roll_value.config(text=student_data.get("Roll No."))
        self.enrollment_value.config(text=student_data.get("Enrollment No."))
        self.contact_value.config(text=student_data.get("Student Mo."))
        self.parent_contact_value.config(text=student_data.get("Parents Mo."))
        self.email_value.config(text=student_data.get("E-mail"))
        self.university_id_value.config(text=student_data.get("user id"))

        if "NULL" in student_data.values():
            self.edit_button.config(state="normal")
        else:
            self.edit_button.config(state="disabled")

    def edit_information(self):
        """Calls the show_edit_page function to display the edit page."""
        roll_number = self.roll_value.cget("text")
        self.show_edit_page(roll_number)

class EditInformationPage(tk.Frame):
    """Page for editing student information."""
    def __init__(self, master, backend, return_to_profile):
        super().__init__(master)
        self.master = master
        self.backend = backend
        self.return_to_profile = return_to_profile
        self.configure(bg="#f8f8f8")

        # ... (Header Frame and Navigation Buttons - Same as in WelcomePage) ...

        # Page Title
        edit_label = tk.Label(self, text="Edit Information", font=("Arial", 24), bg="#f8f8f8", fg="black")
        edit_label.pack(pady=20)

        # Frame for Edit Options and Input
        main_frame = tk.Frame(self, bg="#f8f8f8")
        main_frame.pack(pady=20)

        # Dropdown to select information type
        info_type_label = tk.Label(main_frame, text="Select Information to Edit:", font=("Arial", 12), 
                                     bg="#f8f8f8", fg="black")
        info_type_label.grid(row=0, column=0, sticky="w", pady=10)

        self.info_type_var = tk.StringVar()
        info_type_dropdown = ttk.Combobox(main_frame, textvariable=self.info_type_var, font=("Arial", 10), state="readonly")
        info_type_dropdown['values'] = ("Student Contact Number", "Parent's Contact Number", "Student Email", "Student ID")
        info_type_dropdown.grid(row=0, column=1, pady=10, padx=10)
        info_type_dropdown.current(0)

        # Entry field for new information
        input_label = tk.Label(main_frame, text="Enter New Information:", font=("Arial", 12), bg="#f8f8f8", fg="black")
        input_label.grid(row=1, column=0, sticky="w", pady=10)

        self.new_info_entry = tk.Entry(main_frame, font=("Arial", 12), width=30, fg="grey", relief=tk.GROOVE, bd=1)
        self.new_info_entry.insert(0, "Enter new information here...")
        self.new_info_entry.bind("<FocusIn>", self.on_entry_click)
        self.new_info_entry.bind("<FocusOut>", self.on_focusout)
        self.new_info_entry.grid(row=1, column=1, pady=10, padx=10)

        # Update Button
        update_button = tk.Button(self, text="Update Information", font=("Arial", 12), bg="#444", fg="white", command=self.update_info)
        update_button.pack(pady=20)

    def on_entry_click(self, event):
        """Clears the placeholder text in the entry field."""
        if self.new_info_entry.get() == "Enter new information here...":
            self.new_info_entry.delete(0, "end")
            self.new_info_entry.config(fg="black")

    def on_focusout(self, event):
        """Restores placeholder text if the entry field is empty."""
        if self.new_info_entry.get() == "":
            self.new_info_entry.insert(0, "Enter new information here...")
            self.new_info_entry.config(fg="grey")

    def update_info(self):
        """Updates student information in the backend."""
        selected_type = self.info_type_var.get()
        new_info = self.new_info_entry.get()
        roll_number = self.roll_value.cget("text") 

        field_mapping = {
            "Student Contact Number": "Student Mo.",
            "Parent's Contact Number": "Parents Mo.",
            "Student Email": "E-mail",
            "Student ID": "user id" 
        }

        field_to_update = field_mapping.get(selected_type)
        if field_to_update:
            self.backend.update_student_info(roll_number, field_to_update, new_info)
            messagebox.showinfo("Success", "Information updated successfully!")
            self.return_to_profile()
        else:
            messagebox.showerror("Error", "Invalid information type selected.")

    def load_student_data(self, roll_number):
        """Loads the student data for the given roll number."""
        student_data = self.backend.get_student_by_roll(roll_number)
        if student_data:
            self.roll_value = tk.Label(self, text=student_data.get("Roll No.", "N/A"), 
                                         font=("Arial", 24, "bold"), bg="#ffffff", fg="black")
            # ... (Potentially load other student data into labels for display) ...

class AttendanceReportPage(tk.Frame):
    """Displays the attendance report."""
    def __init__(self, master, show_page):
        super().__init__(master)
        self.master = master
        self.show_page = show_page 
        self.configure(bg="#f8f8f8")

        # ... (GUI elements from "attendance_report_page.txt") ...
        header_frame = tk.Frame(self, bg="#dedede", height=50)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        # Get Attendance Button 
        tk.Button(header_frame, text="Get Attendance", command=lambda: self.show_page("LoginPage", target_page="AttendancePopup")).pack(side="right", padx=20)

        # Table for attendance report
        table_frame = tk.Frame(self)
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = ("name", "section", "semester", "attendance_count", "avg")
        attendance_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
        
        # Set up headings
        attendance_table.heading("name", text="Name")
        attendance_table.heading("section", text="Section")
        attendance_table.heading("semester", text="Semester")
        attendance_table.heading("attendance_count", text="Attendance Count")
        attendance_table.heading("avg", text="Avg")
        
        # Set up column properties
        attendance_table.column("name", anchor="center", width=150)
        attendance_table.column("section", anchor="center", width=100)
        attendance_table.column("semester", anchor="center", width=100)
        attendance_table.column("attendance_count", anchor="center", width=150)
        attendance_table.column("avg", anchor="center", width=100)

        # Pack the table into the frame
        attendance_table.pack(fill="both", expand=True)

        # You can also add a scrollbar if needed
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=attendance_table.yview)
        attendance_table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

        # You can also populate the table with data from attendance_records.txt here

class LoginPage(tk.Frame):
    """Login page for admin verification."""
    def __init__(self, master, handle_login):
        super().__init__(master)
        self.master = master
        self.handle_login = handle_login 
        self.configure(bg="#333333")

        # Create the background frame
        background_frame = ttk.Frame(self, style="Background.TFrame")
        background_frame.pack(fill="both", expand=True)

        # Create the login form frame
        login_frame = ttk.Frame(background_frame, style="Form.TFrame")
        login_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        # ... (Title, Subject ID, Password labels and entry fields from "login_page.txt") ...
        # Title
        title_label = tk.Label(login_frame, text="Login", font=("Arial", 24), bg="#333333", fg="white")
        title_label.pack(pady=10)

        # Subject ID Entry
        subject_id_label = tk.Label(login_frame, text="Username:", font=("Arial", 12), bg="#333333", fg="white")
        subject_id_label.pack(pady=5)
        self.subject_id_entry = ttk.Entry(login_frame, font=("Arial", 12))
        self.subject_id_entry.pack(pady=5)

        # Password Entry
        password_label = tk.Label(login_frame, text="Password:", font=("Arial", 12), bg="#333333", fg="white")
        password_label.pack(pady=5)
        self.password_entry = ttk.Entry(login_frame, font=("Arial", 12), show="*")
        self.password_entry.pack(pady=5)

        # Create the login button
        login_button = ttk.Button(login_frame, text="Login", command=self.attempt_login, style="Button.TButton")
        login_button.pack(pady=15)

        # ... (Disclaimer Label and Style definitions from "login_page.txt") ...
        disclaimer_label = tk.Label(login_frame, text="Please enter your credentials.", font=("Arial", 10), bg="#333333", fg="white")
        disclaimer_label.pack(pady=5)

    def attempt_login(self):
        """Verifies login credentials and calls handle_login."""
        username = self.subject_id_entry.get()
        password = self.password_entry.get()
        self.handle_login(username, password)  

class AttendancePopup(tk.Toplevel):
    """Popup window for marking student attendance."""
    def __init__(self, master, students):
        self.master = master
        self.students = students
        self.current_student_index = 0  # Start with the first student
        self.master.withdraw()  # Hide the main window

        # Setup for attendance popup window
        self.popup = tk.Toplevel(self.master)
        self.popup.title("Attendance")
        self.popup.geometry("500x400")
        self.popup.resizable(False, False)
        self.popup.configure(bg="white")

        # Center the popup on the screen
        self.popup.update_idletasks()
        width = self.popup.winfo_width()
        height = self.popup.winfo_height()
        x = (self.popup.winfo_screenwidth() // 2) - (width // 2)
        y = (self.popup.winfo_screenheight() // 2) - (height // 2)
        self.popup.geometry(f"+{x}+{y}")

        # Profile picture placeholder
        try:
            profile_image = Image.open("profile.jpg").resize((80, 80), Image.LANCZOS)
            self.profile_photo = ImageTk.PhotoImage(profile_image)
        except Exception as e:
            print(f"Error loading profile picture: {e}")
            self.profile_photo = None

        # Student Information Display
        self.student_frame = tk.Frame(self.popup, bg="white")
        self.student_frame.pack(pady=20)

        # Display profile picture
        if self.profile_photo:
            self.photo_label = tk.Label(self.student_frame, image=self.profile_photo, bg="white")
            self.photo_label.grid(row=0, column=0, rowspan=4, padx=(0, 20), pady=10)

        # Labels for student information
        self.name_label = tk.Label(self.student_frame, text="", font=("Arial", 12), bg="white")
        self.name_label.grid(row=0, column=1, sticky="w")
        self.roll_label = tk.Label(self.student_frame, text="", font=("Arial", 12), bg="white")
        self.roll_label.grid(row=1, column=1, sticky="w")
        self.contact_label = tk.Label(self.student_frame, text="", font=("Arial", 12), bg="white")
        self.contact_label.grid(row=2, column=1, sticky="w")
        self.enrollment_label = tk.Label(self.student_frame, text="", font=("Arial", 12), bg="white")
        self.enrollment_label.grid(row=3, column=1, sticky="w")

        # Attendance buttons
        self.attend_button = tk.Button(self.popup, text="Attend", command=lambda: self.mark_attendance("Present"),
                                       bg="green", fg="white")
        self.attend_button.pack(pady=(20, 10))

        self.reject_button = tk.Button(self.popup, text="Reject", command=lambda: self.mark_attendance("Absent"),
                                       bg="red", fg="white")
        self.reject_button.pack(pady=(0, 20))

        # Navigation arrows
        self.left_arrow = tk.Button(self.popup, text="<", command=self.prev_student)
        self.left_arrow.place(relx=0.05, rely=0.5, anchor="center")

        self.right_arrow = tk.Button(self.popup, text=">", command=self.next_student)
        self.right_arrow.place(relx=0.95, rely=0.5, anchor="center")

        # Load initial student data
        self.load_student_data()

        # Handle popup close event
        self.popup.protocol("WM_DELETE_WINDOW", self.close_popup)

    def load_student_data(self):
        """Load and display the current student's data."""
        student = self.students[self.current_student_index]
        self.name_label.config(text=f"Name: {student.get('Name of Student', 'N/A')}")
        self.roll_label.config(text=f"Roll Number: {student.get('Roll No.', 'N/A')}")
        self.contact_label.config(text=f"Contact: {student.get('Student Mo.', 'N/A')}")
        self.enrollment_label.config(text=f"Enrollment: {student.get('Enrollment No.', 'N/A')}")

    def mark_attendance(self, status):
        """Marks the student as present or absent and saves the record."""
        student = self.students[self.current_student_index]
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("attendance_records.txt", "a") as f:
            f.write(f"{date_time}, Name: {student['name']}, Roll Number: {student['roll_number']}, Status: {status}\n")
        messagebox.showinfo("Attendance", f"Marked as {status}")
        self.next_student()  # Move to the next student

    def prev_student(self):
        """Navigate to the previous student."""
        self.current_student_index = (self.current_student_index - 1) % len(self.students)
        self.load_student_data()

    def next_student(self):
        """Navigate to the next student."""
        self.current_student_index = (self.current_student_index + 1) % len(self.students)
        self.load_student_data()

    def close_popup(self):
        """Close the popup and show the main window again if needed."""
        self.popup.destroy()
        self.master.deiconify()

class StudentAdminPage(tk.Frame):
    """Page displaying a list of students for admin view."""
    def __init__(self, master, backend, open_student_profile):
        super().__init__(master)
        self.master = master
        self.backend = backend
        self.open_student_profile = open_student_profile
        self.configure(bg="#f8f8f8")

        # ... (Header Frame and Navigation Buttons - Same as in WelcomePage) ...

        # Page Title
        title = tk.Label(self, text="Student Information", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Table for Student Information
        columns = ("roll", "name", "enrollment", "phone")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.heading("roll", text="Roll Number")
        self.tree.heading("name", text="Name")
        self.tree.heading("enrollment", text="Enrollment Number")
        self.tree.heading("phone", text="Phone Number")

        # Load student data from the backend
        for student in self.backend.load_student_data():
            self.tree.insert("", tk.END, values=(student["Roll No."], student["Name of Student"], 
                                                 student["Enrollment No."], student["Student Mo."]))

        # Attach double-click event to open profile
        self.tree.bind("<Double-1>", self.open_profile)
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

    def open_profile(self, event):
        """Opens the profile of the selected student."""
        selected_item = self.tree.selection()
        if selected_item:
            item=self.tree.item(selected_item)
            roll_number = str(item['values'][0])  # Assuming roll number is the first element
            print(f"Selected Roll Number: {roll_number}")  # Debug print
            student_data = self.backend.get_student_by_roll(roll_number)
            if student_data:
                print(f"Opening profile for: {student_data}")  # Debug print
                self.open_student_profile(roll_number)
            else:
                print(f"No student found with Roll No. {roll_number}")  # Debug print

class MainController:
    """Controls the flow of the application and manages pages."""
    def __init__(self, root):
        self.root = root
        self.root.title("Student Information System")
        self.target_page = None
        
        # Create a header frame
        self.header_frame = tk.Frame(self.root, bg="#dedede", height=50)
        self.header_frame.pack(fill=tk.X, side=tk.TOP)

        # Navigation Buttons
        home_btn = tk.Button(self.header_frame, text="Home", font=("Arial", 12), relief=tk.FLAT, bg="#dedede", fg="black", 
                             command=lambda: self.show_page("WelcomePage"))
        home_btn.pack(side=tk.LEFT, padx=20, pady=10)

        details_btn = tk.Button(self.header_frame, text="Report", font=("Arial", 12), relief=tk.FLAT, bg="#dedede", fg="black", 
                             command=lambda: self.show_page("AttendanceReportPage"))
        details_btn.pack(side=tk.LEFT, padx=20, pady=10)

        student_btn = tk.Button(self.header_frame, text="Student", font=("Arial", 12), relief=tk.FLAT, bg="#dedede", fg="black", 
                             command=lambda: self.show_page("LoginPage", target_page="StudentAdminPage"))
        student_btn.pack(side=tk.LEFT, padx=20, pady=10)

        self.backend = Backend()
        self.pages = {}
        self.create_pages()
        self.show_page("WelcomePage") 

    def create_pages(self):
        """Creates instances of all pages and stores them in a dictionary."""
        self.pages["WelcomePage"] = WelcomePage(self.root, self.show_page)
        self.pages["LoginPage"] = LoginPage(self.root, self.handle_login)
        self.pages["StudentProfile"] = StudentProfile(self.root, self.show_edit_page)
        self.pages["EditInformationPage"] = EditInformationPage(self.root, self.backend, self.return_to_profile)
        self.pages["StudentAdminPage"] = StudentAdminPage(self.root, self.backend, self.open_student_profile)
        self.pages["AttendanceReportPage"] = AttendanceReportPage(self.root, self.show_page)
        self.pages["AttendancePopup"] = None  # Initialize AttendancePopup as None

        for page in self.pages.values():
            if page:  # Check if page is not None (for AttendancePopup)
                page.pack(fill=tk.BOTH, expand=True)  # Use pack instead of grid
                page.pack_forget()  # Hide all pages initially

    def show_page(self, page_name, student_data=None, target_page=None):
        """Displays the specified page."""
        if page_name == "LoginPage" and target_page:
            self.target_page = target_page  # Store target page for post-login navigation

        # Create AttendancePopup when needed
        if page_name == "AttendancePopup":
            students = self.backend.load_student_data()  # Load students from CSV
            self.pages["AttendancePopup"] = AttendancePopup(self.root, students)
        else:
            page = self.pages.get(page_name)
            if page:
                page.pack(fill=tk.BOTH, expand=True)  # Show the page
                if page_name == "StudentProfile":
                    page.load_student_data(student_data)

        # Hide other pages
        for other_page_name, other_page in self.pages.items():
            if other_page and other_page_name != page_name:
                other_page.pack_forget()

    def handle_login(self, username, password):
        """Handles admin login attempts."""
        if self.backend.verify_admin(username, password):
             # Navigate to the stored target page if it exists, otherwise default to StudentAdminPage
            self.show_page(self.target_page if self.target_page else "StudentAdminPage")
            self.target_page = None  # Clear the target page after navigation
        
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")

    def show_edit_page(self, roll_number):
        """Displays the Edit Information page for a specific student."""
        edit_page = self.pages["EditInformationPage"]
        edit_page.load_student_data(roll_number)
        self.show_page("EditInformationPage")

    def return_to_profile(self):
        """Returns to the Student Profile page."""
        self.show_page("StudentProfile")

    def open_student_profile(self, roll_number):
        """Opens the profile page for a specific student."""
        student_data = self.backend.get_student_by_roll(roll_number)
        if student_data:
            self.show_page("StudentProfile", student_data)
    

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")

    app = MainController(root)
    
    root.mainloop()
    os.system('cls')
    
