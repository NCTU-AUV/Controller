#!/usr/bin/env python
import AUV_physics
import numpy as np
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray 
from std_msgs.msg import Int32
from std_msgs.msg import Int32MultiArray
from rospy.numpy_msg import numpy_msg
import time
import traceback
import rosparam
import math


class Main():
	def __init__(self):
		rospy.init_node('forward_PID', anonymous=True)
		self.state = 0 
		self.Po = AUV_physics.AUV()
		self.yaw_error = 0
		self.forward_pub = rospy.Publisher('/force/forward',Float32MultiArray,queue_size=1)
		self.vel = 0.1
		rospy.Subscriber('/error/yaw', Float32, self.yaw)
		rospy.Subscriber('/AUVmanage/state',Int32,self.state_change)
		tStart = time.time()
		while not rospy.is_shutdown():
			if time.time() - tStart >0.5:
				try:
					self.tune_yaw = rosparam.get_param('/tune/yaw')
					tStart = time.time()
				except Exception as e:
					exstr = traceback.format_exc()
					print(exstr)

	def yaw(self,data):
		yaw_error = data.data
		if self.state == 1:
			drag_force = self.Po.drag_effect(np.array([self.vel,0,0,0,0,0]))
			forward_force = drag_force + np.array([0,0,0,0,0,yaw_error])
			#print forward_force
			forward_force = np.dot(self.Po.Trust_inv,forward_force)
			print(forward_force)
			force_data = Float32MultiArray(data = forward_force)
			self.forward_pub.publish(force_data)
		elif self.state ==0:
			self.forward_pub.publish(Float32MultiArray(data = [0,0,0,0,0,0]))
	def state_change(self,data):
		self.state = data.data
if __name__ == "__main__":
	try:
		Main()
	except Exception as e:
		exstr = traceback.format_exc()
		print(exstr)