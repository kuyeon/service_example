#!/usr/bin/env python3
import sys
import rospy
from service_example.srv import *


class MoveItClient:
    def __init__(self):
        pass


    def move_it_client(self, cmd_type, dist, vel):
        rospy.wait_for_service("move_it")
        try:
            move_it = rospy.ServiceProxy("move_it", MoveIt)
            resp1 = move_it(cmd_type, dist, vel)
            return resp1.response_message
        except rospy.ServiceException as e:
            print("Serive call failed: %s" % e)


if __name__ == "__main__":
    c1 = MoveItClient()


    if len(sys.argv) == 4:
        c = sys.argv[1]
        d = sys.argv[2]
        v = sys.argv[3]
    else:
        sys.exit()


    print("\nRequesting the railrobot to %s %s at a speed of %s\n" % (c, d, v))
    print("Moving...\n")
    print(c1.move_it_client(c, d, v))
