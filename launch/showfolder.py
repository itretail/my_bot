import os
from ament_index_python.packages import get_package_share_directory

package_name='my_bot' #<--- CHANGE ME

joy_params = os.path.join(get_package_share_directory(package_name),'config','joystick.yaml')

print(joy_params)

