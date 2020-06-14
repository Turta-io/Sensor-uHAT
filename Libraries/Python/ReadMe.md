# Python Libraries
This directory includes Python libraries for Turta Sensor uHAT.

## Index
* __Turta_Accel.py:__ Python Library for NXP MMA8491Q 3-Axis Accelerometer & Tilt Sensor.
* __Turta_Digital.py:__ Python Library for Digital IO Ports.
* __Turta_Env_280.py:__ Python Library for Bosch Sensortec BME280 Environmental Sensor.
* __Turta_IRRemote.py:__ Python Library for IR Remote Controller Transmitter.
* __Turta_UV_Light.py:__ Python Library for Silicon Labs Si1133 UV Index & Ambient Light Sensor.

## Installation of Python Libraries
* Use 'pip3 install turta-sensoruhat' to download and install libraries automatically.
* Use 'pip3 install --upgrade --user turta-sensoruhat' to update your libraries.
* Use 'pip3 uninstall turta-sensoruhat' to uninstall the libraries.
* If you wish to install libraries manually, copy the ingredients of Python folder to the project folder.

## Dependencies for Python Libraries
The package installer installs other libraries required for Sensor uHAT's operation.
* We're using 'SMBus' for I2C communication. To install it manually, type 'sudo pip3 install smbus' to the terminal.
* We're using 'RPi.GPIO' for GPIO access. To install it manually, type 'pip3 install RPi.GPIO' to the terminal.
* We're using Python 3 for the libraries and samples.

## Documentation
Visit [docs.turta.io](https://docs.turta.io) for documentation.
