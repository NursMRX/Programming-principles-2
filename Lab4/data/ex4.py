from datetime import datetime

start_time = datetime(2025, 2, 16, 12, 0, 0)
end_time = datetime(2025, 2, 16, 12, 7, 30)

difference = end_time - start_time
Total_seconds = difference.total_seconds()

print("Total seconds:", Total_seconds)