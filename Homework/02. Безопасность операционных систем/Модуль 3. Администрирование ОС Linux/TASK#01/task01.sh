#!/bin/bash
####################################################################
############################| TASK#01 |#############################
#                           DESCRIPTION
#        Add Backports Repository (for Ubuntu based systems)
#                  Install Apache2, Python, SSH, FTP
#-------------------------------------------------------------------
#               Written by Yuriy Shamray (aka Prospero)
#                           MIFIIB - 2023
#              Tested on Ubuntu 22.10 (codename: Kinetic)
####################################################################
#############################| COLORS |#############################
# Regular Colors
nocolor='\033[0m'    # Text Reset
yellow='\033[1;33m'  # Yellow
purple='\033[1;35m'  # Purple
green='\033[1;32m'   # Green
cyan='\033[1;36m'    # Cyan
red='\033[1;31m'     # Red
#------------------------------------------------------------------
# Icons
icon_ok='▸'
icon_ko='⚠'
icon_stage='↯'
icon_wait='▹'
icon_light='☺'
icon_arrowr='→'
####################################################################
# Distro Info
echo "\n${cyan}${icon_wait} Linux Distro Information ${nocolor}"
sleep 2
lsb_release -a
sleep 3
# sudo password reminder
echo "\n${yellow}[${icon_light} INFO] Please enter your password if requested! ${nocolor}"
############################| STAGE#01 |############################
# Checking if the Backports repo is in the source.list
sleep 2
echo "\n${purple}[${icon_stage} STAGE#01] - ${cyan}${icon_wait} Checking ${icon_arrowr} /etc/apt/sources.list ${nocolor}\n"
sleep 2

if grep -R "jammy-backports" /etc/apt/sources.list
then
    echo -n "${green}${icon_ok} Backports Repository already exists!\n"
    sleep 2
else
    echo -n "${red}${icon_ko} Backports Repository not found!"; sleep 2; echo "${cyan} ${icon_wait} Adding ${icon_arrowr} /etc/apt/sources.list ${nocolor}\n"
    echo "deb http://archive.ubuntu.com/ubuntu jammy-backports main restricted universe multiverse" | sudo sh -c 'cat >> /etc/apt/sources.list'
    sleep 2
    echo "${green}${icon_ok} Backports Repository has been added! ${nocolor}" && tail -n 1 /etc/apt/sources.list
fi

####################################################################
############################| STAGE#02 |############################
# Update packages
echo "\n${purple}[${icon_stage} STAGE#02] - ${cyan}${icon_wait} Starting update packages ${nocolor}"
sleep 2
sudo apt update
#-------------------------------------------------------------------
# Uncomment if you wish to upgrade system
# sudo apt upgrade -y 
#-------------------------------------------------------------------
echo "${green}${icon_ok} Updated Successfully!\n"

####################################################################
############################| STAGE#03 |############################
# Install Apache2 & Requirements
# Check Apache
sleep 2
echo -n "${purple}[${icon_stage} STAGE#03] - ${cyan}${icon_wait} Checking Apache Server ${nocolor}\n"
sleep 2
if ! apache2 -v 2>/dev/null 
then
    echo -n "\n${red}${icon_ko} Apache Server not found!";sleep 2; echo "${cyan} ${icon_wait} Installing Apache Server ${nocolor}"
    sleep 2
    sudo apt install apache2 apache2-doc apache2-utils -y
    echo -n "\n${green}${icon_ok} Apache Server Installed Successfully! ${nocolor}\n"
    sleep 2
    apache2 -v
else
    echo "${green}${icon_ok} Apache Server already installed!"
fi
#-------------------------------------------------------------------
# Check Apache service
sleep 2
echo -n "\n${cyan}${icon_wait} Checking Apache Service Status"
sleep 2
if systemctl is-active -q apache2
then
    echo "${green} ${icon_ok} Active (running) ${nocolor}"
else
    echo "${red} ${icon_ko} Inactive (stopped) ${nocolor}"
