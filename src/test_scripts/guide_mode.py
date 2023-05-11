import numpy as np
from autolab_core import RigidTransform
from frankapy import FrankaArm 

if __name__ == "__main__":
    fa = FrankaArm()
    fa.reset_joints()
    # fa.run_guide_mode(20)