import time


def say_hello(x: int):
    time.sleep(1)  # simulate I/O blocking call
    print(f"{time.strftime('%X')} - Hello world {x}")


print(f"{time.strftime('%X')} - Started")
for i in range(5):
    say_hello(i)
