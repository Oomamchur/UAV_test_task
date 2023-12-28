## **Drone ALT_HOLD Manual Control**

This Python script is designed to command a drone using the DroneKit library with manual control in the ALT_HOLD mode. The script performs the following tasks:

## Connection Setup:
The script takes a connection target string as an optional command-line argument. If not specified, it starts a Software-in-the-Loop (SITL) simulation.
It connects to the vehicle using the specified connection string or the one generated for SITL.

1. Takeoff and Altitude Control:

 - The arm_and_takeoff function performs basic pre-arm checks, arms the motors, and takes off.
 - During the ascent, it adjusts the throttle channels based on the current altitude to achieve a smooth climb.

2. Distance and Bearing Calculations:

 - The script includes functions to calculate the distance between two global locations and the bearing from one location to another.

3. Manual Control in ALT_HOLD Mode:

 - The way_to_point function commands the drone to move towards a specified destination (wpl) in the ALT_HOLD mode.
 - It adjusts throttle channels based on the distance to the destination, providing manual control.
 - Yaw control is handled separately to ensure the drone faces the correct direction.
 - 
4. Yaw Control:

5. The condition_yaw function adjusts the yaw to a specified angle, ensuring the correct orientation of the drone.

6.  Main Mission:

 - The main part of the script waits until the vehicle is in ALT_HOLD mode, arms, takes off to an altitude of 100 meters, and then navigates to a predefined destination (point_B).
 - Yaw is adjusted to face the destination, and manual control is used to guide the drone to the destination.
 - After reaching the destination, the drone's yaw is adjusted, and the script prints a mission completion message.

## **USAGE**

1. Install requirements  
```terminal
    pip install -r requirements.txt
```
2. Start SITL (Software-in-the-Loop) Simulation
In the first terminal, start the SITL simulation with the specified home location:
```terminal
    dronekit-sitl copter-3.3 --home=50.450739,30.461242,0,180
```
3. Start MAVProxy
In the second terminal, start MAVProxy with the specified configuration:
```terminal
    mavproxy.py --master tcp:127.0.0.1:5760 --out udp:127.0.0.1:14551 --out udp:127.0.0.1:14550 --out udp:10.55.222.120:14550
```
4. Mission planer already installed
5. Open Mission Planner
Ensure that Mission Planner is installed and connected to port 14551.
6. Run the Drone Flight Script
In the third terminal, run the drone_flight.py script with the specified connection string:
```terminal
    python drone_flight.py --connect udp:127.0.0.1:14551
```
Video: https://www.loom.com/share/d83187dc6ca74230919a755c15ce6dd7?sid=98f133f7-7b8b-44f3-b885-b3e2c76ec5b7