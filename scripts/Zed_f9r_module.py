#!/usr/bin/env python3
import rospy
from picontroller.msg import Location
from picontroller.msg import Imu
import serial
from ublox_gps import UbloxGps
from ublox_gps import core
from ublox_gps import sparkfun_predefines as sp


port = serial.Serial('/dev/serial0', baudrate=38400, timeout=1)
gps = UbloxGps(port)
message_rate = 1 # In Hz
init_time = 0 # In milliseconds
init_defined = False

def start():
    global init_defined
    global init_time
    imu_pub = rospy.Publisher('imu_data', Imu, queue_size=10)
    loc_pub = rospy.Publisher('loc_data', Location, queue_size=10)
    rospy.init_node('Zed_f9r_module', anonymous=True)
    rate = rospy.Rate(message_rate)
    rospy.loginfo("Zed_f94_module node started!")
    while not rospy.is_shutdown():
        gps.send_message(sp.NAV_CLS, gps.nav_ms.get('ATT'))
        gps.send_message(sp.NAV_CLS, gps.nav_ms.get('PVT'))
        parse_tool = core.Parser([sp.NAV_CLS])
        cls_name, msg_name, payload = parse_tool.receive_from(gps.hard_port)
        if (msg_name == "ATT"):
            veh = gps.scale_NAV_ATT(payload)
            imu_msg = Imu()
            imu_msg.time = veh.iTOW # time of the week
            imu_msg.roll = float(veh.roll)
            imu_msg.pitch = float(veh.pitch)
            imu_msg.heading = float(veh.heading)
            imu_msg.rollAcc = float(veh.accRoll)
            imu_msg.pitchAcc = float(veh.accPitch)
            imu_msg.headingAcc = float(veh.accHeading)
            imu_pub.publish(imu_msg)
        elif (msg_name == "PVT"):
            geo = gps.scale_NAV_PVT(payload)
            loc_msg = Location()
            loc_msg.time = geo.iTOW # Internet time of the week
            loc_msg.longitude = float(geo.lon)
            loc_msg.latitude = float(geo.lat)
            loc_msg.altitude = float(geo.height)
            loc_pub.publish(loc_msg)

        #rate.sleep()


if __name__ == "__main__":
    try:
        start()
    except rospy.ROSInterruptException:
        pass