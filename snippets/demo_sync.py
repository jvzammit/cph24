import time


def say_hello(x: int):
    time.sleep(x)  # simulate I/O blocking call
    print(f"{time.strftime('%X')} - Hello world {x}")


print(f"{time.strftime('%X')} - Started")
for i in range(1, 4):
    say_hello(i)
