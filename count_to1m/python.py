import time

one_million = list(range(1, 1000001))


start_time = time.time()

for number in one_million:
    print(number)

# count = 0
# while count < 1000000:
#     print(count)
#     count += 1

end_time = time.time()

execution_time = end_time - start_time

print(f"The loop took {execution_time} seconds to execute.")
