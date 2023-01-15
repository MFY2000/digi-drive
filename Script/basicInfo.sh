# sudo "$2" "$3"


if [ "$1" -e '' ]; then
  sudo usermod -l "$1" "$2"  
fi



if [ "$3" -e '' ]; then
  sudo hostnamectl set-hostname "$7"  
fi

if [ "$4" -ne 0 ]; then
    pactl set-sink-mute 0 1
fi

if [ "$5" -ne 0 ]; then
    sudo apt update
fi

if [ "$6" -ne 0 ]; then
    sudo apt upgrade
fi
