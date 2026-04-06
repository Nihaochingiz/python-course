time_mins = int(input())
start_hours = int(input())
start_mins = int(input())

total_start_mins = start_hours * 60 + start_mins

total_end_mins = total_start_mins + time_mins

end_hours = total_end_mins // 60 % 24  # % 24 для 24-часового формата
end_mins = total_end_mins % 60

print(end_hours, end_mins)