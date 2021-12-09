// Generated by gencpp from file intera_motion_msgs/WaypointOptions.msg
// DO NOT EDIT!


#ifndef INTERA_MOTION_MSGS_MESSAGE_WAYPOINTOPTIONS_H
#define INTERA_MOTION_MSGS_MESSAGE_WAYPOINTOPTIONS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace intera_motion_msgs
{
template <class ContainerAllocator>
struct WaypointOptions_
{
  typedef WaypointOptions_<ContainerAllocator> Type;

  WaypointOptions_()
    : label()
    , max_joint_speed_ratio(0.0)
    , joint_tolerances()
    , max_joint_accel()
    , max_linear_speed(0.0)
    , max_linear_accel(0.0)
    , max_rotational_speed(0.0)
    , max_rotational_accel(0.0)
    , corner_distance(0.0)  {
    }
  WaypointOptions_(const ContainerAllocator& _alloc)
    : label(_alloc)
    , max_joint_speed_ratio(0.0)
    , joint_tolerances(_alloc)
    , max_joint_accel(_alloc)
    , max_linear_speed(0.0)
    , max_linear_accel(0.0)
    , max_rotational_speed(0.0)
    , max_rotational_accel(0.0)
    , corner_distance(0.0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _label_type;
  _label_type label;

   typedef double _max_joint_speed_ratio_type;
  _max_joint_speed_ratio_type max_joint_speed_ratio;

   typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _joint_tolerances_type;
  _joint_tolerances_type joint_tolerances;

   typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _max_joint_accel_type;
  _max_joint_accel_type max_joint_accel;

   typedef double _max_linear_speed_type;
  _max_linear_speed_type max_linear_speed;

   typedef double _max_linear_accel_type;
  _max_linear_accel_type max_linear_accel;

   typedef double _max_rotational_speed_type;
  _max_rotational_speed_type max_rotational_speed;

   typedef double _max_rotational_accel_type;
  _max_rotational_accel_type max_rotational_accel;

   typedef double _corner_distance_type;
  _corner_distance_type corner_distance;





  typedef boost::shared_ptr< ::intera_motion_msgs::WaypointOptions_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::intera_motion_msgs::WaypointOptions_<ContainerAllocator> const> ConstPtr;

}; // struct WaypointOptions_

typedef ::intera_motion_msgs::WaypointOptions_<std::allocator<void> > WaypointOptions;

typedef boost::shared_ptr< ::intera_motion_msgs::WaypointOptions > WaypointOptionsPtr;
typedef boost::shared_ptr< ::intera_motion_msgs::WaypointOptions const> WaypointOptionsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::intera_motion_msgs::WaypointOptions_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::intera_motion_msgs::WaypointOptions_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace intera_motion_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'intera_core_msgs': ['/home/sawyer/ros_ws/src/intera_common/intera_core_msgs/msg', '/home/sawyer/ros_ws/devel/share/intera_core_msgs/msg'], 'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'intera_motion_msgs': ['/home/sawyer/ros_ws/src/intera_common/intera_motion_msgs/msg', '/home/sawyer/ros_ws/devel/share/intera_motion_msgs/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::intera_motion_msgs::WaypointOptions_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::intera_motion_msgs::WaypointOptions_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::intera_motion_msgs::WaypointOptions_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::intera_motion_msgs::WaypointOptions_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::intera_motion_msgs::WaypointOptions_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::intera_motion_msgs::WaypointOptions_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::intera_motion_msgs::WaypointOptions_<ContainerAllocator> >
{
  static const char* value()
  {
    return "1b4687d4e536269b06e629169723339f";
  }

  static const char* value(const ::intera_motion_msgs::WaypointOptions_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x1b4687d4e536269bULL;
  static const uint64_t static_value2 = 0x06e629169723339fULL;
};

template<class ContainerAllocator>
struct DataType< ::intera_motion_msgs::WaypointOptions_<ContainerAllocator> >
{
  static const char* value()
  {
    return "intera_motion_msgs/WaypointOptions";
  }

  static const char* value(const ::intera_motion_msgs::WaypointOptions_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::intera_motion_msgs::WaypointOptions_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Optional waypoint label\n\
string label\n\
\n\
# Ratio of max allowed joint speed : max planned joint speed (from 0.0 to 1.0)\n\
float64 max_joint_speed_ratio\n\
\n\
# Slowdown heuristic is triggered if tracking error exceeds tolerances - radians\n\
float64[] joint_tolerances\n\
\n\
# Maximum accelerations for each joint (only for joint paths) - rad/s^2.\n\
float64[] max_joint_accel\n\
\n\
\n\
###########################################################\n\
# The remaining parameters only apply to Cartesian paths\n\
\n\
# Maximum linear speed of endpoint - m/s\n\
float64 max_linear_speed\n\
\n\
# Maximum linear acceleration of endpoint - m/s^2\n\
float64 max_linear_accel\n\
\n\
# Maximum rotational speed of endpoint - rad/s\n\
float64 max_rotational_speed\n\
\n\
# Maximum rotational acceleration of endpoint - rad/s^2\n\
float64 max_rotational_accel\n\
\n\
# Used for smoothing corners for continuous motion - m\n\
# The distance from the waypoint to where the curve starts while blending from\n\
# one straight line segment to the next.\n\
# Larger distance:  trajectory passes farther from the waypoint at a higher speed\n\
# Smaller distance:  trajectory passes closer to the waypoint at a lower speed\n\
# Zero distance:  trajectory passes through the waypoint at zero speed\n\
float64 corner_distance\n\
";
  }

  static const char* value(const ::intera_motion_msgs::WaypointOptions_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::intera_motion_msgs::WaypointOptions_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.label);
      stream.next(m.max_joint_speed_ratio);
      stream.next(m.joint_tolerances);
      stream.next(m.max_joint_accel);
      stream.next(m.max_linear_speed);
      stream.next(m.max_linear_accel);
      stream.next(m.max_rotational_speed);
      stream.next(m.max_rotational_accel);
      stream.next(m.corner_distance);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct WaypointOptions_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::intera_motion_msgs::WaypointOptions_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::intera_motion_msgs::WaypointOptions_<ContainerAllocator>& v)
  {
    s << indent << "label: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.label);
    s << indent << "max_joint_speed_ratio: ";
    Printer<double>::stream(s, indent + "  ", v.max_joint_speed_ratio);
    s << indent << "joint_tolerances[]" << std::endl;
    for (size_t i = 0; i < v.joint_tolerances.size(); ++i)
    {
      s << indent << "  joint_tolerances[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.joint_tolerances[i]);
    }
    s << indent << "max_joint_accel[]" << std::endl;
    for (size_t i = 0; i < v.max_joint_accel.size(); ++i)
    {
      s << indent << "  max_joint_accel[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.max_joint_accel[i]);
    }
    s << indent << "max_linear_speed: ";
    Printer<double>::stream(s, indent + "  ", v.max_linear_speed);
    s << indent << "max_linear_accel: ";
    Printer<double>::stream(s, indent + "  ", v.max_linear_accel);
    s << indent << "max_rotational_speed: ";
    Printer<double>::stream(s, indent + "  ", v.max_rotational_speed);
    s << indent << "max_rotational_accel: ";
    Printer<double>::stream(s, indent + "  ", v.max_rotational_accel);
    s << indent << "corner_distance: ";
    Printer<double>::stream(s, indent + "  ", v.corner_distance);
  }
};

} // namespace message_operations
} // namespace ros

#endif // INTERA_MOTION_MSGS_MESSAGE_WAYPOINTOPTIONS_H