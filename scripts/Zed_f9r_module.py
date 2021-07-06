#!/usr/bin/env python
import rospy
from picontroller.msg import Location
from picontroller.msg import Imu
import serial
from ublox_gps import UbloxGps

port = serial.Serial('/dev/serial0', baudrate=38400, timeout=1)
gps = UbloxGps(port)
message_rate = 1 # In Hz

def start():
    imu_pub = rospy.Publisher('imu_data', Imu, queue_size=10)
    loc_pub = rospy.Publisher('loc_data', Location, queue_size=10)
    rospy.init_node('Zed_f9r_module', anonymous=True)
    rate = rospy.Rate(message_rate)
    rospy.loginfo("Zed_f94_module node started!")
    while not rospy.is_shutdown():
        veh = gps.veh_attitude()
        geo = gps.geo_coords()
        gps_time = gps.date_time()

        imu_msg = Imu()
        imu_msg.time = gps_time.iTOW # Internet time of the week
        imu_msg.roll = veh.roll
        imu_msg.pitch = veh.pitch
        imu_msg.heading = veh.heading
        imu_msg.rollAcc = veh.accRoll
        imu_msg.pitchAcc = veh.accPitch
        imu_msg.headingAcc = veh.accHeading
        imu_pub.publish(imu_msg)

        loc_msg = Location()
        loc_msg.time = gps_time.iTOW # Internet time of the week
        loc_msg.longitude = geo.lon
        loc_msg.latitude = geo.lat
        loc_msg.altitude = geo.altitude
        loc_pub.publish(loc_msg)

        rate.sleep()


if __name__ == "__main__":
    try:
        start()
    except rospy.ROSInterruptException:
        pass