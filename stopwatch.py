import time

startTime = time.time()

input("Click enter to stop the watch...")

endTime = time.time()

elapsedTime = endTime - startTime

print(f"The elapsed time is {elapsedTime} seconds")
