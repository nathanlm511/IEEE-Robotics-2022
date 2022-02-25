'''
This is skeleton code for the main FSM of the robot.



Rough quick reference for competition board
1,3,5,6,7,910 = Net/Cup
4 = Turn
P = powerline pole
2T,8T = Trees
"""""""""""""""""""""""""""""""""""""""""""""""""""""""
|                                    |          |     |
|    10                 P    7       |          |1    |
|""""""""""""         """"""""""""""""          |     |
|                                               |2T   |
|                                               |3    |
|                                               |     |
|""""""""""""         """""""""""""""""""""""""""     |
|    9   8T             P     6              5  4     |
|                                                     |
"""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''


import camera
import navigation
import arm

# variables to be used for readability when changing states
start_up = 0
grab_beads = 1
put_beads_in_catapult = 2
fire_catapult = 3
center_robot = 4
nav = 5
align_with_tree = 6
look_at_right_side = 7
detect_net = 8
return_to_start = 9

#this is a test comment


# arbitrary class currently being used for readability, it may be
# decided later on to put something here
class Startup():
    def __init__(self):
        pass

    def execute(self, robot):
        print("Start")
        robot.state = nav


# arm
class GrabBeads():
    def __init__(self):
        pass

    def execute(self, robot):
        # move arm to grab beads
        arm.retrieveBracelets()
        print("Grab Beads")
        robot.state = navigation


# arm
class PutBeadsInCatapult():
    def __init__(self):
        pass

    def execute(self, robot):
        # move arm over and place beads in catapult
        arm.beadsToCatapult()
        print("Place beads in catapult")
        robot.catapult_loaded = True
        robot.state = center_robot
        pass

# arm
class FireCatapult():
    def __init__(self):
        pass

    def execute(self, robot):
        if robot.net_on_right:
            # rotate catapult to right side
            pass
        arm.launchBracelets()
        print("Fire catapult")

        robot.catapult_loaded = False
        robot.state = center_robot

# camera/arm
class LookAtRightSide():
    def __init__(self):
        pass

    def execute(self, robot):
        # aim arm at right side of robot for camera to detect net
        arm.lookRight()
        robot.arm_on_right = True
        
        robot.state = detect_net

# camera
class DetectNet():
    def __init__(self):
        self.net = True # place holder for logic in execute

    def execute(self, robot):
        # idealy, the below if statement will be replaced with a helper function used
        #  by the camera to tell if there is a net in the current position
        camera.detectNet()
        print("Detecting net...")
        if self.net:
            print("Net detected")
            robot.state = fire_catapult
        else:
            print("No net detected")
            # move to next cup/net location?
            robot.state = nav


# camera/navigation
class AlignWithTree():
    def __init__(self):
        pass

    def execute(self, robot):
        # using camera, more precisely line up robot with first tree and move robot as close as possible
        camera.treeAlign()
        print("Align with tree")
        robot.state = grab_beads

# navigation
class CenterRobot():
    def __init__(self):
        pass

    def execute(self, robot):
        navigation.centreOnTrack()
        print("Center robot on track")
        robot.state = nav

# navigation
class Navigation():
    def __init__(self):
        pass

    def execute(self, robot):
        if robot.next_location == 1:
            print("Reverse to position 1")
            navigation.reverseTo1()
        elif robot.next_location == 2:
            if robot.forward:
                print("Forward to tree 1")
                navigation.forwardTree1()
            else:
                navigation.reverseTree1()
            if robot.next_tree < 3:
                robot.state = align_with_tree
                robot.next_tree += 1
        elif robot.next_location == 3:
            if robot.forward:
                print("Forward to location 3")
                navigation.forwardTo3()
            else:
                print("Reverse to location 3")
                navigation.reverseTo3()
            if robot.catapult_loaded:
                robot.state = detect_net
        elif robot.next_location == 4:
            if robot.forward:
                print("Turn1")
                navigation.turn1()
            else:
                print("Turn2 (Turn1 in reverse)")
                navigation.turn2()
        elif robot.next_location == 5:
            if robot.forward:
                print("Forward to location 5")
                navigation.forwardTo5()
            else:
                print("Reverse to location 5")
                navigation.reverseTo5()
            if robot.catapult_loaded:
                robot.state = detect_net
        elif robot.next_location == 6:
            if robot.forward:
                print("Forward to location 6")
                navigation.forwardTo6()
            else:
                print("Robot is going backwards and is already at position 6")
            if robot.catapult_loaded:
                robot.state = detect_net
        elif robot.next_location == 7:
            if robot.forward:
                print("Robot is already at position 6, so if\n\tcatapult is loaded, check for net at location 7")
            else:
                print("Reverse to location 7")
                navigation.reverseTo7()
            if robot.catapult_loaded:
                robot.state = look_at_right_side
        elif robot.next_location == 8:
            if robot.forward:
                print("Forward to tree 1")
                navigation.forwardTree2()
            else:
                navigation.reverseTree2()
            if robot.next_tree < 3:
                robot.state = align_with_tree
                robot.next_tree += 1
        elif robot.next_location == 9:
            if robot.forward:
                print("Forward to location 9")
                navigation.forwardTo9()
            else:
                print("Robot already at location 9, do nothing")
            if robot.catapult_loaded:
                robot.state = detect_net
        elif robot.next_location == 10:
            print("If catapult is loaded, check for net at location 10")
            if robot.catapult_loaded:
                robot.state = look_at_right_side
            
        if robot.next_location == 10:
            robot.forward = not robot.forward
        
        if robot.next_location == 1:
            robot.state = return_to_start
        
        if robot.forward:
            robot.next_location += 1
        else:
            robot.next_location -= 1
        
        
# navigation
class ReturnToStart():
    def __init__(self):
        pass

    def execute(self, robot):
        pass

class RobotFSM():
    def __init__(self):
        self.states =  [Startup(),
                        GrabBeads(),
                        PutBeadsInCatapult(),
                        FireCatapult(),
                        CenterRobot(),
                        Navigation(),
                        AlignWithTree(),
                        LookAtRightSide(),
                        DetectNet(),
                        # MoveTree1(),
                        # MoveTree2(),
                        # Turn1(),
                        # Turn2(),
                        ReturnToStart()]
        self.catapult_loaded = False
        self.next_location = 2
        self.arm_on_right = False
        self.net_on_right = False
        self.next_tree = 1
        self.forward = True
        self.state = 0

def main():
    robot = RobotFSM()

    while True:
        robot.states[robot.state].execute(robot)
        if robot.state == return_to_start:
            print("Success!")
            break
