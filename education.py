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


# from threading import Timer
# from time import sleep


# def worker(task: str):
#     sleep(2)
#     print(f"{task=} done")

# Timer(1.0, worker, ["print"]).start()

# import threading


# class PrintThread(threading.Thread):  # наследуем оригинальный класс Thread

#     def __init__(self, text): 
#         super().__init__()
#         self.text = text
#         # выведите на печать количество активных потоков

#     def run(self):  # переопределение метода run
#         # выведите на печать количество активных потоков
#         print(self.text)


# print_thread = PrintThread("Очень простой но бесполезный пример работы отдельного потока")
# print_thread.start()


# import threading


# class TwoTaskThread(threading.Thread):  # наследуем оригинальный класс Thread

#     def __init__(self, task=None, new_task=None, args=()):
#         super().__init__()
#         self.new_task = new_task
#         self.task = task
#         self.args = args

#     def run(self):
#         try:
#             if self.task is not None:
#                 self.new_task(self.task(*self.args))
#         finally:
#             del self.task, self.args, self.new_task


# def worker(*args) -> int:
#     return sum(args)


# def handler(n):
#     print(n)


# my_thread = TwoTaskThread(worker, handler, (1, 2, 3))
# print(my_thread.task)
# print(my_thread.new_task)
# print(my_thread.args)
# my_thread.start()

# import threading
# from typing import Callable

# # Исправьте ошибки в классе
# class MyThread(threading.Thread):
#     def __init__(self, msg_error: str = "error", task: Callable = None):
#         super().__init__()
#         self.msg_error = msg_error
#         self.task = task

#     def run(self) -> None:
#         try:
#             self.task()
#         except Exception as err:
#             print(self.msg_error)

# def divzero():
#     4/1

# my_thread = MyThread('shit', divzero)
# my_thread.start()


# import threading

# # Создайте класс SimpleThread
# class SimpleThread(threading.Thread):
#     """Класс простого потока."""
    
#     def __init__(self,function=None, data=None):
#         super().__init__()
#         self.function = function
#         self.data = data

#     def run(self):
#         """Запускаем поток."""
#         if self.function is not None:
#             result = self.function(self.data)
#             print(result)

# def divzero(data):
#     print(data)
#     return 123

# data = {1: 1}
# my_thread = SimpleThread(divzero, data)
# my_thread.start()


# from functools import wraps


# class ColorDecorator:
#     def __init__(self, color: str):
#         self.reset = "\033[0m"  # дефолтный цвет в консоли
#         if color == "RED":  # поддерживаем пока только красный
#             self.color = "\033[91m"
#         else:
#             self.color = ""

#     def color_output(self, func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             if result is not None:
#                 print(f"{self.color}{func.__name__} return: {self.color}{result}{self.reset}")
#             return result
#         return wrapper

# red_decorator = ColorDecorator(color="RED")

# @red_decorator.color_output
# def read_root():
#     return {"Hello": "World"}

# # Проверяем, read_root выведет красным свой результат
# read_root()


from functools import wraps


class ColorPalette:
    """Класс для управления ANSI-цветами в консоли"""
    COLORS = {
        "RESET": "\033[0m",
        "RED": "\033[91m",
        "GREEN": "\033[92m",
        "YELLOW": "\033[93m",
        "BLUE": "\033[94m",
        "MAGENTA": "\033[95m",
        "CYAN": "\033[96m",
        "WHITE": "\033[97m",
        "GRAY": "\033[90m"
    }

    @classmethod
    def get_color(cls, color_name: str) -> str:
        """Возвращает ANSI-код цвета или пустую строку если цвет не найден"""
        return cls.COLORS.get(color_name.upper(), "")


class ColorDecorator:
    def __init__(self, color: str):
        self.color = ColorPalette.get_color(color)
        self.reset = ColorPalette.COLORS["RESET"]

    def color_output(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result is not None:
                print(f"{self.color}[{func.__name__}] returned: {result}{self.reset}")
            return result
        return wrapper


# Примеры использования
red_decorator = ColorDecorator(color="RED")
green_decorator = ColorDecorator(color="GREEN")
blue_decorator = ColorDecorator(color="BLUE")

@red_decorator.color_output
def read_root():
    return {"Hello": "World"}

@green_decorator.color_output
def read_item(item_id: int, q: str):
    return {"item_id": item_id, "q": q}

@blue_decorator.color_output
def say_hello(user: str):
    return f"Hello, {user}!"


# Проверяем
read_root()            # Вывод красным
read_item(2, "item")    # Вывод зеленым
say_hello("boy")     # Вывод синим
