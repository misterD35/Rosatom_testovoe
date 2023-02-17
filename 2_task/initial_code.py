def create_handlers(callback):
    handlers = []
    for step in range(5):
        handlers.append(lambda: callback(step))
    return handlers


def execute_handlers(handlers):
    for handler in handlers:
        handler()
