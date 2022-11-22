#!/usr/bin/env python3

import rospy
import math
from include.geodesic import inverse
from sensor_msgs.msg import NavSatFix
import socket
import time
import telnetlib


nav_topic = '/ben/project11/nav/position'
base_lat = 43.072047356563296
base_lon = -70.71152740402871
rad  = 0
distance = 0
tup = (0,0)
heading = 0

def callback(data, pub):
    
    global heading
    #rospy.loginfo(data.latitude) 
    #rospy.loginfo(data.longitude)
    tup = inverse(base_lon, base_lat, data.longitude, data.latitude)
    rad = tup[0]
    distance = tup[1]
    seconds = rospy.get_time()
    heading = math.degrees((rad))
    
  
   

def position_track():
    
    rospy.init_node('mwa')
    pub = rospy.Publisher(nav_topic + 'rotator_heading', NavSatFix, queue_size=1)
    sub = rospy.Subscriber(nav_topic, NavSatFix, callback, callback_args=(pub))
    
    HOST ="localhost"
    tn=telnetlib.Telnet()
    tn.open(HOST,"7373")
    last_heading = 0

    while not rospy.is_shutdown():
        print(heading)
        cur_heading = round(heading)
        if abs(cur_heading - last_heading) > 2:
            move = "M" + str(int(heading)) + "\n"
            tn.write(move.encode('UTF-8'))
            print("[COMMANDED]: " + move)
            last_heading = cur_heading

        rospy.sleep(5.0)

if __name__ == '__main__':
    position_track()
