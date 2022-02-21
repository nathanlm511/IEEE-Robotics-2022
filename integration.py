'''
This is skeleton code for the main FSM of the robot.



Rough quick reference for competition board
1,3,5,6,7,910 = Net/Cup
4 = Turn
P = powerline pole
2,8 = Trees
"""""""""""""""""""""""""""""""""""""""""""""""""""""""
|                                    |          |     |
|    10                 P    7       |          |1    |
|""""""""""""         """"""""""""""""          |     |
|                                               |2    |
|                                               |3    |
|                                               |     |
|""""""""""""         """""""""""""""""""""""""""     |
|    9   8             P     6              5  4      |
|                                                     |
"""""""""""""""""""""""""""""""""""""""""""""""""""""""
'''
import arm

# variables to be used for readability when changing states
import camera
import navigation

start_up = 0
grab_beads = 1
put_beads_in_catapult = 2
fire_catapult = 3
# move_tree_1 = 4
# move_tree_2 = 5
center_robot = 4
move_cup_net = 5
align_with_tree = 6
look_at_right_side = 7
detect_net = 8
# turn_1 = 11
# turn_2 = 12
return_to_start = 9

# arbitrary class currently being used for readability, it may be
# decided later on to put something here
class Startup():
    def __init__(self):
        pass

    def execute(self, robot):
        print("Start")
        robot.state = move_cup_net

# arm
class GrabBeads():
    def __init__(self):
        pass

    def execute(self, robot):
        # move arm to grab beads
        arm.Bead_Grabbing()
        print("Grab Beads")
        robot.state = put_beads_in_catapult

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
        arm.fireCatapult()
        print("Fire catapult")

        robot.catapult_loaded = False
        robot.state = center_robot

# camera/arm
class LookAtRightSide():
    def __init__(self):
        pass

    def execute(self, robot):
        # aim arm at right side of robot for camera to detect net
        robot.arm_on_right = True
        
        robot.state = detect_net

# camera
class DetectNet():
    def __init__(self):
        self.net = True # place holder for logic in execute

    def execute(self, robot):
        # idealy, the below if statement will be replaced with a helper function used
        #  by the camera to tell if there is a net in the current position
        camera.detectCam()
        print("Detecting net...")
        if self.net:
            print("Net detected")
            robot.state = fire_catapult
        else:
            print("No net detected")
            # move to next cup/net location?
            robot.state = move_cup_net

# camera/navigation
class AlignWithTree():
    def __init__(self):
        pass

    def execute(self, robot):
        # using camera, more precisely line up robot with first tree and move robot as close as possible
        camera.treeAlign()
        print("Align with tree")
        robot.state = grab_beads
'''
# navigation
class MoveTree1():
    def __init__(self):
        pass

    def execute(self, robot):
        print("Move to first tree")
        robot.state = align_with_tree
        pass

# navigation
class MoveTree2():
    def __init__(self):
        pass

    def execute(self, robot):
        # should be able to move to this location from net locations 2-4
        # by default, the robot moves to this state after net location 4
        print("Move to second tree")
        robot.state = 8
        pass
'''

# navigation
class CenterRobot():
    def __init__(self):
        pass

    def execute(self, robot):
        navigation.centreOnTrack()
        print("Center robot on track")
        robot.state = move_cup_net

        # if robot.catapult_loaded and robot.next_tree == 2:
        #     # if catapult is loaded, move to the next net location
        #     pass

'''
# navigation
class Turn1():
    def __init__(self):
        pass

    def execute(self, robot):
        # Turn1 should only ever be made after checking the first net location
        print("Make first turn")

# navigation
class Turn2():
    def __init__(self):
        pass

    def execute(self, robot):
        # turn2 should be able to be made from net locations 3-7
        pass
'''

# navigation
class MoveCupNet():
    def __init__(self):
        pass

    def execute(self, robot):
        if robot.next_net_location == 1:
            print("Move to net at location 1/Start position")
        if robot.next_net_location == 2:
            print("Move to tree 1")
            if robot.next_tree < 3:
                robot.state = align_with_tree
                robot.next_tree += 1
        elif robot.next_net_location == 3:
            print("Move to location 3")
            if robot.catapult_loaded:
                robot.state = detect_net
        elif robot.next_net_location == 4:
            if robot.forward:
                print("Turn1")
            else:
                print("Turn2 (Turn1 in reverse)")
        elif robot.next_net_location == 5:
            print("Move to location 5")
            if robot.catapult_loaded:
                robot.state = detect_net
        elif robot.next_net_location == 6:
            if robot.forward:
                print("Move to location 6")
            else:
                print("Robot is going backwards and is already at position 6")
            if robot.catapult_loaded:
                robot.state = detect_net
        elif robot.next_net_location == 7:
            if robot.forward:
                print("Robot is already at position 6, so if\n\tcatapult is loaded, check for net at location 7")
            else:
                print("Move to location 7")
            if robot.catapult_loaded:
                robot.state = look_at_right_side
        elif robot.next_net_location == 8:
            print("Move to tree 2")
            if robot.next_tree < 3:
                robot.state = align_with_tree
                robot.next_tree += 1
        elif robot.next_net_location == 9:
            if robot.forward:
                print("Move to location 9")
            else:
                print("Robot already at location 9")
            if robot.catapult_loaded:
                robot.state = detect_net
        elif robot.next_net_location == 10:
            print("If catapult is loaded, check for net at location 10")
            if robot.catapult_loaded:
                robot.state = look_at_right_side
            
        if robot.next_net_location == 10:
            robot.forward = not robot.forward
        
        if robot.next_net_location == 1:
            robot.state = return_to_start
        
        if robot.forward:
            robot.next_net_location += 1
        else:
            robot.next_net_location -= 1
        
        
# navigation
class ReturnToStart():
    def __init__(self):
        pass

    def execute(self, robot):
        # should be able to return to starting point from net locations 2-5
        pass

class RobotFSM():
    def __init__(self):
        self.states =  [Startup(),
                        GrabBeads(),
                        PutBeadsInCatapult(),
                        FireCatapult(),
                        # MoveTree1(),
                        # MoveTree2(),
                        CenterRobot(),
                        MoveCupNet(),
                        AlignWithTree(),
                        LookAtRightSide(),
                        DetectNet(),
                        # Turn1(),
                        # Turn2(),
                        ReturnToStart()]
        self.catapult_loaded = False
        self.next_net_location = 2
        self.arm_on_right = False
        self.net_on_right = False
        self.next_tree = 1
        self.forward = True
        self.state = 0


robot = RobotFSM()

while True:
    robot.states[robot.state].execute(robot)
    if robot.state == return_to_start:
        print("Success!")
        break
