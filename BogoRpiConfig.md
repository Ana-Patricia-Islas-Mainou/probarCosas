# Instructions to Configure Bogo's Raspberry Pi 4 or 5

The purpose of this file is to install the minimum configuration for any Bogobot's Raspberry Pi 4 or 5.

---
## Ubuntu 24.04.02 LTS Instalation

### Requiered Hardware

1. Personal Computer
2. Kingston or SanDisk Ultra MicroSD Card 64 GB minimum (do not use ADATA since the data transfer speed is tow low snd the RPi can no work properly).
3. Adapter to connect the MicroSD to the computer (if needed).

### Raspberry Pi Imager Install

1. Install the Rasberry Pi Imager needed for your OS from here: 
2. Excecute the installation file and acept terms and conditions.
3. Open the Raspberry Pi Imager program.
4. If the installation is succesfull you will see the following app in ypour computer.

<p align="center">
<img src="IMGS/rpi_imager.png" alt="Rpi_imager" width="300" height="200">
</p>

### Ubuntu 24.04.02 LTS with Raspberry Pi Imager

1. Open Raspberry Pi Imager and click on choose device and select Raspberry Pi 4 or Raspberry Pi 5 according to the RPi specificatcions.
2. Click on choose OS, scroll down and click in Other General Purpose OS -> Ubuntu -> Ubuntu Desktop 24.04.02 LTS (64-bit). Make sure you click on the RPi 4/400/5 Model.

<p align="center">
<img src="IMGS/choose_image.png" alt="Rpi_imager">
</p>

3. Select the target MircoSD and click on start.

4. Once the OS is installed, insert the MicroSD in the Raspberry Pi and conect it to the power source.

### Ubuntu 24.04.02 LTS Setup

The when configuing the OS system make sure you:

+ Select English Language
+ Select Mexico City Time Zone
+ Select Spanish Latin America Keyboard
+ Pin the Terminal to Desktop

Once your OS is configured update and upgrade apt
```nano 
sudo apt update
sudo apt upgrade
```

Install `raspi-config` to enable GIPO, I2C, ethernet among other features 

```nano 
sudo apt install raspi-config
```

Install `gedit` text editor for future use

```nano 
sudo apt-get install gedit
```

Install `pip` to download python packages

```nano 
sudo apt install python3-pip
```

Install `net-tools` for future use

```nano 
sudo apt install net-tools
```
---
## ROS2 Jazzy Jalisco Installation

