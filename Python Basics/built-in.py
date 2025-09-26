import math

print(math.sqrt(16))   # 4.0
print(math.factorial(5)) # 120


from random import *

print(random()) # Any number
print(randint(1, 10))  # random number between 1 and 10






# Time


import time

# 1. Get current time in seconds since epoch (Unix timestamp)
print("time.time():", time.time())

# 2. Human readable current time
print("time.ctime():", time.ctime())

# 3. Pause execution
print("\nStart sleeping for 3 seconds...")
time.sleep(3)
print("Woke up after 3 seconds!")

# 4. Local time as structured object
local_t = time.localtime()
print("\ntime.localtime():", local_t)
print("Year:", local_t.tm_year)
print("Month:", local_t.tm_mon)
print("Day:", local_t.tm_mday)
print("Hour:", local_t.tm_hour)
print("Minute:", local_t.tm_min)
print("Second:", local_t.tm_sec)

# 5. Format the current time
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_t)
print("\nFormatted time:", formatted_time)

# 6. Parse a string back into a time object
time_string = "2025-09-21 16:30:00"
parsed_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print("\nParsed time (from string):", parsed_time)

# 7. Measure execution time of some code
print("\nMeasuring execution time...")
start = time.time()
for i in range(1000000):  # dummy loop
    pass
end = time.time()
print("Execution time:", end - start, "seconds")
