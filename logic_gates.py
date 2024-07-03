import tkinter as tk
from tkinter import Text, Scrollbar
import sqlite3

class StudentInfoGUI:
    def __init__(self, master):  # Corrected __init__ method
        self.master = master
        master.title("Student Information")
        master.geometry("800x600")

        # Create a connection to the SQLite database
        self.conn = sqlite3.connect('student_info.db')
        self.cursor = self.conn.cursor()

        # Create tables if they don't exist
        self.create_tables()

        # Create a frame for the input fields
        self.input_frame = tk.Frame(master, bg="#f0f0f0")
        self.input_frame.pack(padx=20, pady=20)

        # Create labels and entry fields
        self.roll_number_label = tk.Label(self.input_frame, text="Roll Number:", font=("Arial", 12))
        self.roll_number_label.grid(row=0, column=0, padx=10, pady=10)
        self.roll_number_entry = tk.Entry(self.input_frame, width=30, font=("Arial", 12))
        self.roll_number_entry.grid(row=0, column=1, padx=10, pady=10)

        self.num_people_label = tk.Label(self.input_frame, text="Number of People:", font=("Arial", 12))
        self.num_people_label.grid(row=1, column=0, padx=10, pady=10)
        self.num_people_entry = tk.Entry(self.input_frame, width=30, font=("Arial", 12))
        self.num_people_entry.grid(row=1, column=1, padx=10, pady=10)

        # Create an upload button
        self.upload_button = tk.Button(self.input_frame, text="Upload", command=self.upload_options, font=("Arial", 12), bg="#007bff", fg="white")
        self.upload_button.grid(row=2, column=1, padx=10, pady=10)

        # Create a frame for the save and view buttons
        self.button_frame = tk.Frame(self.input_frame, bg="#f0f0f0")
        self.button_frame.grid(row=3, column=1, padx=10, pady=10)

        # Create a save button
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_info, font=("Arial", 12), bg="#007bff", fg="white", state=tk.DISABLED)
        self.save_button.grid(row=0, column=0, padx=10, pady=10)

        # Create a view button
        self.view_button = tk.Button(self.button_frame, text="View", command=self.view_info, font=("Arial", 12), bg="#007bff", fg="white", state=tk.DISABLED)
        self.view_button.grid(row=0, column=1, padx=10, pady=10)

        # Create frames for the previous information
        self.prev_frame = tk.Frame(master, bg="#f0f0f0")
        self.prev_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Create frames and Text widgets for single student and group project information
        self.single_student_frame = tk.Frame(self.prev_frame)
        self.single_student_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.single_student_label = tk.Label(self.single_student_frame, text="Single Student PPTs", font=("Arial", 14))
        self.single_student_label.pack()

        self.single_student_text = Text(self.single_student_frame, wrap=tk.WORD, font=("Arial", 12), height=15, width=35)
        self.single_student_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.single_student_scrollbar = Scrollbar(self.single_student_frame, command=self.single_student_text.yview)
        self.single_student_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.single_student_text.config(yscrollcommand=self.single_student_scrollbar.set)

        self.group_project_frame = tk.Frame(self.prev_frame)
        self.group_project_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.group_project_label = tk.Label(self.group_project_frame, text="Group Projects", font=("Arial", 14))
        self.group_project_label.pack()

        self.group_project_text = Text(self.group_project_frame, wrap=tk.WORD, font=("Arial", 12), height=15, width=35)
        self.group_project_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.group_project_scrollbar = Scrollbar(self.group_project_frame, command=self.group_project_text.yview)
        self.group_project_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.group_project_text.config(yscrollcommand=self.group_project_scrollbar.set)

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS single_student (
                roll_number TEXT PRIMARY KEY,
                num_people INTEGER,
                ppt_title TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS group_project (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                roll_number1 TEXT,
                roll_number2 TEXT,
                roll_number3 TEXT,
                roll_number4 TEXT,
                num_people INTEGER,
                project_title TEXT
            )
        ''')
        self.conn.commit()

    def fetch_single_student_info(self, roll_number):
        self.cursor.execute('SELECT * FROM single_student WHERE roll_number=?', (roll_number,))
        return self.cursor.fetchone()

    def upload_options(self):
        num_people = int(self.num_people_entry.get())

        # Clear existing dynamic widgets
        for widget in self.input_frame.grid_slaves():
            if int(widget.grid_info()["row"]) > 3:
                widget.grid_forget()

        if num_people == 1:
            self.ppt_title_label = tk.Label(self.input_frame, text="PPT Title:", font=("Arial", 12))
            self.ppt_title_label.grid(row=4, column=0, padx=10, pady=10)
            self.ppt_title_entry = tk.Entry(self.input_frame, width=30, font=("Arial", 12))
            self.ppt_title_entry.grid(row=4, column=1, padx=10, pady=10)

            # Fetch and display previous single student info if available
            roll_number = self.roll_number_entry.get()
            student_info = self.fetch_single_student_info(roll_number)
            if student_info:
                _, _, ppt_title = student_info
                self.ppt_title_entry.insert(0, ppt_title)
        elif num_people == 4:
            self.roll_number_labels = []
            self.roll_number_entries = []
            for i in range(4):
                label = tk.Label(self.input_frame, text="Roll Number {}:".format(i + 1), font=("Arial", 12))
                label.grid(row=4 + i, column=0, padx=10, pady=10)
                entry = tk.Entry(self.input_frame, width=30, font=("Arial", 12))
                entry.grid(row=4 + i, column=1, padx=10, pady=10)
                self.roll_number_labels.append(label)
                self.roll_number_entries.append(entry)

            self.project_title_label = tk.Label(self.input_frame, text="Project Title:", font=("Arial", 12))
            self.project_title_label.grid(row=8, column=0, padx=10, pady=10)
            self.project_title_entry = tk.Entry(self.input_frame, width=30, font=("Arial", 12))
            self.project_title_entry.grid(row=8, column=1, padx=10, pady=10)
        else:
            error_label = tk.Label(self.input_frame, text="Invalid number of people", font=("Arial", 12), fg="red")
            error_label.grid(row=4, column=1, padx=10, pady=10)

        self.save_button.config(state=tk.NORMAL)

    def save_info(self):
        roll_number = self.roll_number_entry.get()
        num_people = int(self.num_people_entry.get())

        if num_people == 1:
            ppt_title = self.ppt_title_entry.get()
            self.cursor.execute('''
                INSERT OR REPLACE INTO single_student (roll_number, num_people, ppt_title)
                VALUES (?, ?, ?)
            ''', (roll_number, num_people, ppt_title))
            self.conn.commit()
        elif num_people == 4:
            roll_numbers = [entry.get() for entry in self.roll_number_entries]
            project_title = self.project_title_entry.get()
            self.cursor.execute('''
                INSERT INTO group_project (roll_number1, roll_number2, roll_number3, roll_number4, num_people, project_title)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (*roll_numbers, num_people, project_title))
            self.conn.commit()

        self.view_button.config(state=tk.NORMAL)

    def view_info(self):
        single_student_text = ""
        group_project_text = ""

        self.cursor.execute('SELECT * FROM single_student')
        single_students = self.cursor.fetchall()
        for student in single_students:
            single_student_text += f"Roll Number: {student[0]}\nNumber of People: {student[1]}\nPPT Title: {student[2]}\n\n"

        self.cursor.execute('SELECT * FROM group_project')
        group_projects = self.cursor.fetchall()
        for project in group_projects:
            roll_numbers = ", ".join(project[1:5])
            group_project_text += f"Roll Numbers: {roll_numbers}\nNumber of People: {project[5]}\nProject Title: {project[6]}\n\n"

        self.single_student_text.delete(1.0, tk.END)  # Clear previous content
        self.single_student_text.insert(tk.END, single_student_text)

        self.group_project_text.delete(1.0, tk.END)  # Clear previous content
        self.group_project_text.insert(tk.END, group_project_text)

root = tk.Tk()
my_gui = StudentInfoGUI(root)
root.mainloop()
