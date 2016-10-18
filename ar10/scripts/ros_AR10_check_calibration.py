#!/usr/bin/env python

from ros_ar10_class import ar10
import time

def check_calibration(hand, joint):
    n_points = 0

    sum_x  = 0.0
    sum_y  = 0.0
    sum_xy = 0.0
    sum_xx = 0.0

    if joint == 9:
        hand.move(8, 5500)

    print

    for target in range(4500, 8000, 500):
        hand.move(joint, target)
        hand.wait_for_hand()
        time.sleep(2.0)

        set_position = hand.get_set_position(joint)
        position     = hand.get_position(joint)
        error        = abs(set_position - position)

        print "joint = " + str(joint) + " set position = " + str(set_position) + " position = " + str(position) + " error = " + str(error)

    hand.move(joint, 7950)
    hand.wait_for_hand()

    if joint == 9:
        hand.move(8, 7950)
        hand.wait_for_hand()

    return

def main():
    # create hand object
    hand = ar10()

    hand.open_hand()

    hand.wait_for_hand()

    for joint in range(0, 10):
        check_calibration(hand, joint)

    # destroy hand object
    hand.close()

if __name__ == "__main__":
    main()


