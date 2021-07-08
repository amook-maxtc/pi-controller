#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from picontroller.msg import Location
from picontroller.msg import Imu

imuLog = open("/home/pi/sensor_data/imu_data.txt",'w')
locLog = open("/home/pi/sensor_data/loc_data.txt",'w')

def processImuData(data): #Initially just log data using ascii, eventually need to make own file format
    rospy.loginfo("Logging IMU data")
    imuLog.write("{0},{1},{2},{3},{4},{5},{6}\n".format(data.time, data.roll, data.pitch,data.heading,data.rollAcc,data.pitchAcc,data.headingAcc))

def processLocData(data):
    rospy.loginfo("Logging location data")
    locLog.write("{0},{1},{2},{3}\n".format(data.time,data.longitude,data.latitude,data.altitude))

def listener():
    rospy.loginfo("Data logger opened")
    rospy.init_node("logger_node",anonymous=True)
    rospy.Subscriber('imu_data', Imu, processImuData)
    rospy.Subscriber('loc_data', Location, processLocData)
    rospy.spin()

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        imuLog.close()
        locLog.close()