fi
#-------------------------------------------------------------------
# Changing ownership on the /var/www directory
sleep 2
echo -n "\n${cyan}${icon_wait} Changing ownership ${icon_arrowr} /var/www ${nocolor}"
sudo chown -R $USER:$USER /var/www && sleep 2; echo "${green}${icon_ok} Done!"
#-------------------------------------------------------------------
# Landing Page http://mifiib
sleep 2
echo -n "\n${cyan}${icon_wait} Creating a landing page ${icon_arrowr} /var/www/html/index.html ${nocolor}"
sleep 2
cd /var/www/html/
echo '<!DOCTYPE html>' > index.html
echo '<html>' >> index.html
echo '<head>' >> index.html
echo '<title>MIFIIB webpage</title>' >> index.html
echo '<meta charset="UTF-8">' >> index.html
echo '</head>' >> index.html
echo '<body>' >> index.html
echo '<h1>Welcome to MIFIIB webpage! Have a great day!</h1>' >> index.html
echo '</body>' >> index.html
echo '</html>' >> index.html
echo "${green}${icon_ok} Done! ${icon_arrowr} http://mifiib"
#-------------------------------------------------------------------
# Insert/update hosts entry
sleep 2
echo -n "\n${cyan}${icon_wait} Inserting a new entry ${icon_arrowr} /etc/hosts ${nocolor}"
echo "127.0.0.1       localhost" > ./temp_hosts
echo "127.0.0.1       mifiib" >> ./temp_hosts
cat /etc/hosts | tail -n +2 >> ./temp_hosts
sudo sh -c 'cat ./temp_hosts > /etc/hosts'
rm ./temp_hosts
sleep 2
echo "${green}${icon_ok} Done! ${nocolor}"

####################################################################
############################| STAGE#04 |############################
# Install Python
sleep 2
echo "\n${purple}[${icon_stage} STAGE#04] - ${cyan}${icon_wait} Checking Python ${nocolor}\n"
sleep 2
#-------------------------------------------------------------------
# Uncomment the lines below if Python is not installed
# because it was tested on a system with Python pre-installed.
#if ! python3 --version 2>/dev/null
#then
#   echo -n "${red} ${icon_ko} Python not found!"
#-------------------------------------------------------------------
echo "${cyan}${icon_wait} Installing Python ${nocolor}\n"
sleep 2
echo "${cyan}${icon_wait} Installing important packages ${nocolor}"
sudo apt install software-properties-common -y && echo "${green}${icon_ok} Done! ${nocolor}\n"
sleep 2
echo "${cyan}${icon_wait} Installing repo for Python 3.10 ${nocolor}"
sudo add-apt-repository ppa:deadsnakes/ppa -y && echo "${green}${icon_ok} Done! ${nocolor}\n"
sleep 2
echo "${green}${icon_ok} Python Installed Successfully! ${nocolor}"
sleep 2
python3 --version 
#-------------------------------------------------------------------
#else
#    sleep 2
#    echo "${green}${icon_ok} Python already installed! ${nocolor}"
#fi

####################################################################
############################| STAGE#05 |############################
# Install & Setup SSH
sleep 2
echo "\n${purple}[${icon_stage} STAGE#05] - ${cyan}${icon_wait} Checking SSH Server ${nocolor}\n"
sleep 2

if ! ssh -V 2>/dev/null
then
    echo -n "${red}${icon_ko} SSH Server not found!";sleep 2; echo "${cyan} ${icon_wait} Installing OpenSSH ${nocolor}"
    sleep 2
    sudo apt install openssh-server -y
    sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.factory-defaults
    sudo chmod a-w /etc/ssh/sshd_config.factory-defaults
    # Change SSH port from 22 to 2222
    sudo sed -i -e 's/#Port 22/Port 2222\n#Port 22/g' /etc/ssh/sshd_config
    # Disable SSH password login
    sudo sed -i -e 's/#PasswordAuthentication yes/PasswordAuthentication no\n#PasswordAuthentication yes/g' /etc/ssh/sshd_config
    sudo systemctl start ssh
    echo -n "\n${green}${icon_ok} OpenSSH Server Installed Successfully! ${nocolor}";sleep 2; ssh -V
