import time

one_million = list(range(1, 1000001))


start_time = time.time()

count = 0
for number in one_million:
    print(count)
    count += 1
    # if count == 1000000:
    #     print("For loop done!")

end_time = time.time()
execution_time_for = end_time - start_time

start_time = time.time()
count = 0
while count < 1000000:
    print(count)
    count += 1
    # if count == 1000000:
    #     print("While loop done!")

end_time = time.time()
execution_time_while = end_time - start_time

print(f"for loop completed in {execution_time_for} seconds.")
print(f"while loop completed in {execution_time_while} seconds.")
