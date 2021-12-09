
"use strict";

let HeadState = require('./HeadState.js');
let IODataStatus = require('./IODataStatus.js');
let HomingCommand = require('./HomingCommand.js');
let NavigatorState = require('./NavigatorState.js');
let InteractionControlCommand = require('./InteractionControlCommand.js');
let EndpointState = require('./EndpointState.js');
let RobotAssemblyState = require('./RobotAssemblyState.js');
let DigitalIOStates = require('./DigitalIOStates.js');
let CollisionAvoidanceState = require('./CollisionAvoidanceState.js');
let AnalogIOState = require('./AnalogIOState.js');
let IODeviceStatus = require('./IODeviceStatus.js');
let JointLimits = require('./JointLimits.js');
let AnalogOutputCommand = require('./AnalogOutputCommand.js');
let IOComponentCommand = require('./IOComponentCommand.js');
let IOComponentStatus = require('./IOComponentStatus.js');
let AnalogIOStates = require('./AnalogIOStates.js');
let CollisionDetectionState = require('./CollisionDetectionState.js');
let IONodeStatus = require('./IONodeStatus.js');
let URDFConfiguration = require('./URDFConfiguration.js');
let JointCommand = require('./JointCommand.js');
let DigitalOutputCommand = require('./DigitalOutputCommand.js');
let DigitalIOState = require('./DigitalIOState.js');
let HeadPanCommand = require('./HeadPanCommand.js');
let EndpointStates = require('./EndpointStates.js');
let NavigatorStates = require('./NavigatorStates.js');
let CameraSettings = require('./CameraSettings.js');
let CameraControl = require('./CameraControl.js');
let IOStatus = require('./IOStatus.js');
let EndpointNamesArray = require('./EndpointNamesArray.js');
let SEAJointState = require('./SEAJointState.js');
let HomingState = require('./HomingState.js');
let IODeviceConfiguration = require('./IODeviceConfiguration.js');
let InteractionControlState = require('./InteractionControlState.js');
let IONodeConfiguration = require('./IONodeConfiguration.js');
let IOComponentConfiguration = require('./IOComponentConfiguration.js');
let CalibrationCommandAction = require('./CalibrationCommandAction.js');
let CalibrationCommandActionResult = require('./CalibrationCommandActionResult.js');
let CalibrationCommandActionGoal = require('./CalibrationCommandActionGoal.js');
let CalibrationCommandResult = require('./CalibrationCommandResult.js');
let CalibrationCommandActionFeedback = require('./CalibrationCommandActionFeedback.js');
let CalibrationCommandGoal = require('./CalibrationCommandGoal.js');
let CalibrationCommandFeedback = require('./CalibrationCommandFeedback.js');

module.exports = {
  HeadState: HeadState,
  IODataStatus: IODataStatus,
  HomingCommand: HomingCommand,
  NavigatorState: NavigatorState,
  InteractionControlCommand: InteractionControlCommand,
  EndpointState: EndpointState,
  RobotAssemblyState: RobotAssemblyState,
  DigitalIOStates: DigitalIOStates,
  CollisionAvoidanceState: CollisionAvoidanceState,
  AnalogIOState: AnalogIOState,
  IODeviceStatus: IODeviceStatus,
  JointLimits: JointLimits,
  AnalogOutputCommand: AnalogOutputCommand,
  IOComponentCommand: IOComponentCommand,
  IOComponentStatus: IOComponentStatus,
  AnalogIOStates: AnalogIOStates,
  CollisionDetectionState: CollisionDetectionState,
  IONodeStatus: IONodeStatus,
  URDFConfiguration: URDFConfiguration,
  JointCommand: JointCommand,
  DigitalOutputCommand: DigitalOutputCommand,
  DigitalIOState: DigitalIOState,
  HeadPanCommand: HeadPanCommand,
  EndpointStates: EndpointStates,
  NavigatorStates: NavigatorStates,
  CameraSettings: CameraSettings,
  CameraControl: CameraControl,
  IOStatus: IOStatus,
  EndpointNamesArray: EndpointNamesArray,
  SEAJointState: SEAJointState,
  HomingState: HomingState,
  IODeviceConfiguration: IODeviceConfiguration,
  InteractionControlState: InteractionControlState,
  IONodeConfiguration: IONodeConfiguration,
  IOComponentConfiguration: IOComponentConfiguration,
  CalibrationCommandAction: CalibrationCommandAction,
  CalibrationCommandActionResult: CalibrationCommandActionResult,
  CalibrationCommandActionGoal: CalibrationCommandActionGoal,
  CalibrationCommandResult: CalibrationCommandResult,
  CalibrationCommandActionFeedback: CalibrationCommandActionFeedback,
  CalibrationCommandGoal: CalibrationCommandGoal,
  CalibrationCommandFeedback: CalibrationCommandFeedback,
};
