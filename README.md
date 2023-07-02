# Collision Detection Smart Helmet

The Collision Detection Smart Helmet is a project aimed at enhancing the safety of motorcycle riders by providing real-time collision detection and alert systems. This repository contains the source code, documentation, and resources related to the development of the project.

## **Features**

**Collision Detection**: Utilizes computer vision techniques and machine learning models to detect potential collisions with vehicles or obstacles in front of the motorcycle.

**Rear Proximity Detection**: Includes a sensor-based system to detect objects in the blind spot behind the rider, providing warnings when necessary.

**Distinctive Warning System**: Generates audible alerts with distinctive type of sound using a piezo buzzer to notify the rider of potential collision threats.

**Remote Access**: Enables remote control and management of the helmet's functionalities via a connected computer or laptop.

## **Hardware Specification**
Raspberry Pi 4 4GB microcomputer board X1 (For better performance, can also use Nvidia Jetson Nano)

Pi-camera (Official pi-camera 64MP) X1 

HC-SR02 Ultrasonic Sensor X1

Piezo buzzer X3

## **Software Specification**
Python

OpenCV

VNC Viewer (for PC)

VNC Server (For micro-computer)

Darknet framework for object detection (refer documentation for how to get the neccessary files)

## **Installation and Setup**
Clone the repository: Use the command git clone <repository-url> to clone the project repository to your local machine.

Hardware Setup: Follow the hardware setup instructions provided in the documentation to configure the Raspberry Pi and connect the required components.

Software Setup: Install the necessary dependencies and libraries as outlined in the project documentation. Ensure that Python, OpenCV, GPIO, and Darknet are installed and configured correctly.

Configuration: Customize the system parameters and settings according to your requirements.

Build and Run: Compile and run the project code on the Raspberry Pi using the provided instructions.

For detailed installation, setup, and usage instructions, please refer to the project documentation included in the repository.

**Obtaining the Darknet Folder**

The Darknet folder should be in the same folder as the code provided.

To obtain the Darknet folder for object detection, please follow these steps:

Visit the official Darknet repository on GitHub at https://github.com/AlexeyAB/darknet.
Clone the Darknet repository to your local machine using the command git clone https://github.com/AlexeyAB/darknet.git.
Follow the instructions in the Darknet repository's documentation to build and configure the framework for your specific environment.
Contributions, bug reports, and feature requests for the Collision Detection Smart Helmet project are welcome. If you encounter any issues or have suggestions for improvements, please submit a pull request or open an issue in the repository.

## **License**
This project is licensed under the MIT License, which allows for the use, modification, and distribution of the code.

## **Acknowledgments**
We would like to acknowledge the support and guidance of our project supervisor and the contributions of all project team members.

**Contact**
For any inquiries or further information about the project, please contact:

Project Developer: Sarawit A/L Thanat (c08@live.com.my)
We appreciate your interest in our project and hope it contributes to enhancing motorcycle rider safety on the road.

