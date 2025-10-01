import json
import random
import os
import datetime
import subprocess

try:
   with open("tasks.json", "r") as f:
      data = json.load(f)
except FileNotFoundError:
   data = []
   with open("tasks.json", "w") as f:
      json.dump(data, f)

new_items = []

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
week = [{day: []} for day in days_of_week]

def output_week():

   all_items = data + new_items
   local_week = {day: [] for day in days_of_week}

   for task_dict in all_items:

      for task_name, count in task_dict.items():

         if count > 7:

            count = 7
         chosen_days = random.sample(days_of_week, count)

         for day in chosen_days:
            local_week[day].append(task_name)

   print("\n--- Generated Week ---")

   if os.path.exists("schedule.txt"):
      os.remove("schedule.txt")

   with open("schedule.txt", "w") as f:

      for day in days_of_week:

         tasks = local_week[day]
         print(f"{day}: {', '.join(tasks) if tasks else 'No tasks'}")
         line = f"{day}: {', '.join(tasks) if tasks else 'No tasks'}\n"
         f.write(line)

def main():
   print("Press Enter without typing to finish adding new tasks.")

   while True:
      item = input("New task name to append:\n")

      if item.strip() == "":
         break

      try:

         times = int(input("How many times this task should appear in the week (max 7):\n"))
         times = min(times, 7)
         dictionary = {item: times}
         new_items.append(dictionary)
         with open("tasks.json", "w") as f:
            json.dump(data + new_items, f)
         

      except ValueError:

         print("Please enter a valid number.")

   output_week()
   current_dir = os.getcwd()
   subprocess.Popen(f'explorer "{current_dir}"')

if __name__ == '__main__':
   main()
