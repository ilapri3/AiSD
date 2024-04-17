def custom_decorator(arg1, arg2, arg3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Аргументы декоратора: {arg1}, {arg2}, {arg3}")
            print("Переданные аргументы в функцию:")
            print(f"Позиционные: {args}")
            print(f"Именованные: {kwargs}")
            
            return func(*args, custom_arg1=arg1, custom_arg2=arg2, custom_arg3=arg3, **kwargs)
        
        return wrapper
    return decorator

@custom_decorator("Значение1", "Значение2", "Значение3")
def example_function(*args, **kwargs):
    print("Выполняется функция")
    
example_function(56, 4, 32, 35, a="Value1", b="Value2", c="Value3")
