#!/usr/bin/env python
import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("keyboard_node", anonymous=True)
    rospy.loginfo("Started Publishing")

    pub = rospy.Publisher('/topic', String, queue_size=10)

    while not rospy.is_shutdown:
        print("Would you like to swtich on all peltiers? ")
        all = input("if yes press y, no press n: ")

        if all == 'y':
            pub.publish(all)

        else:

            pub.publish(all)
            
            print("Would you like to swtich on peltier1? ")
            p1 = input("if yes press y, no press n: ")

            if (p1 == 'y'):
                p1 = 'y1'
            
            else: 
                p1 = 'n1'

                pub.publish(p1)

                print("Would you like to swtich on peltier2? ")
                p2 = input("if yes press y, no press n: ")
                pub.publish(p2)

                if (p2 == 'y'):
                    p2 = 'y2'

                else: p2 = 'n2'
                
                pub.publish(p2)






