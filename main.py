import logging

def calculator_decorator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except Exception as e:
            logging.error(f"Error evaluating expression: {expression}. Error message: {e}")
            return None

    return wrapper

@calculator_decorator
def calculate(expression):
    return eval(expression)



result = calculate("7 + 8")
print(result)

result = calculate("10 / 0")
print(result)