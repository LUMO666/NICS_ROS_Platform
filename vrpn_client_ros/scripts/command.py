#!/usr/bin/env python

import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy
from vrpn_client_ros.msg import human_cmd
import sys, select, termios, tty

msg = """
Activate Human Command Line
"""

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)

    pub = rospy.Publisher('human_cmd', human_cmd, queue_size = 1)
    rospy.init_node('human_cmdline')

    try:
        print(msg)
        while(1):
            key = getKey()
                pub.publish(human_cmd(key))

    except Exception as e:
        print(e)

    finally:
        pass
