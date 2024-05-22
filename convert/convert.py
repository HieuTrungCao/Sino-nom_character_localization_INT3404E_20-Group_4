def convert(x1, y1, x2, y2, size_x, size_y):
    x1 /= size_x
    x2 /= size_x
    y1 /= size_y
    y2 /= size_y
    return (x1 + x2) / 2, (y1 + y2) / 2, x2 - x1, y2 - y1




