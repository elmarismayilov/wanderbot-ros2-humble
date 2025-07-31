# 🚀 ROS2 Wander Bot (TurtleBot3 + Gazebo)

This project is a **ROS2 port** of the *wander bot* example from the book  
**Programming Robots with ROS** by Quigley, Gerkey, and Smart.

The robot was simulated in **Gazebo** using **TurtleBot3**, and follows basic reactive behavior based on bump or laser scan feedback. It doesn’t fully avoid obstacles but replicates the behavior described in the book.

---

## 📘 What I Learned

- ✅ Porting a ROS1 project to ROS2  
- 🧠 Writing reactive behavior using **publishers**, **subscribers**, and **TF2**  
- 🛠️ Launching and simulating a robot in **Gazebo**  
- 🔄 Understanding the **ROS2 node lifecycle**  

---

## 🧪 How to Run

1. **Launch a Gazebo simulation** with a robot that:  
   - Publishes to `/scan` (e.g. LaserScan)
   - Subscribes to `/cmd_vel` (velocity command)

   Example: use **TurtleBot3 in Gazebo**

2. **Build the ROS2 package**:
   ```bash
   colcon build --packages-select your_package_name
   source install/setup.bash
3. **Run the wander node** (in a separate terminal after launching simulation):
   ```bash
   ros2 run your_package_name wander_node
