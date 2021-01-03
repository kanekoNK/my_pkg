#!/usr/bin/env python 
#SPDX-License-Identifier: GPL-2.0
#
# Copyright (C) 2020 NaokiKaneko.  All rights reserved.
# 
import rospy
import csv
from std_msgs.msg import Int32	
import os
import time
if __name__ == "__main__":
    with open('log.csv') as f:
         reader = csv.reader(f,lineterminator='\n')
         l = [row for row in reader]
    rospy.init_node('Sub')
    N = 0
    Mnum = 500
    Num = 0
    bt = 0
    while Num <= Mnum:
        time.sleep(0.2)
        N = rospy.wait_for_message("byte", Int32)
        Num += N.data
        bt += 0.2
        os.system('clear')
        print('{0} {1}b/500b'.format(l[Num / 25],Num))
        print('            {0}%           {1}b/s'.format(Num / 5,round(Num / bt, 2)))        
	print('Download time remaining [{0}s]'.format(round((Mnum-Num)/round(Num / bt, 2)),2))

    os.system('clear')
    print('{0} 500b/500b'.format(l[Num / 25]))
    print('            {0}%           {1}b/s'.format(Num / 5,round(Num / bt, 2)))
    print("end of data reception")
        
