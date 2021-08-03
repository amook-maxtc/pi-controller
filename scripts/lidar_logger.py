#!/usr/bin/env python3

import rospy
import numpy as np
from livox_ros_driver.msg import CustomMsg
from livox_ros_driver.msg import CustomPoint
import laspy
from laspy import PointFormat
import datetime


time = datetime.datetime.now()
filename = "/home/pi/sensor_data/lidar_out_{0}_{1}_{2}_{3}_{4}.las".format(time.year, time.month, time.day, time.hour, time.minute)
las_loc = laspy.lib.create_las(point_format=PointFormat(1)) #Create Las File
las_loc.write(filename)
las = laspy.open(filename,"a") #Create LasAppender object to write points to

def processLidarData(data):
    base_time = data.timebase
    pointcld = np.zeros(data.point_num,PointFormat(1).dtype()) #Empty point object
    for i in range(0,data.point_num):
        pointcld[i]["X"] = int(data.points[i].x * 1_000_000) #Livox units are meters, but LAS requires integers. So, the accuracy is 1um
        pointcld[i]["Y"] = int(data.points[i].y * 1_000_000)
        pointcld[i]["Z"] = int(data.points[i].z * 1_000_000)
        pointcld[i]["intensity"] = data.points[i].reflectivity
        pointcld[i]["gps_time"] = (base_time + data.points[i].offset_time) / 1000000 #Time is in units of nano seconds, convert to milli seconds
    las.append_points(laspy.PackedPointRecord(pointcld,PointFormat(1)))

def shutdown():
    print("lidar_logger shutting down.")
    las.close()


def listener():
    rospy.on_shutdown(shutdown)

    rospy.loginfo("Lidar logger opened")
    rospy.init_node("lidar_logger", anonymous=True)
    rospy.Subscriber('livox/lidar', CustomMsg, processLidarData)
    rospy.spin()


if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass