#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/sawyer/ros_ws/src/intera_sdk/intera_interface"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/sawyer/ros_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/sawyer/ros_ws/install/lib/python2.7/dist-packages:/home/sawyer/ros_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/sawyer/ros_ws/build" \
    "/usr/bin/python2" \
    "/home/sawyer/ros_ws/src/intera_sdk/intera_interface/setup.py" \
    egg_info --egg-base /home/sawyer/ros_ws/build/intera_sdk/intera_interface \
    build --build-base "/home/sawyer/ros_ws/build/intera_sdk/intera_interface" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/sawyer/ros_ws/install" --install-scripts="/home/sawyer/ros_ws/install/bin"
