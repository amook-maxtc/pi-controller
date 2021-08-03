# pi-controller

## Dependencies 

1) [livox_ros_driver](https://github.com/Livox-SDK/livox_ros_driver)

note: The livox_ros_driver and picontroller should be placed inside the same catkin workspace

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

To configure the ZED-F9R, use the software [u-center](https://learn.sparkfun.com/tutorials/getting-started-with-u-center-for-u-blox).

Here is what I changed inside the configuration:
1) MSG (Messages) Everything turned off for all ports except the following:
  - NAV-ATT on for UART1
  - NAV-PVT on for UART1
  - NMEA GxRMC on for USB, with 10 in the text box (Will divide the 10hz down to 1 hz needed for time sync)
2) PRT (Ports) Protocol out for USB set to only NMEA
3) RATE (Rates) Measurement Period set to 100ms


### Initalization

To initalize the IMU, you **must** drive it around.
Here are the steps,
1) Secure pi/imu combo to vehicle such that x-axis on the ZED-F9R points forward
2) Park in open for 5 or so minutes
3) Drive around, making sure to take several turns and reach minimum 20mph

To check the status of the initalization, using u-center, navigate inside the messages window to UBX->ESF (External Sensor Fusion)->STATUS and double click on the tab to ensure it updates every second. If it is not updating, the seconds counter will accumulate in the upper right-hand corner

### Implementation

To actually read the data from the ZED-F9R, the sparkfun library is used. The code that broadcasts the data is [here](https://github.com/amook-maxtc/pi-controller/blob/main/scripts/Zed_f9r_module.py). A custom ROS message is constructed for the IMU data and GPS data. They are then written to binary files.

## Livox MD-40 Lidar

This project uses the [MD-40](https://www.livoxtech.com/mid-40-and-mid-100)
Here are some important links used during development:
1) [livox_ros_driver](https://github.com/Livox-SDK/livox_ros_driver)
2) [livox high precision mapping](https://github.com/Livox-SDK/livox_high_precision_mapping/)
3) [livox SDK](https://github.com/Livox-SDK/Livox-SDK)
4) [laspy](https://laspy.readthedocs.io/en/latest/index.html)

### Configuration

Inside the livox_ros_driver workspace, enter the lidar's Serial Number into the [config file](https://github.com/Livox-SDK/livox_ros_driver/blob/master/livox_ros_driver/config/livox_lidar_config.json). 

### Lidar Logger

the file [lidar_logger.py](https://github.com/amook-maxtc/pi-controller/blob/main/scripts/lidar_logger.py) listens to the lidar messages that the lidar_ros_driver broadcasts. It then appends the messages into a LAS file using [point format 1](https://laspy.readthedocs.io/en/latest/intro.html). With the default configuration, the lidar publishes packs of 10,000 points at a rate of 2.5hz. So, each packet of 10,000 points is converted into a `PackedPointRecord` by first creating a numpy array. 


## Raspberry Pi 4

There are some important distinctions when using the Raspberry Pi with Raspbian. 

Ros Melodic was installed using this [tutorial](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Melodic%20on%20the%20Raspberry%20Pi)
- In section 4.2, these additional modules were needed: `ros_comm`, `tfs_sensor_msgs`, `pcl_ros`, `roslint`, `nav_msgs`
