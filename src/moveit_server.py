#!/usr/bin/env python3
from service_example.srv import *
import rospy
import time


def show_in_terminal(dist, vel):
    for i in range(0, dist+1):
        process = i*'-' + '■' + (dist-i)*'-'
        print('0m', process, str(dist)+'m', "[%d%%]\r" % (i/dist*100), end="")
        time.sleep(1/vel)


def move_it_railrobot(cmd_type, distance, velocity):
    if cmd_type == 'move':
        d = int(distance[:-1])
        v = int(velocity[:-3])
        show_in_terminal(d, v)


def handle_move_it(req):
    print("\nThe railrobot is moving %s at a speed of %s" % (req.distance, req.velocity))
    move_it_railrobot(req.command_type, req.distance ,req.velocity)
    return MoveItResponse('Mission Complete!!')


def move_it_server():
    rospy.init_node("move_it_server")
    rospy.Service('move_it', MoveIt, handle_move_it)
    print("ready")
    rospy.spin()


if __name__ == "__main__":
    move_it_server()


