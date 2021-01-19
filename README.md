### Codes for creating a simple IoT application for controlling an device connected to Arduino  


##### Steps to setup your arduino
- Attach your device to Pin 13 of arduino (LED for example). Use relay if attaching any high voltage appliance.
- Attach arduino to your system using an UART-USB cable.
- Open ``arduino/ioot_led.ino`` in Arduino IDE and burn it in your board.
- You can get Port Name from serial monitor in IDE only.
- Make sure serial monitor is closed.

#### Steps to Setup your python environment and Start server 
- Install all required packages using requirements.txt
- Download ngrok and extract it in ngrok directory
- Do ``cd ngrok`` and execute ``./ngrok http 8000`` (port used should be same as used in server.py)
- You will get an http forwarding ip from the terminal, we will use this ip to control our device.
- Set ``SERVER_IP`` at line 125 in ``templates/index.html`` to the ip you received in above step. 
- Set ``COMM`` according to your arduino code and comm port name in which you will attach arduino in  
  ``server.py`` file
- Execute ``python server.py``
- Open your browser and test it out.


