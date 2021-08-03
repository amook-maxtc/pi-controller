# pi-controller

## Dependencies 

1) [livox_ros_driver](https://github.com/Livox-SDK/livox_ros_driver)
Note: livox_ros_driver has its own dependencies, and ROS Melodic was used for this project.
2) [Rospy](http://wiki.ros.org/rospy)
Note: Make sure to get the python3 version of rospy.
```
sudo apt-get update
sudo apt-get install python3-rospy
```
3) [Qwiic_Ublox_Gps_Py](https://github.com/sparkfun/Qwiic_Ublox_Gps_Py/)
```
sudo pip install sparkfun-ublox-gps
```
4) [numpy](https://numpy.org/install/)
Note: Make sure to install python3 version

## Zed-F9R Sensor

This project uses the [SparkFun GPS-RTK Dead Reckoning pHAT for Raspberry Pi](https://www.sparkfun.com/products/16475)
Here are some important links used during development: 
1) [Hookup Guide](https://learn.sparkfun.com/tutorials/sparkfun-gps-rtk-dead-reckoning-zed-f9r-hookup-guide)
2) [U-blox Integration Manual](https://cdn.sparkfun.com/assets/learn_tutorials/1/1/7/2/ZED-F9R_Integrationmanual__UBX-20039643_.pdf)
3) [Python Code](https://qwiic-ublox-gps-py.readthedocs.io/en/latest/index.html)

### Configuration

### Initalization

### Implementation

## Livox MD-40 Lidar

This project uses the [MD-40](https://www.livoxtech.com/mid-40-and-mid-100)
Here are some important links used during development:
1) [livox_ros_driver](https://github.com/Livox-SDK/livox_ros_driver)
2) [livox high precision mapping](https://github.com/Livox-SDK/livox_high_precision_mapping/)
3) [livox SDK](https://github.com/Livox-SDK/Livox-SDK)

### Configuration
aaa

### Lidar Logger

## Raspberry Pi 4

There are some important distinctions when using the Raspberry Pi with Raspbian. 

Ros Melodic was installed using this [tutorial](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Melodic%20on%20the%20Raspberry%20Pi)
- In section 4.2, these additional modules were needed: `ros_comm`, `tfs_sensor_msgs`, `pcl_ros`, `roslint`, `nav_msgs`
