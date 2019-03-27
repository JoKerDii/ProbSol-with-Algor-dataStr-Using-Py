"""The Tower of Hanoi puzzle was invented by the French mathematician Edouard Lucas in 1883. 
He was inspired by a legend that tells of a Hindu temple where the puzzle was presented to young priests.
At the beginning of time, the priests were given three poles and a stack of 64 gold disks,
each disk a little smaller than the one beneath it.
Their assignment was to transfer all 64 disks from one of the three poles to another, 
with two important constraints. They could only move one disk at a time, and they could never place a larger disk on top of a smaller one. """


def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        # move all but the bottom disk on the initial tower to an intermediate pole
        moveTower(height-1,fromPole,withPole,toPole)
        # moves the bottom disk to its final resting place.
        moveDisk(fromPole,toPole)
        # move the tower from the intermediate pole to the top of the largest disk      
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    """moving a disk from one pole to another. """

    print("moving disk from",fp,"to",tp)

# test
# moveTower(3,"A","B","C")