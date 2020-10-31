# bronzebeard
Bare-metal RISC-V Forth implementation

## Supported Devices
[Longan Nano](https://www.seeedstudio.com/Sipeed-Longan-Nano-RISC-V-GD32VF103CBT6-Development-Board-p-4205.html)  
TODO [Wio Lite](https://www.seeedstudio.com/Wio-Lite-RISC-V-GD32VF103-p-4293.html)  
TODO [HiFive1 Rev B](https://www.sifive.com/boards/hifive1-rev-b)  

## Cables
USB-C for programming  
USB to TTL Serial for interacting (VCC attached to 5V, not 3.3V!)  

## Setup
Need custom build of dfu-util:
```
git clone git://git.code.sf.net/p/dfu-util/dfu-util
cd dfu-util
./autogen.sh
./configure
make
sudo make install
cd ..
rm -r dfu-util/
```

If you want to be able to do this stuff as non-root:  
Need udev rules (for the Longan Nano and serial cable[s]):
```
sudo vim /etc/udev/rules.d/99-bronzebeard.rules
```
```
# Longan Nano
ATTRS{idVendor}=="28e9", ATTRS{idProduct}=="0189", MODE="0666"
# Adafruit USB to TTL Serial Cable
ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", MODE="0666"
# SparkFun USB to TTL Serial Cable
ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", MODE="0666"
```
```
sudo udevadm control --reload
```

## Build
```
python3 -m venv venv
. venv/bin/activate
python forth.py
```

## Program
```
dfu-util --download forth.bin --alt 0 --dfuse-address 0x08000000:0x20000
```

## Usage
```
python -m serial.tools.miniterm /dev/ttyUSB0 115200
```
