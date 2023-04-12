#!/bin/bash
####################################################################
############################| TASK#02 |#############################
#                           DESCRIPTION:                           
#     Simple script for backing up the /home /var/log directories,
#                 the config files of SSH, RDP, FTP
#          Cron task to run this script every Friday at 18:30.
#    Move the backup to a separate pre-created /archive directory
#-------------------------------------------------------------------
#               Written by Yuriy Shamray (aka Prospero)
#                           MIFIIB - 2023
#              Tested on Ubuntu 22.10 (codename: Kinetic)
####################################################################

# Backup HOME directory
tar cpf /archive/home-backup-$(date '+%d.%B.%Y_%H:%M').tar -C / home

# Backup SSH Config File
tar cpf /archive/ssh-backup-$(date '+%d.%B.%Y_%H:%M').tar -C / etc/ssh/sshd_config

# Backup RDP Config File
sudo tar cpf /archive/xrdp-backup-$(date '+%d.%B.%Y_%H:%M').tar -C / etc/xrdp/xrdp.ini

# Backup FTP Config file
sudo tar cpf /archive/vsftpd-backup-$(date '+%d.%B.%Y_%H:%M').tar -C / etc/vsftpd.conf

# Backup /var/log dir
sudo tar cpf /archive/varlog-backup-$(date '+%d.%B.%Y_%H:%M').tar -C / var/log

# To delete files older than 15 days
find /archive/* -mtime +15 -delete