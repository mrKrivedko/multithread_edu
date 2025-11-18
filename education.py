# import threading


# def task():
#     raise ValueError("ops, ValueError")


# def handler():
#     try:
#         task()
#     except ValueError as error:
#         print(error)


# thread = threading.Thread(target=handler)
# thread.start()


# import threading


# def test_1():
#     raise TypeError("some error")

# def test_2():
#     raise SyntaxError("some error")

# def test_3():
#     raise ZeroDivisionError("some error")

# def test_4():
#     raise SyntaxError("some error")


# for function in (test_1, test_2, test_3, test_4):
#     threading.Thread(target=function).start()

# print("А главному потоку все равно")


# import threading


# flag = False


# def custom_hook(args):
#     global flag
#     exc_type, exc_value, exc_traceback, exc_thread = args
#     print(f"Exception {exc_type.__name__} {exc_value} in thread {exc_thread.name}")
#     flag = True


# threading.excepthook = custom_hook


# def test():
#     raise RuntimeError("some error")


# thread = threading.Thread(target=test)
# thread.start()
# thread.join()

# if flag:
#     raise RuntimeError("Допонительный поток завершился с исключением")
# print("А главному потоку все равно")


# import threading
# import time


# def test():
#     raise ValueError("error")


# def work():
#     for _ in range(5):
#         time.sleep(0.5)
#         print("i'm fine!")


# thread = threading.Thread(target=work)  # чтобы потоки не жили после краха main thread поток должен быть демоническим.
# thread.start()

# test()


# import threading
# import traceback


# def custom_hook(args):
#     exc_type, exc_value, exc_traceback, exc_thread = args
#     print(f"Exception in thread {exc_thread.name}")
#     print(*traceback.format_exception(exc_type, exc_value, exc_traceback))


# threading.excepthook = custom_hook


# def task():
#     raise ValueError("error")


# thread = threading.Thread(target=task)
# thread.start()
# thread.join()
# print("\nА главному потоку все нипочем!")


# import threading
# import traceback


# def task():
#     raise TypeError("ops, TypeError")


# def custom_hook(args):
#     exc_type, exc_value, exc_traceback, thread = args
#     print(f"Тип исключения: {exc_type.__name__}")
#     print(f"Сообщение исключения: {exc_value}")
#     print(f"Номер потока: {thread.ident}")
#     print(f"Имя потока: {thread.name}")
#     print(f"Путь исключения:")
#     traceback.print_tb(exc_traceback)


# threading.excepthook = custom_hook

# thread = threading.Thread(target=task)
# thread.start()


# import threading
# from time import sleep
# from itertools import count

# count = count()

# def trace_func(frame, event, arg):
#     print(f"{next(count)} executing trace func with {threading.current_thread().name=}")
#     print(f"{frame=}\n{event=}\n{arg=}")

# def get_inform():
#     print(f"{threading.current_thread().name=}")
#     print(f"{threading.current_thread().ident=}")
#     print(f"{threading.current_thread().native_id=}")
#     print(f"{threading.get_ident()=}")
#     print(f"{threading.get_native_id()=}")
#     print("---------------")
#     sleep(2)

# threading.settrace(trace_func)

# thr = [threading.Thread(target=get_inform) for _ in range(1)]
# for t in thr:
#     t.start()


# import sys, time
# def teleprint(*args, delay=1, str_join=' '):
#     text = str_join.join(str(x) for x in args)
#     n = len(text)
#     for i, char in enumerate(text, 1):
#         if i == n:
#             char = f'{char}\n'
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         time.sleep(delay) 

# # Строка будет печататься с задержкой, как в телетексте...
# teleprint('Печать с задержкой!', 10, 12.5, 'Super!!!', delay=0.07)

# import cProfile
# import threading
# import time

# def get_slow_inform():
#     time.sleep(1.01)
#     print(f"{threading.current_thread().name=}")


# def profile_func():
#     profiler = cProfile.Profile()
#     profiler.enable()

#     get_slow_inform()

#     profiler.disable()
#     profiler.print_stats(sort="time")


# thr = threading.Thread(target=profile_func)
# thr.start()
# thr.join()


# import cProfile
# import threading
# import time
# from functools import wraps
# from typing import Callable


# def profile_func(func: Callable):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         profiler = cProfile.Profile()
#         profiler.enable()
#         result = func(*args, **kwargs)
#         profiler.disable()
#         profiler.print_stats(sort="time")
#         return result
#     return wrapper


# @profile_func
# def get_slow_inform():
#     time.sleep(1.01)
#     print(f"{threading.current_thread().name=}")


# thr = threading.Thread(target=get_slow_inform)
# thr.start()
# thr.join()


from threading import Timer
from time import sleep


def worker(task: str):
    sleep(2)
    print(f"{task=} done")

Timer(1.0, worker, ["print"]).start()