execute_process(COMMAND "/home/sawyer/ros_ws_noetic/build/intera_sdk/intera_interface/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/sawyer/ros_ws_noetic/build/intera_sdk/intera_interface/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
