#!/bin/bash


cd Script/unBlock
sudo install -m 0600 -o root -g root usbguard-daemon.conf /etc/usbguard/usbguard-daemon.conf
sudo systemctl restart usbguard

echo "unblock script finished"
