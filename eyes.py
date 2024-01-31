def draw_eye(matrix, x, y):
    eye_data = [0x0C00, 0x1F00, 0x1F80, 0x1000, 0x1FE0, 0x3FE0, 0x3FF0, 0x3FF0, 0x3FF0, 0x3FF0, 0x3FF0, 0x1FE0, 0x1FE0, 0x1FC0, 0x1F80, 0x0F00]

    for ex in range(0,16):
        column = eye_data[ex]
        for ey in range(0,16):
            g = 255 if column & 0x1 else 0
            matrix.SetPixel(x + ex, y + ey, 0, 0, g)
            column = column >> 1
    
def draw(matrix):
    draw_eye(matrix, 8, 8)
    draw_eye(matrix, 40, 8)