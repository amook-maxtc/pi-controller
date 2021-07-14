#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from picontroller.msg import Location
from picontroller.msg import Imu
import struct
import datetime

time = datetime.datetime.now()
imuLog = open("/home/pi/sensor_data/imu_data_{0}_{1}_{2}_{3}_{4}.imulog".format(time.year, time.month, time.day, time.hour, time.minute),'wb')
locLog = open("/home/pi/sensor_data/loc_data_{0}_{1}_{2}_{3}_{4}.gpslog".format(time.year, time.month, time.day, time.hour, time.minute),'wb')

def processImuData(data): #Initially just log data using ascii, eventually need to make own file format
    rospy.loginfo("Logging IMU data")
    #imuLog.write("{0},{1},{2},{3},{4},{5},{6}\n".format(data.time, data.roll, data.pitch,data.heading,data.rollAcc,data.pitchAcc,data.headingAcc))
    imuLog.write(struct.pack("Iffffff",data.time,data.roll,data.pitch,data.heading,data.rollAcc,data.pitchAcc,data.headingAcc))

def processLocData(data):
    rospy.loginfo("Logging location data")
    #locLog.write("{0},{1},{2},{3}\n".format(data.time,data.longitude,data.latitude,data.altitude))
    locLog.write(struct.pack("Ifff",data.time, data.longitude, data.latitude, data.altitude))

def shutdown():
    print("logger_node shutting down.")
    imuLog.close()
    locLog.close()


def listener():
    rospy.on_shutdown(shutdown)
    rospy.loginfo("Data logger opened")
    rospy.init_node("logger_node",anonymous=True)
    rospy.Subscriber('imu_data', Imu, processImuData)
    rospy.Subscriber('loc_data', Location, processLocData)
    rospy.spin()

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass