import sys
sys.path.append('../smart_grasping_sandbow/src/smart_grasping_sandbow')
from smart_grasper import SmartGrasper
# from smart_grasping_sandbow.src.smartg_grasping_sandbox.smart_grasper import SmartGrasper

smart_grasper = SmartGrasper()

smart_grasper.reset_world()

print(smart_grasper.get_current_pose())