else
    ssh -V
    echo "${green}${icon_ok} SSH Server already installed! ${nocolor}"
fi
#--------------------------------------------------------------------
# Check SSH service
sleep 2
echo -n "\n${cyan}${icon_wait} Checking SSH Service Status ${nocolor}"
if systemctl is-active -q ssh
then
    sleep 2
    echo "${green}${icon_ok} Active (running) ${nocolor}"
else
    echo "${red}${icon_ko} Inactive (stopped) ${nocolor}"
    sleep 2
    echo "\n${cyan}${icon_wait} Starting SSH Service ${nocolor}"
    sleep 2
    sudo systemctl start ssh && echo "${green}${icon_ok} Done! ${nocolor}"
fi

####################################################################
############################| STAGE#06 |############################
# Install & Setup FTP
sleep 2
echo "\n${purple}[${icon_stage} STAGE#06] - ${cyan}${icon_wait} Checking VSFTPD (Very Secure FTP Daemon) ${nocolor}\n"
sleep 2
if ! vsftpd -version 2>/dev/null
then
    echo -n "${red}${icon_ko} VSFTPD not found!";sleep 2; echo "${cyan} ${icon_wait} Installing VSFTPD ${nocolor}"
    sleep 2
    sudo apt install vsftpd -y
# Backup /etc/vsftpd.conf
    sudo cp /etc/vsftpd.conf /etc/vsftpd.conf.backup
# Change /etc/vsftpd.conf
    sudo sed -i -e 's/#write_enable=YES/write_enable=YES/' /etc/vsftpd.conf 
    sudo sed -i -e 's/#local_umask=022/local_umask=022/' /etc/vsftpd.conf
    sudo sed -i -e 's/#xferlog_std_format=YES/xferlog_std_format=YES/' /etc/vsftpd.conf
    sudo sed -i -e 's/ssl_enable=NO/ssl_enable=YES/' /etc/vsftpd.conf
    sudo sed -i '/ssl_enable=YES/a ssl_tlsv1=YES' /etc/vsftpd.conf
    sudo sed -i '/ssl_tlsv1=YES/a ssl_sslv2=NO' /etc/vsftpd.conf
    sudo sed -i '/ssl_sslv2=NO/a ssl_sslv3=NO' /etc/vsftpd.conf
    sudo sed -i '/ssl_sslv3=NO/a allow_anon_ssl=NO' /etc/vsftpd.conf
    sudo sed -i '/allow_anon_ssl=NO/a force_local_data_ssl=YES' /etc/vsftpd.conf
    sudo sed -i '/force_local_data_ssl=YES/a force_local_logins_ssl=YES' /etc/vsftpd.conf
    sudo sed -i '/force_local_logins_ssl=YES/a ssl_ciphers=HIGH' /etc/vsftpd.conf
    sudo sed -i '/ssl_sslv3=NO/a user_sub_token=$USER' /etc/vsftpd.conf
    sudo sed -i '/user_sub_token=$USER/a local_root=/home/$USER/ftp' /etc/vsftpd.conf
    sudo sed -i '/ssl_ciphers=HIGH/a pasv_min_port=10000' /etc/vsftpd.conf
    sudo sed -i '/pasv_min_port=10000/a pasv_max_port=10100' /etc/vsftpd.conf
    sudo sed -i '/pasv_max_port=10100/a userlist_enable=YES' /etc/vsftpd.conf
    sudo sed -i '/userlist_enable=YES/a userlist_file=/etc/vsftpd.userlist' /etc/vsftpd.conf
    sudo sed -i '/userlist_enable=YES/a userlist_deny=NO' /etc/vsftpd.conf
    sudo sed -i '/userlist_deny=NO/a chroot_local_user=YES' /etc/vsftpd.conf
    sudo sed -i '/userlist_deny=NO/a allow_writeable_chroot=YES' /etc/vsftpd.conf
    sudo service vsftpd restart
    echo "\n${green}${icon_ok} VSFTPD Installed Successfully! ${nocolor}"
    sleep 2
    vsftpd -version
