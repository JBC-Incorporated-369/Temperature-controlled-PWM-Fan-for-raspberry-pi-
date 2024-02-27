Setup instructions

Firstly SSH into your raspberry pi

Then run this command:  nano

Then copy and paste the fan.py script from fan.py.
then changen the GPIO pin to mach your pwm fan.
Change the on (Full Speed temperature) and low power
mode temperature to best suit your application.

Then save the file by pressing CTRL+O then input fan.py
as the file name. then press enter to save the file
Then exit the file by pressing CTRL+X

Now Run your script by running this command: python3 fan.py


To make the fan script run on startup, 

You can use the rc.local file in Linux. 
Here's how to do it:Open the rc.local file 
for editing by running the following command in the terminal:

sudo nano /etc/rc.local

Add the following line before the exit 0 line:

python3 /fan.py &

Save the file by pressing Ctrl + O, then press Enter.
Exit the editor by pressing Ctrl + X.
Make sure the script file has execute permissions by running:

sudo chmod +x /fan.py

Reboot your Raspberry Pi to apply the changes:

sudo reboot
