def make_grid(width, height):
    return {(row,col): ' '
            for row in range(height)
            for col in range(width)}

grid = make_grid(2,2)
print grid