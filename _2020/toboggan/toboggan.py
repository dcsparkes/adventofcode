def traverse(fileName, steepness=(1, 3), start=0):
    """Count collisions of a traversal of a slope.
    Parameters:
        fileName: of tree-map
        start: index of start position
        steepness: tuple of horizontal speed (veer) and vertical speed (plummet)."""

    width = 0
    collisions = 0
    position = start
    progress = 0

    plummet, veer = steepness

    with open(fileName) as inFile:
        for line in inFile:
            if width == 0: #firstLine
                width = len(line) - 1 # don't count newline

            progress %= plummet

            if progress == 0:
                if(line[position] == '#'):
                    collisions += 1

                position += veer
                position %= width

            progress += 1

    return collisions

