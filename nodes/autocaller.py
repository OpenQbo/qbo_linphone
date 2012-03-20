#!/usr/bin/env python

import roslib; roslib.load_manifest('qbo_linphone')
import rospy

from qbo_linphone.srv import CallMe
from linphone.linphone import Linphone

class Autocaller:
    def __init__(self):
        rospy.init_node('autocaller')
        audio_device_id = rospy.get_param('audio_device', 'ALSA: default device')
        self.phone = Linphone( audio_dev_id = audio_device_id,
                               termination_condition = rospy.is_shutdown )
        call_service = rospy.Service('autocaller', CallMe, self.handle_call_me)
        print "Ready to call."

    def handle_call_me(self, call_request):
        return self.phone.call(call_request.address)

if __name__ == '__main__':
    try:
        caller = Autocaller()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

