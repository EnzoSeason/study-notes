from typing import Any

MAX_LEVEL = float("inf")


def recursion(level: int, params: Any) -> None:
    # 1. Terminator
    if level > MAX_LEVEL:
        return

    #  2. process data at the current level
    process(level, params)

    # 3. drill down
    recursion(level + 1, params)

    # 4. recover the state of the current level
    #  The action at the next level may influence the state of current level.
    recover_state(level, params)


def process(level: int, params: Any) -> None:
    pass


def recover_state(level: int, params: Any) -> None:
    pass