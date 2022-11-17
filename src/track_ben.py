#!/usr/bin/env python3

import rospy
import math
from include.geodesic import inverse
from sensor_msgs.msg import NavSatFix
import socket


nav_topic = '/ben/project11/nav/position'
base_lat = 43.07144719594087
base_lon = -70.7123558037089
rad  = 0
distance = 0
tup = (0,0)

def callback(data, pub):
    
    rospy.loginfo(data.latitude) 
    rospy.loginfo(data.longitude)
    tup = inverse(base_lat, base_lon, data.latitude, data.longitude)
    rad = tup[0]
    distance = tup[1]
    #pub.publish(math.degrees(rad))
    rospy.loginfo(math.degrees(rad))
   

def position_track():
    rospy.init_node('mwa')
    pub = rospy.Publisher(nav_topic + 'rotator_heading', NavSatFix, queue_size=1)
    rospy.Subscriber(nav_topic, NavSatFix, callback, callback_args=(pub))
    rospy.spin()

if __name__ == '__main__':
    position_track()
