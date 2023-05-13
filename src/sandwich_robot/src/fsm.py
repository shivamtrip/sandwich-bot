#!/usr/bin/env python

from enum import Enum
import rospy
import manipulation

class States(Enum):
    IDLE = 0
    FORWARD_MODE = 1
    RESET_MODE = 2


class SandwichFSM:

    def _init_(self):
        rospy.init_node('sandwich_fsm', anonymous = True)

        self.state = States.IDLE
        self.number_of_objects = 3


    def main(self):

        while not rospy.is_shutdown():

            if self.state == States.IDLE:
                print("Sandwich Robot initializing..")
                self.state = States.FORWARD_MODE

            elif self.state == States.FORWARD_MODE:

                manipulation.forward_mode(self.number_of_objects)
                self.state = States.RESET_MODE

            elif self.state == States.RESET_MODE:
                manipulation.reset_mode(self.number_of_objects)

                self.state = States.IDLE


if __name__ == "__main__":

    fsm = SandwichFSM()

    fsm.main()






