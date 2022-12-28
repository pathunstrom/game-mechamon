import typing


class Rect(typing.Protocol):
    width: int | float
    height: int | float
    top: int | float
    bottom: int | float
    left: int | float
    right: int | float


def collision_rect_to_rect(first: Rect, second: Rect) -> bool:
    max_width = first.width + second.width
    max_height = first.height + second.height
    total_width = max(first.right, second.right) - min(first.left, second.left)
    total_height = max(first.top, second.top) - min(first.bottom, second.bottom)
    return total_width <= max_width and total_height <= max_height
