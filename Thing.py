import tkinter as tk
from tkinter import messagebox
import json

class ActivityRepositoryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Activity Repository")
        self.activities = []
        self.label_name = tk.Label(master, text="Activity Name:")
        self.label_name.grid(row=0, column=0, sticky=tk.W)
        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1)

        self.label_category = tk.Label(master, text="Category:")
        self.label_category.grid(row=1, column=0, sticky=tk.W)
        self.entry_category = tk.Entry(master)
        self.entry_category.grid(row=1, column=1)

        self.save_button = tk.Button(master, text="Save Activity", command=self.save_activity)
        self.save_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.label_filter = tk.Label(master, text="Filter by Category:")
        self.label_filter.grid(row=3, column=0, sticky=tk.W)
        self.filter_var = tk.StringVar()
        self.filter_entry = tk.Entry(master, textvariable=self.filter_var)
        self.filter_entry.grid(row=3, column=1)
        self.filter_button = tk.Button(master, text="Filter", command=self.filter_activities)
        self.filter_button.grid(row=3, column=2)

        self.activity_listbox = tk.Listbox(master, width=50)
        self.activity_listbox.grid(row=4, column=0, columnspan=3)
        self.label_lesson_plan = tk.Label(master, text="Lesson Plan:")
        self.label_lesson_plan.grid(row=5, column=0, sticky=tk.W)
        self.lesson_plan_text = tk.Text(master, width=50, height=10)
        self.lesson_plan_text.grid(row=6, column=0, columnspan=3)

    def save_activity(self):
        name = self.entry_name.get()
        category = self.entry_category.get()

        if name and category:
            activity = {"name": name, "category": category}
            self.activities.append(activity)
            self.save_to_file()
            self.update_activity_listbox()
            messagebox.showinfo("Success", "Activity saved successfully!")
        else:
            messagebox.showerror("Error", "Please enter activity name and category.")

    def save_to_file(self):
        with open("activities.json", "w") as file:
            json.dump(self.activities, file)

    def load_from_file(self):
        try:
            with open("activities.json", "r") as file:
                self.activities = json.load(file)
        except FileNotFoundError:
            pass

    def update_activity_listbox(self):
        self.activity_listbox.delete(0, tk.END)
        for activity in self.activities:
            self.activity_listbox.insert(tk.END, f"{activity['name']} ({activity['category']})")

    def filter_activities(self):
        filter_text = self.filter_var.get()
        filtered_activities = [activity for activity in self.activities if filter_text.lower() in activity['category'].lower()]
        self.activity_listbox.delete(0, tk.END)
        for activity in filtered_activities:
            self.activity_listbox.insert(tk.END, f"{activity['name']} ({activity['category']})")

root = tk.Tk()
app = ActivityRepositoryApp(root)
root.mainloop()