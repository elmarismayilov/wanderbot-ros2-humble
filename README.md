ROS2 Wander Bot (TurtleBot3, Gazebo)

This project is a ROS2 port of the wander bot example from the book Programming Robots with ROS by Quigley, Gerkey, and Smart.

The robot was simulated in Gazebo using TurtleBot3, and follows basic reactive behavior based on bump or laser scan feedback. It doesn’t fully avoid obstacles but replicates the behavior described in the book.

What I Learned

Porting a ROS1 project to ROS2
Writing reactive behavior using publishers, subscribers, and TF2
Launching a robot in Gazebo
Understanding the ROS2 node lifecycle and simulation setup
Run Instructions

Launch a Gazebo simulation with a robot that publishes /scan and subscribes to /cmd_vel (e.g., TurtleBot3).
Build the ROS2 package.
Run the wander node separately in another terminal.
Make sure ros2_control, TF2, and your simulation environment are properly configured.
