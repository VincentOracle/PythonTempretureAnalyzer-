#!/usr/bin/env python
# coding: utf-8

# # Temperature Analyzer Program

# In[ ]:


import os

def display_menu():
    print("\nWelcome to the Temperature Analyzer Program!")
    print("Please choose from the following options:")
    print("1. Upload text data")
    print("2. View data")
    print("3. Download statistics")
    print("4. Print statistics file")
    print("5. Exit the program")

def upload_text_data():
    global temperature_data
    file_name = input("Enter the name of the file to upload (with extension): ")
    try:
        with open(file_name, 'r') as file:
            temperature_data = []
            for line in file:
                parts = line.strip().split()
                month, day, year = parts[0], int(parts[1]), int(parts[2])
                min_temp, max_temp = int(parts[3]), int(parts[4])
                temperature_data.append({
                    "date": f"{month} {day}, {year}",
                    "min_temp": min_temp,
                    "max_temp": max_temp
                })
            print("File uploaded successfully.")
    except FileNotFoundError:
        print("Error: File not found. Please try again.")
    except Exception as e:
        print(f"Error: {e}")

def print_data():
    if not temperature_data:
        print("No data available. Please upload a file first.")
        return
    for entry in temperature_data:
        print(f"Date: {entry['date']}, Low Temperature: {entry['min_temp']}°C, High Temperature: {entry['max_temp']}°C")

def create_stats_file():
    if not temperature_data:
        print("No data available. Please upload a file first.")
        return

    highest_temp_day = max(temperature_data, key=lambda x: x['max_temp'])
    lowest_temp_day = min(temperature_data, key=lambda x: x['min_temp'])
    avg_max_temp = sum(d['max_temp'] for d in temperature_data) / len(temperature_data)

    month_days = {}
    for entry in temperature_data:
        month = entry['date'].split()[0]
        month_days[month] = month_days.get(month, 0) + 1

    with open("stats.txt", "w") as file:
        file.write(f"Day with the highest temperature: {highest_temp_day['date']} ({highest_temp_day['max_temp']}°C)\n")
        file.write(f"Day with the lowest temperature: {lowest_temp_day['date']} ({lowest_temp_day['min_temp']}°C)\n")
        file.write(f"Average of the highest temperatures for the year: {avg_max_temp:.1f}°C\n")
        file.write("Number of days data collected for each month:\n")
        for month, days in month_days.items():
            file.write(f"  - {month}: {days} days\n")

    print("Statistics file created successfully.")

def print_statistics_file():
    try:
        with open("stats.txt", "r") as file:
            print("\nStatistics File Content:")
            print(file.read())
    except FileNotFoundError:
        print("Error: 'stats.txt' not found. Please generate the statistics first.")

def main():
    global temperature_data
    temperature_data = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            upload_text_data()
        elif choice == "2":
            print_data()
        elif choice == "3":
            create_stats_file()
        elif choice == "4":
            print_statistics_file()
        elif choice == "5":
            print("Thank you for using the Temperature Analyzer Program!")
            print("Current working directory:", os.getcwd())
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


# In[ ]:




