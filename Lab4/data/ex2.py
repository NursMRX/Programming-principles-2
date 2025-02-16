import datetime

yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).date()
today = (datetime.datetime.now()).date()
tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).date()

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)