from datetime import datetime
now = datetime.now()
print("Datetime with microseconds:", now)
without_microsec = now.replace(microsecond=0)
print("Datetime without microseconds:", without_microsec)