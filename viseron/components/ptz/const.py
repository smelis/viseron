"""Telegram-PTZ component constants."""

COMPONENT = "ptz"
DESC_COMPONENT = "Telegram bot to control pan-tilt-zoom cameras."

CONFIG_CAMERAS = "cameras"
CONFIG_HOST = "host"
CONFIG_CAMERA_PORT = "onvif_port"
CONFIG_CAMERA_USERNAME = "onvif_username"
CONFIG_CAMERA_PASSWORD = "onvif_password"
CONFIG_CAMERA_FULL_SWING_MIN_PAN = "camera_min_pan"
CONFIG_CAMERA_FULL_SWING_MAX_PAN = "camera_max_pan"
CONFIG_PTZ_PRESETS = "presets"
CONFIG_PRESET_NAME = "name"
CONFIG_PRESET_PAN = "pan"
CONFIG_PRESET_TILT = "tilt"
CONFIG_PRESET_ZOOM = "zoom"
CONFIG_PRESET_ON_STARTUP = "on_startup"

DESC_CAMERAS = "List of ONVIF cameras to make available to the component."
DESC_CAMERA_PORT = "ONVIF port of the camera."
DESC_CAMERA_USERNAME = "ONVIF username for the camera."
DESC_CAMERA_PASSWORD = "ONVIF password for the camera."
DESC_CAMERA_FULL_SWING_MIN_PAN = "Minimum pan value of the camera."
DESC_CAMERA_FULL_SWING_MAX_PAN = "Maximum pan value of the camera."
DESC_PTZ_PRESETS = "List of PTZ presets."
DESC_PRESET_NAME = "Name of the PTZ preset."
DESC_PRESET_PAN = "Pan value of the PTZ preset. Usually a value between -1.0 and 1.0."
DESC_PRESET_TILT = "Tilt value of the PTZ preset. Usually a value between -1.0 and 1.0."
DESC_PRESET_ZOOM = "Zoom value of the PTZ preset. Usually a value between -1.0 and 1.0?"
DESC_PRESET_ON_STARTUP = "Move to this (named) preset on startup."
