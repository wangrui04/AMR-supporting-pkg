import rospy
from uvatraj_msgs.srv import ExecuteTraj, ExecuteTrajRequest
from uvatraj_msgs.msg import ControlPoint
import numpy as np

def send_request():
    rospy.init_node('send_request_node')
    rospy.wait_for_service('/visualize_suggestion')
    try:
        visualize = rospy.ServiceProxy('/visualize_suggestion', ExecuteTraj)
        
        # Create a request object
        request = ExecuteTrajRequest()
        request.ctrl_points = []
        
        N = 10
        start_x, start_y = -0.965,-1.3
        end_x, end_y = 0.855,0.925

        # Generate control points
        x_values = np.linspace(start_x, end_x, N)
        y_values = np.linspace(start_y, end_y, N)

        for x, y in zip(x_values, y_values):
            request.ctrl_points.append(ControlPoint(x=x, y=y))
        
        # Assign the control points to the request
        request.control_points = control_points
        
        # Call the service
        response = visualize(request)
        
        # Print the response
        print("Success:", response.success)
        print("Message:", response.status_message)
    
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)


if __name__ == '__main__':
    send_request()
