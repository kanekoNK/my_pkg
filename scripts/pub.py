#!/usr/bin/env python
#SPDX-License-Identifier: GPL-2.0
#
#Copyright (C) 2020 NaokiKaneko.  All rights reserved.
# 
import rospy
import random
from std_msgs.msg import Int32

rospy.init_node('pub')
pub = rospy.Publisher('byte', Int32 , queue_size=1)

rate = rospy.Rate(20)
while not rospy.is_shutdown():
    by = random.randint(0,5)
    pub.publish(by)
    rate.sleep()
