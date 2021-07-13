import rospy

from livox_ros_driver.msg import CustomMsg
from livox_ros_driver.msg import CustomPoint

def processLidarData(data):
    print(data)

def listener():
    rospy.loginfo("Lidar logger opened")
    rospy.init_node("lidar_logger", anonymous=True)
    rospy.Subscriber('livox/lidar', CustomMsg, processLiarData)
    rospy.spin()

if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass