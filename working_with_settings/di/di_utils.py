def singleton(func):
    instance = None

    def wrapper(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = func(*args, **kwargs)
        return instance

    return wrapper
