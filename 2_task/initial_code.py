def create_handlers(callback):
    handlers = []
    for step in range(5):
        handlers.append(lambda: callback(step))

    def execute_handlers():
        for handler in handlers:
            handler()
    return execute_handlers
