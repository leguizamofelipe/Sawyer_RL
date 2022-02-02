
"use strict";

let IODataStatus = require('./IODataStatus.js');
let CameraControl = require('./CameraControl.js');
let IOComponentConfiguration = require('./IOComponentConfiguration.js');
let AnalogIOStates = require('./AnalogIOStates.js');
let HomingCommand = require('./HomingCommand.js');
let AnalogOutputCommand = require('./AnalogOutputCommand.js');
let NavigatorState = require('./NavigatorState.js');
let IOComponentCommand = require('./IOComponentCommand.js');
let CameraSettings = require('./CameraSettings.js');
let JointLimits = require('./JointLimits.js');
let IOComponentStatus = require('./IOComponentStatus.js');
let HeadState = require('./HeadState.js');
let IODeviceConfiguration = require('./IODeviceConfiguration.js');
let EndpointStates = require('./EndpointStates.js');
let AnalogIOState = require('./AnalogIOState.js');
let EndpointNamesArray = require('./EndpointNamesArray.js');
let NavigatorStates = require('./NavigatorStates.js');
let JointCommand = require('./JointCommand.js');
let EndpointState = require('./EndpointState.js');
let InteractionControlCommand = require('./InteractionControlCommand.js');
let CollisionAvoidanceState = require('./CollisionAvoidanceState.js');
let DigitalIOState = require('./DigitalIOState.js');
let IONodeConfiguration = require('./IONodeConfiguration.js');
let SEAJointState = require('./SEAJointState.js');
let RobotAssemblyState = require('./RobotAssemblyState.js');
let InteractionControlState = require('./InteractionControlState.js');
let DigitalIOStates = require('./DigitalIOStates.js');
let URDFConfiguration = require('./URDFConfiguration.js');
let IODeviceStatus = require('./IODeviceStatus.js');
let DigitalOutputCommand = require('./DigitalOutputCommand.js');
let IONodeStatus = require('./IONodeStatus.js');
let CollisionDetectionState = require('./CollisionDetectionState.js');
let HomingState = require('./HomingState.js');
let IOStatus = require('./IOStatus.js');
let HeadPanCommand = require('./HeadPanCommand.js');
let CalibrationCommandActionFeedback = require('./CalibrationCommandActionFeedback.js');
let CalibrationCommandGoal = require('./CalibrationCommandGoal.js');
let CalibrationCommandActionGoal = require('./CalibrationCommandActionGoal.js');
let CalibrationCommandFeedback = require('./CalibrationCommandFeedback.js');
let CalibrationCommandResult = require('./CalibrationCommandResult.js');
let CalibrationCommandAction = require('./CalibrationCommandAction.js');
let CalibrationCommandActionResult = require('./CalibrationCommandActionResult.js');

module.exports = {
  IODataStatus: IODataStatus,
  CameraControl: CameraControl,
  IOComponentConfiguration: IOComponentConfiguration,
  AnalogIOStates: AnalogIOStates,
  HomingCommand: HomingCommand,
  AnalogOutputCommand: AnalogOutputCommand,
  NavigatorState: NavigatorState,
  IOComponentCommand: IOComponentCommand,
  CameraSettings: CameraSettings,
  JointLimits: JointLimits,
  IOComponentStatus: IOComponentStatus,
  HeadState: HeadState,
  IODeviceConfiguration: IODeviceConfiguration,
  EndpointStates: EndpointStates,
  AnalogIOState: AnalogIOState,
  EndpointNamesArray: EndpointNamesArray,
  NavigatorStates: NavigatorStates,
  JointCommand: JointCommand,
  EndpointState: EndpointState,
  InteractionControlCommand: InteractionControlCommand,
  CollisionAvoidanceState: CollisionAvoidanceState,
  DigitalIOState: DigitalIOState,
  IONodeConfiguration: IONodeConfiguration,
  SEAJointState: SEAJointState,
  RobotAssemblyState: RobotAssemblyState,
  InteractionControlState: InteractionControlState,
  DigitalIOStates: DigitalIOStates,
  URDFConfiguration: URDFConfiguration,
  IODeviceStatus: IODeviceStatus,
  DigitalOutputCommand: DigitalOutputCommand,
  IONodeStatus: IONodeStatus,
  CollisionDetectionState: CollisionDetectionState,
  HomingState: HomingState,
  IOStatus: IOStatus,
  HeadPanCommand: HeadPanCommand,
  CalibrationCommandActionFeedback: CalibrationCommandActionFeedback,
  CalibrationCommandGoal: CalibrationCommandGoal,
  CalibrationCommandActionGoal: CalibrationCommandActionGoal,
  CalibrationCommandFeedback: CalibrationCommandFeedback,
  CalibrationCommandResult: CalibrationCommandResult,
  CalibrationCommandAction: CalibrationCommandAction,
  CalibrationCommandActionResult: CalibrationCommandActionResult,
};
