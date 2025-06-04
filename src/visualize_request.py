#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Point
from uvatraj_msgs.srv import RequestTraj, RequestTrajResponse
from uvatraj_msgs.msg import ControlPoint

def handle_request_traj(req):
    rospy.loginfo("Received goal point: x=%.2f, y=%.2f, z=%.2f", req.goal.x, req.goal.y, req.goal.z)

    # Example: Create dummy control points for the response
    all_ctrl_pts = [ControlPoint(x=0.5, y=1.0, z=0.0), ControlPoint(x=2.0, y=1.0, z=0.0)]
    boundary_ctrl_pts = [ControlPoint(x=0.0, y=0.5, z=0.0), ControlPoint(x=1.0, y=1.0, z=0.0)]

    return RequestTrajResponse(
        success=True,
        status_message="Trajectory computed successfully.",
        all_ctrl_pts=all_ctrl_pts,
        boundary_ctrl_pts=boundary_ctrl_pts
    )

def request_traj_server():
    rospy.init_node('request_traj_server')
    rospy.Service('/visualize_suggestion', RequestTraj, handle_request_traj)
    rospy.loginfo("Ready to handle /visualize_suggestion service calls.")
    rospy.spin()

if __name__ == "__main__":
    request_traj_server()

