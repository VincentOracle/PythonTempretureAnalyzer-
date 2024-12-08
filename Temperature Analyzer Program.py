#!/usr/bin/env python
# coding: utf-8

# # Temperature Analyzer Program

# In[2]:


import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os

# Global temperature data
temperature_data = []

def upload_text_data():
    global temperature_data
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                temperature_data.clear()
                for line in file:
                    parts = line.strip().split()
                    month, day, year = parts[0], int(parts[1]), int(parts[2])
                    min_temp, max_temp = int(parts[3]), int(parts[4])
                    temperature_data.append({
                        "date": f"{month} {day}, {year}",
                        "min_temp": min_temp,
                        "max_temp": max_temp
                    })
                messagebox.showinfo("Success", "File uploaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

def view_data():
    if not temperature_data:
        messagebox.showwarning("No Data", "Please upload a file first!")
        return
    data_window = tk.Toplevel()
    data_window.title("View Temperature Data")
    text_area = scrolledtext.ScrolledText(data_window, wrap=tk.WORD, width=60, height=20)
    text_area.pack(padx=10, pady=10)
    for entry in temperature_data:
        text_area.insert(tk.END, f"Date: {entry['date']}, Low Temp: {entry['min_temp']}°C, High Temp: {entry['max_temp']}°C\n")

def create_stats_file():
    if not temperature_data:
        messagebox.showwarning("No Data", "Please upload a file first!")
        return
    try:
        highest_temp_day = max(temperature_data, key=lambda x: x['max_temp'])
        lowest_temp_day = min(temperature_data, key=lambda x: x['min_temp'])
        avg_max_temp = sum(d['max_temp'] for d in temperature_data) / len(temperature_data)
        month_days = {}

        for entry in temperature_data:
            month = entry['date'].split()[0]
            month_days[month] = month_days.get(month, 0) + 1

        with open("stats.txt", "w") as file:
            file.write(f"Day with the highest temp: {highest_temp_day['date']} ({highest_temp_day['max_temp']}°C)\n")
            file.write(f"Day with the lowest temp: {lowest_temp_day['date']} ({lowest_temp_day['min_temp']}°C)\n")
            file.write(f"Avg of highest temps: {avg_max_temp:.1f}°C\n")
            file.write("Days data collected per month:\n")
            for month, days in month_days.items():
                file.write(f"  - {month}: {days} days\n")

        messagebox.showinfo("Success", "Statistics file created successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def print_statistics_file():
    try:
        with open("stats.txt", "r") as file:
            stats_window = tk.Toplevel()
            stats_window.title("Statistics")
            text_area = scrolledtext.ScrolledText(stats_window, wrap=tk.WORD, width=60, height=20)
            text_area.pack(padx=10, pady=10)
            text_area.insert(tk.END, file.read())
    except FileNotFoundError:
        messagebox.showerror("Error", "'stats.txt' not found. Generate stats first.")

def exit_program():
    if messagebox.askyesno("Exit", "Do you really want to exit?"):
        root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Temperature Analyzer Program")
root.geometry("400x300")

# Buttons with different colors
upload_btn = tk.Button(root, text="Upload Text Data", bg="#4CAF50", fg="white", font=("Arial", 12), command=upload_text_data)
upload_btn.pack(pady=10)

view_btn = tk.Button(root, text="View Data", bg="#2196F3", fg="white", font=("Arial", 12), command=view_data)
view_btn.pack(pady=10)

stats_btn = tk.Button(root, text="Download Statistics", bg="#FF9800", fg="white", font=("Arial", 12), command=create_stats_file)
stats_btn.pack(pady=10)

print_btn = tk.Button(root, text="Print Statistics File", bg="#9C27B0", fg="white", font=("Arial", 12), command=print_statistics_file)
print_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit Program", bg="#F44336", fg="white", font=("Arial", 12), command=exit_program)
exit_btn.pack(pady=10)

root.mainloop()


# In[ ]:




