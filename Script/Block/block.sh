#!/bin/bash

cd Script/Block
sudo install -m 0600 -o root -g root usbguard-daemon.conf /etc/usbguard/usbguard-daemon.conf
sudo systemctl restart usbguard

echo "Block script finished"