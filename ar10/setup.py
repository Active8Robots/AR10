from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup


setup_args = generate_distutils_setup(
    packages=['ros_ar10_class'],
    package_dir={'':'scripts'},
    requires=['std_msgs', 'rospy', 'geometry_msgs']
)

setup(**setup_args)
