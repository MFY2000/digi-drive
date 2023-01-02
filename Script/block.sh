sudo while (true) do uhubctl -l 1-1 -p 2 -a 0 -r 1 
echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/unbind

sudo shutdown -r now # reboot