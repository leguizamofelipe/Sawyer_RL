# Install script for directory: /home/sawyer/ros_ws/src/intera_sdk/intera_interface

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/sawyer/ros_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  include("/home/sawyer/ros_ws/build/intera_sdk/intera_interface/catkin_generated/safe_execute_install.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/intera_interface" TYPE FILE FILES "/home/sawyer/ros_ws/devel/include/intera_interface/SawyerPositionJointTrajectoryActionServerConfig.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/intera_interface" TYPE FILE FILES "/home/sawyer/ros_ws/devel/include/intera_interface/SawyerVelocityJointTrajectoryActionServerConfig.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/intera_interface" TYPE FILE FILES "/home/sawyer/ros_ws/devel/include/intera_interface/SawyerPositionFFJointTrajectoryActionServerConfig.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/sawyer/ros_ws/devel/lib/python2.7/dist-packages/intera_interface/cfg")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/intera_interface" TYPE DIRECTORY FILES "/home/sawyer/ros_ws/devel/lib/python2.7/dist-packages/intera_interface/cfg")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/sawyer/ros_ws/build/intera_sdk/intera_interface/catkin_generated/installspace/intera_interface.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/intera_interface/cmake" TYPE FILE FILES
    "/home/sawyer/ros_ws/build/intera_sdk/intera_interface/catkin_generated/installspace/intera_interfaceConfig.cmake"
    "/home/sawyer/ros_ws/build/intera_sdk/intera_interface/catkin_generated/installspace/intera_interfaceConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/intera_interface" TYPE FILE FILES "/home/sawyer/ros_ws/src/intera_sdk/intera_interface/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/intera_interface" TYPE PROGRAM FILES "/home/sawyer/ros_ws/build/intera_sdk/intera_interface/catkin_generated/installspace/home_joints.py")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/intera_interface" TYPE PROGRAM FILES "/home/sawyer/ros_ws/build/intera_sdk/intera_interface/catkin_generated/installspace/joint_trajectory_action_server.py")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/intera_interface" TYPE PROGRAM FILES "/home/sawyer/ros_ws/build/intera_sdk/intera_interface/catkin_generated/installspace/calibrate_arm.py")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/intera_interface" TYPE PROGRAM FILES "/home/sawyer/ros_ws/build/intera_sdk/intera_interface/catkin_generated/installspace/io_config_editor.py")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/intera_interface" TYPE PROGRAM FILES "/home/sawyer/ros_ws/build/intera_sdk/intera_interface/catkin_generated/installspace/send_urdf_fragment.py")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/intera_interface" TYPE PROGRAM FILES "/home/sawyer/ros_ws/build/intera_sdk/intera_interface/catkin_generated/installspace/enable_robot.py")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/intera_interface" TYPE DIRECTORY FILES "/home/sawyer/ros_ws/src/intera_sdk/intera_interface/scripts/" USE_SOURCE_PERMISSIONS)
endif()

