#!/usr/bin/env python

import roslib; roslib.load_manifest('linphone')
import rospy

if __name__ == '__main__':
    rospy.init_node('sound_play')
