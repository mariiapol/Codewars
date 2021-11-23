def can_move(minimap, i, j, di, dj):
    #Check if can move in specified direction
    
    # minimap is always square
    n = len(minimap)

    # Move once
    i += di
    j += dj

    # Cannot move outside of minimap
    if i < 0 or i >= n or j < 0 or j >= n:
        return False

    # Cannot move if occupied
    if minimap[i][j] == 1:
        return False

    # Move second time
    i += di
    j += dj

    # Can move if second move falls outside
    if i < 0 or i >= n or j < 0 or j >= n:
        return True

    # Cannot move if second move is occupied
    if minimap[i][j] == 1:
        return False

    # Otherwise we can move
    return True


def spiralize(size):

    # Initial minimap
    spiral = [[0 for i in range(size)] for j in range(size)]

    # Start position
    i = j = 0

    # Direction vector
    di, dj = 0, 1

    # Make a snake, cannot rotate more than once each time
    rotated = 0
    while rotated < 2:
        spiral[i][j] = 1

        if can_move(spiral, i, j, di, dj):
            # Move
            i += di
            j += dj
            rotated = 0
        else:
            # Rotate direction clockwise
            di, dj = dj, -di
            rotated += 1

    # Last step might have made spiral curl on itself
    di, dj = -dj, di
    if spiral[i + di][j + dj] == 1:
        spiral[i][j] = 0

    return spiral
