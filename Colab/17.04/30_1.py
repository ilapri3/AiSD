def decorator(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        
        with open("statistics.txt", "a") as file:
            file.write(f"Function '{func.__name__}' was called. Total calls: {wrapper.count}\n")
        
        print(f"Function '{func.__name__}' was called. Total calls: {wrapper.count}")
        
        return result
    
    wrapper.count = 0
    return wrapper

@decorator
def example():
    print('Пример функции. Проверка работы')
    
for _ in range(3):
    example()