This section contains the ROS2 Jazzy Jalisco Installation steps for Ubuntu. You can also find them in the [ROS2 Jazzy Jalisco Documentation](hhttps://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html#next-steps).

### System Setup

Setup requiered for install

```nano 
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings 
```

Enable Ubuntu Universe Repositories
```nano 
sudo apt install software-properties-common
sudo add-apt-repository universe
```

Add the ROS 2 GPG Key
```nano 
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```
Add the repository to your sources list
```nano 
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

Install development tools
```nano 
sudo apt update && sudo apt install ros-dev-tools
```

### Install ROS2 Jazzy

Update apt repository
```nano 
sudo apt update
```

Upgarde apt repository
```nano 
sudo apt upgrade
```

ROS2 Desktop Install
```nano 
sudo apt install ros-jazzy-desktop
```

### ROS2 Jazzy Test Install

Open a new terminal and excecute the follwong commands
```nano 
source /opt/ros/jazzy/setup.bash
ros2 topic list
```

If the installation is successfull you should be able to see  `\event_parameter` and  `\rosout` in your terminal.

Change to the root directoy and create the ROS2 Workspace.

```nano 
cd 
mkdir  ros2_ws/src
```

Change to your ROS2 Workspace and compile it to set it up.

```nano 
cd ros2_ws
colcon build
```

If everything worked properly you should recive a message saying `0 packages compiled` and when you run `ls` you should have the `build`, `install`, `log` and `src` directories.

### Configure `.bashrc` file

Change to the root directoy and open the `.bashrc` file using nano.

```nano 
cd 
nano .bashrc
```

Paste the following lines at the end of the `.bashrc` file to configure ROS2 enviorment in the terminal

```nano
source /opt/ros/humble/setup.bash
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
source /usr/share/colcon_cd/function/colcon_cd.sh
export _colcon_cd_root_=/opt/ros/humble
source ~/ros2_ws/install/setup.bash
```

Paste the following lines at the end of the `.bashrc` file to create an alias for easy ROS2 compilation and easy enviorment update.

```nano
alias cb="cd ~/ros2_ws; colcon build && source install/setup.bash" 
alias so="cd ~/ros2_ws; source install/setup.bash"
```

Save the `.bashrc` file, close the terminal and open a new one to apply changes.

---
## Dynamixel SDK Installation and Setup

Change to the `\ros2_ws\src` directory

```nano
cd
cd ros2_ws/src
```

Clone the [Robotis Dynamixel SDK GitHub Repository](https://github.com/ROBOTIS-GIT/DynamixelSDK) and compile ROS2 packages.


```nano
git clone https://github.com/ROBOTIS-GIT/DynamixelSDK
cb
```

If everything worked properly, you should see the correct compilation of packages `pkg`, `pkg` and `pkg`.

---
## MPU6050 Installation and Setup

### Hardware Setup

Take the MPU5060 and conect it to the Raspberry Pi as shown in the image below.

<p align="center">
<img src="IMGS/MPU6050.png" alt="MPU5060">
</p>

### Software Install
Install prerequiste packages

```nano
sudo apt install python3-smbus
```

Install [MPU5060 Package](https://github.com/m-rtijn/mpu6050)

```nano
pip install mpu6050-raspberrypi --break-system-packages
```

Open the main Raspberry Pi configuration window with 
```nano
sudo raspi-config
```

Scroll down to ***Interface Options*** and select it
<p align="center">
<img src="IMGS/raspi_config.png" alt="Rpi_imager">
</p>

Scroll down to ***I2C*** and select it to enable comunication.

<p align="center">
<img src="IMGS/raspi_interfaces.png" alt="Rpi_imager">
</p>

---
## HX711 Installation and Setup

### Hardware Setup

PENDING...

<p align="center">
<img src="IMGS/HX711.png" alt="HX711">
</p>

### Software Install
Install [HX711 Package](https://pypi.org/project/hx711-rpi-py/)

```nano
pip install hx711-rpi-py --break-system-packages
```

---
## Remote Conection with SSH

Open the main Raspberry Pi configuration window with 
```nano
sudo raspi-config
```

Scroll down to ***Interface Options*** and select it
<p align="center">
<img src="IMGS/raspi_config.png" alt="Rpi_imager">
</p>

Scroll down to ***SSH*** and select it to enable comunication.

<p align="center">
<img src="IMGS/raspi_interfaces_ssh.png" alt="Rpi_imager">
</p>

Install OpenSSH Server
```nano
sudo apt-get install openssh-server
```

Start and enable the SSH service
```nano
sudo systemctl start ssh
sudo systemctl enable ssh
```

**Reboot** the Raspberry Pi to apply changes

### Stablish Conection with Eternet

Connect the Ethernet cable from the Raspberry Pi to the computer as shown the followng images.

<p align="center">
<img src="IMGS/ethernet.png" alt="ethernet">
</p>

**In the Raspberry Pi** excecute the following command 
```nano
ifconfig
```

The ethernet port and IP adress should apear in the terminal.

<p align="center">
<img src="IMGS/ethernet_bogo.png" alt="ethernet">
</p>
 
**In your computer** (on Windows) excecute the following command 
```nano
ipconfig
```

**In your computer** (on Ubuntu/Linux) excecute the following command 
```nano
ifconfig
```

The ethernet port and IP adress should apear in the terminal.

<p align="center">
<img src="IMGS/ethernet_windows.png" alt="ethernet">
</p>

Note that they share the same network **192.168.137.###**, to check conectivity run a ping form your computer to the Raspberry Pi.

following command 
```nano
ping 192.168.137.102
```
If there is conectivity you should recieve a response from the IP Adress.

Conect to the Raspberry Pi using SSH
```nano
ssh bogo@192.168.137.102
```

### Stablish Conection with Hotspot

PENDING ...






















