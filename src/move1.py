#!/usr/bin/env python
from getkey import getkey, keys
import rospy
import sys
from geometry_msgs.msg import Twist

def update(lx,ly,lz,ax,ay,az):
  

  twist = Twist()
  twist.linear.x = lx
  twist.linear.y = ly 
  twist.linear.z = lz 
  twist.angular.x = ax
  twist.angular.y = ay
  twist.angular.z = az
	
  pub.publish(twist)	


if __name__=="__main__":
    rospy.init_node('move_bot', anonymous=True)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
    try:
        rospy.loginfo('Reading from keyboard')
        rospy.loginfo('Press d-> RIGHT a->LEFT w->UP x->DOWN and to stop press s')
        rospy.loginfo('----------------------')
        while not rospy.is_shutdown():
        #k=raw_input('enter the key:')
            key = getkey()
            if key == 'd':
                update(0,0,0,0,0,10)
                rospy.loginfo('RIGHT')
  
            elif key == 'a':
                update(0,0,0,0,0,-10)
                rospy.loginfo('LEFT')

            elif key == 'w':
                update(10,0,0,0,0,0)
                rospy.loginfo('UP')

            elif key == 'x':
                update(-10,0,0,0,0,0)
                rospy.loginfo('DOWN')

            elif key=='s':
                update(0,0,0,0,0,0)
                rospy.loginfo('STOP')

            else:
                print("incorrect key")
                sys.exit(1)
    except rospy.ROSInterruptException:
        pass


