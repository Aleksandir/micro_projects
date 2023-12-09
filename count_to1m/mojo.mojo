import time


fn main():
    let one_million = range(1, 1000001)

    var start_time = time.now()

    var count: Int = 0
    for number in one_million:
        print(count)
        count += 1

    var end_time = time.now()
    let execution_time_for = str((end_time - start_time) / 1000000000.0)

    start_time = time.now()
    count = 0
    while count < 1000000:
        print(count)
        count += 1

    end_time = time.now()
    let execution_time_while = str((end_time - start_time) / 1000000000.0)

    print("for loop completed in " + execution_time_for + " seconds.")
    print("while loop completed in " + execution_time_while + " seconds.")