else
    echo "${green}${icon_ok} VSFTPD already installed! ${nocolor}"
    vsftpd -version
fi
#--------------------------------------------------------------------
#Check VSFTPD service
sleep 2
echo -n "\n${cyan}${icon_wait} Checking VSFTPD Service Status ${nocolor}"
if systemctl is-active -q vsftpd
then
    sleep 2
    echo "${green}${icon_ok} Active (running) ${nocolor}"
else
    echo "${red}${icon_ko} Inactive (stopped) ${nocolor}"
    sleep 2
    echo "\n${cyan}${icon_wait} Starting VSFTPD Service ${nocolor}"
    sleep 2
    sudo systemctl start vsftpd && echo "${green}${icon_ok} Done! ${nocolor}"
fi

####################################################################
############################| STAGE#07 |############################
# Install & Setup XRDP
sleep 2
echo "\n${purple}[${icon_stage} STAGE#07] - ${cyan}${icon_wait} Checking XRDP ${nocolor}\n"
sleep 2
if systemctl is-active -q xrdp
then
    sleep 2
    echo "${green}${icon_ok} Active (running) ${nocolor}"
else
    echo -n "${red}${icon_ko} Inactive (stopped) ${nocolor}"
    sleep 2
    echo "${cyan}${icon_wait} Installing XRDP and packages${nocolor}"
    sleep 2
    # install the xfce and xfce-goodies packages
    sudo apt install xfce4 xfce4-goodies -y
    # installing xrdp
    sudo apt install xrdp -y
fi
sleep 2
echo -n "\n${cyan}${icon_wait} Adding xfce4-session ${icon_arrowr} .xsession ${nocolor}"
sleep 2
echo "xfce4-session" | tee .xsession
sudo systemctl restart xrdp && echo "${green}${icon_ok} Done! ${nocolor}"

####################################################################
############################| STAGE#08 |############################
# Enabling UFW firewall and add rules for Apache, SSH, FTP, RDP
sleep 2
echo -n "\n${purple}[${icon_stage} STAGE#08] - ${cyan}${icon_wait} Checking UFW (Uncomplicated Firewall) ${nocolor}"
sleep 2
if sudo ufw status | grep -q inactive
then
    echo -n "${red}${icon_ko} Inactive"
    sleep 2
    echo "${cyan} ${icon_wait} Activating ${nocolor}"
    sleep 2
    sudo ufw enable 
else
    echo "${green}${icon_ok} Active (running) ${nocolor}"
fi
#-------------------------------------------------------------------
# Add rules for Apache, SSH, FTP, RDP
sleep 2
# Apache
echo "\n${cyan}${icon_wait} Adding Rules ${icon_arrowr} 'Apache' ${nocolor}"
sleep 2
sudo ufw allow from any to any port 80,443 proto tcp comment 'Open ports http/https'
sleep 2
# SSH
echo "\n${cyan}${icon_wait} Adding Rules ${icon_arrowr} 'SSH' ${nocolor}"
sleep 2
sudo ufw allow 2222/tcp comment 'Open port for SSH'
sleep 2
# FTP
echo "\n${cyan}${icon_wait} Adding Rules ${icon_arrowr} 'FTP' ${nocolor}"
sleep 2
sudo ufw allow from any to any port 20,21,10000:10100 proto tcp comment 'Open ports for FTP'
sleep 2
# RDP
echo "\n${cyan}${icon_wait} Adding Rules ${icon_arrowr} 'RDP' ${nocolor}"
sleep 2
sudo ufw allow from any to any port 3389 comment 'Open port for RDP'
sleep 2
# Display all rules
sudo ufw status numbered
echo "${green}${icon_ok} Done! ${nocolor}"

####################################################################
##########################| FINAL STAGE |###########################
# Autoclean Apt Cache
sleep 2
echo "\n${purple}[${icon_stage} FINALE STAGE] - ${cyan}${icon_wait} Autoclean Apt Cache ${nocolor}"
sleep 2
sudo apt autoclean && echo "\n${green}${icon_ok} ALL DONE!\n"