#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def driver():
    rospy.on_shutdown(shutdown)
    rospy.loginfo("led_driver node opened")
    rospy.init_node("led_driver", anonymous=True)
    rospy.Subscriber('/rosout_agg', String, parseError)
    rospy.spin()

def parseError(data):
    print("TESTING YO")
    print(data)

def shutdown():
    pass

if __name__ == "__main__":
    try:
        driver()
    except rospy.ROSInterruptException:
        pass