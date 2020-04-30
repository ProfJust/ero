# ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

# The setup.py is for catkin to use, and not for users to invoke.
# catkin will make sure setup.py installs files to the right location.
# If you invoke setup.py manually, you may break your ROS installation.

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['tutorial_package'],
    package_dir={'': 'src'},
)

setup(**setup_args)
