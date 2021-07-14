#!/usr/bin/env python3

import rospy
import numpy as np
from livox_ros_driver.msg import CustomMsg
from livox_ros_driver.msg import CustomPoint
import laspy

las = laspy.open("/home/pi/sensor_data/lidar_out.las","a")
def processLidarData(data):
    base_time = data.timebase
    pointcld = np.zeros(data.point_num,PointFormat(1).dtype())
    for i in range(0,data.point_num):
        pointcld[i]["X"] = int(data.points[i].x * 1_000_000) #Livox units are meters, but LAS requires integers. So, the accuracy is 1um
        pointcld[i]["Y"] = int(data.points[i].y * 1_000_000)
        pointcld[i]["Z"] = int(data.points[i].z * 1_000_000)
        pointcld[i]["intensity"] = data.points[i].reflectivity
        pointcld[i]["gps_time"] = base_time + data.points[i].offset_time
    las.append_points(laspy.PackedPointRecord(pointcld,PointFormat(1)))

def shutdown():
    print("lidar_logger shutting down.")
    las.close()


def listener():
    las_loc = laspy.lib.create_las(point_format=PointFormat(1))
    rospy.on_shutdown(shutdown)
    las_loc.write("/home/pi/sensor_data/lidar_out.las")
    rospy.loginfo("Lidar logger opened")
    rospy.init_node("lidar_logger", anonymous=True)
    rospy.Subscriber('livox/lidar', CustomMsg, processLidarData)
    rospy.spin()


if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass