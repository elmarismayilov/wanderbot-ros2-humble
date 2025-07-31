import rclpy
from rclpy.node import Node
from rclpy.duration import Duration

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import math

class WanderNode(Node):

    def __init__(self):
        super().__init__('wander')
        self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.scan_sub = self.create_subscription(LaserScan, 'scan', self.scan_callback, 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.driving_forward = True
        self.g_range_ahead = float('inf')
        self.state_change_time = self.get_clock().now() + Duration(seconds=5)

    def timer_callback(self):
        if self.driving_forward:
            if self.g_range_ahead < 0.3 or self.get_clock().now() > self.state_change_time:  
                self.driving_forward = False
                self.state_change_time = self.get_clock().now() + Duration(seconds=3)
        else:
            if self.get_clock().now() > self.state_change_time:
                self.driving_forward = True
                self.state_change_time = self.get_clock().now() + Duration(seconds=5)

        twist = Twist()
        if self.driving_forward:
            twist.linear.x = 0.275
        else:
            twist.angular.z = 0.6
        
        self.cmd_vel_pub.publish(twist)

    def scan_callback(self, msg):
        center = len(msg.ranges) // 2
        window = 20

        window_ranges = msg.ranges[center - window // 2 : center + window // 2 + 1]
        valid_ranges = [r for r in window_ranges if r > 0.0 and r < float('inf') and not math.isnan(r)]

        if valid_ranges:
            self.g_range_ahead = sum(valid_ranges) / len(valid_ranges)
        else:
            self.g_range_ahead = float('inf')

def main(args=None):
    rclpy.init(args=args)
    node = WanderNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()