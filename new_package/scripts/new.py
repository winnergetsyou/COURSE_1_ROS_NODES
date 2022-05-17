#!/usr/bin/python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("%s",data.data)
    hello = String(data.data)
    obj = rospy.Publisher("topic_2",String, queue_size=10)
    obj.publish(hello)


def Subscriber():

    rospy.init_node('Subscribe',anonymous=True)
    rospy.Subscriber("topic_one",String,callback)
    rospy.spin()

if __name__=="__main__":
    Subscriber()


