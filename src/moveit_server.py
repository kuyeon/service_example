#!/usr/bin/env python3
from service_example.srv import *
import rospy
import time


class MoveItServer:
    def __init__(self):
        pass


    def show_in_terminal(self, dist, vel):
        for i in range(0, dist+1):
            process = i*'-' + '■' + (dist-i)*'-'
            print('0m ' + process + ' ' + str(dist)+'m ' + "[%d%%]\r" % (i/dist*100), end="")
            time.sleep(1/vel)


    def move_it_railrobot(self, cmd_type, distance, velocity):
        if cmd_type == 'move':
            d = int(distance[:-1])
            v = int(velocity[:-3])
            self.show_in_terminal(d, v)


    def handle_move_it(self, req):
        print("\nThe railrobot is moving %s at a speed of %s" % (req.distance, req.velocity))
        self.move_it_railrobot(req.command_type, req.distance ,req.velocity)
        return MoveItResponse('Mission Complete!!')


    def move_it_server(self):
        rospy.init_node("move_it_server")
        rospy.Service('move_it', MoveIt, self.handle_move_it)
        print("ready")
        rospy.spin()


if __name__ == "__main__":
    s1 = MoveItServer()
    s1.move_it_server()


