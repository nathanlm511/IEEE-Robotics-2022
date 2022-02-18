'''
This is skeleton code for the main FSM of the robot.
'''
# arm
class GrabBeads():
    def __init__(self):
        pass

    def execute(self, robot):
        # move arm to grab beads
        print("Grab Beads")
        robot.state = 1

# arm
class PutBeadsInCup():
    def __init__(self):
        pass

    def execute(self, robot):
        # move arm over and place beads in catapult
        print("Place beads in catapult")
        robot.state = 2
        pass

# arm
class FireCatapult():
    def __init__(self):
        pass

    def execute(self, robot):
        print("Fire catapult")
        robot.state = 3
        pass

# camera/arm
class LookAtRightSide():
    def __init__(self):
        pass

    def execute(self, robot):
        pass

# camera
class DetectNet():
    def __init__(self):
        pass

    def execute(self, robot):
        pass

# camera/navigation
class AlignWithTree():
    def __init__(self):
        pass

    def execute(self, robot):
        pass

# navigation
class MoveTree1():
    def __init__(self):
        pass

    def execute(self, robot):
        pass

# navigation
class MoveTree2():
    def __init__(self):
        pass

    def execute(self, robot):
        pass

# navigation
class CenterRobot():
    def __init__(self):
        pass

    def execute(self, robot):
        pass

# navigation
class Turn1():
    def __init__(self):
        pass

    def execute(self, robot):
        pass

# navigation
class Turn2():
    def __init__(self):
        pass

    def execute(self, robot):
        pass

# navigation
class MoveCupNet1():
    def __init__(self):
        pass

    def execute(self, robot):
        pass

# navigation
class MoveCupNet2():
    def __init__(self):
        pass

    def execute(self, robot):
        pass

# navigation
class MoveCupNet3():
    def __init__(self):
        pass

    def execute(self, robot):
        pass

# navigation
class MoveCupNet4():
    def __init__(self):
        pass

    def execute(self, robot):
        pass

# navigation
class MoveCupNet5():
    def __init__(self):
        pass

    def execute(self, robot):
        pass

# navigation
class MoveCupNet6():
    def __init__(self):
        pass

    def execute(self, robot):
        pass

# navigation
class MoveCupNet7():
    def __init__(self):
        pass

    def execute(self, robot):
        pass

# navigation
class ReturnToStart():
    def __init__(self):
        pass

    def execute(self, robot):
        pass

# class ExampleState():
#     def __init__(self):
#         pass

#     def execute(self, robot):
#         # move arm to grab beads
#         print("Grab Beads")
#         robot.state = 1

class RobotFSM():
    def __init__(self):
        self.states = [GrabBeads(), PutBeadsInCup(), FireCatapult()]
        self.state = 0


robot = RobotFSM()

while True:
    robot.states[robot.state].execute(robot)
    if robot.state == 3:
        print("Success!")
        break
