import asyncio
from enum import Enum, unique
from typing import Callable
import random


@unique
class Statuses(Enum):
    PENDING = "PENDING"
    DONE = "DONE"
    ERROR = "ERROR"


def error_callback(err: str, state: Statuses):
    # Можно залогировать, отправить в базу данных и так далее
    print(f'Выполнено с ошибкой: {err}, статус: {state.value}')


def result_callback(res: str, state: Statuses):
    # Можно залогировать, отправить в базу данных и так далее
    print(f'Выполнено с успешно: {res}, статус: {state.value}')


async def task_coroutine(url: str):
    # Имитация времени выполнения запроса
    delay: int = random.randint(1, 6)
    await asyncio.sleep(delay)

    # Имитация возникновения ошибки
    if delay == 2:
        raise Exception(f"{url}: Ресурс не отвечает на запросы")

    return f"{url} выполнен"


async def main(timeout: float, result_callback_: Callable[[str, Statuses], None] = None,
               errors_callback: Callable[[str, Statuses], None] = None):
    print('Запускаем выполнение задач')
    labels, tasks = zip(*[(f"url {i}", asyncio.create_task(task_coroutine(f"url {i}"))) for i in range(10)])
    done_tasks, pending_tasks = await asyncio.wait(tasks, timeout=timeout)
    if result_callback_:
        for task in done_tasks:
            if not task.exception():
                result_callback_(str(task.result()), Statuses.DONE)
    if errors_callback:
        for task in done_tasks:
            if task.exception():
                errors_callback(str(task.exception()), Statuses.ERROR)
        for task in pending_tasks:
            label = str(labels[tasks.index(task)])
            errors_callback(label, Statuses.PENDING)

if __name__ == "__main__":
    asyncio.run(main(5, result_callback, error_callback))
