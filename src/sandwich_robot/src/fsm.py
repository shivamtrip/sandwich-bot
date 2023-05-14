#!/usr/bin/env python

from enum import Enum
import rospy
import manipulation
import time

class States(Enum):
    IDLE = 0
    FORWARD_MODE = 1
    RESET_MODE = 2


class SandwichFSM:

    def __init__(self):

        self.state = States.IDLE
        self.number_of_objects = 3


    def main(self):

        while not rospy.is_shutdown():

            if self.state == States.IDLE:
                print("Sandwich Robot initializing..")
                
                sw = manipulation.SandwichMaker()           #instantiate sandwich maker class
                # sw.start_listener()
                time.sleep(1)
                self.state = States.FORWARD_MODE

            elif self.state == States.FORWARD_MODE:
                print("FORWARD MODE")
                sw.forward_mode(self.number_of_objects)
                self.state = States.RESET_MODE

            elif self.state == States.RESET_MODE:
                print("RESET MODE")
                sw.reset_mode(self.number_of_objects)

                self.state = States.IDLE


if __name__ == "__main__":

    fsm = SandwichFSM()

    fsm.main()






