#!/usr/bin/env bash

NC='\033[0m'; COPY="\033[31m"; STATUS='\033[0;36m'

echo -e "${STATUS}Setting Environment${NC}"

mkdir -p /tmp/Backup/Personal
echo -e "${COPY}Copying Documents${NC}"
cp -ir /home/$USER/Documents /tmp/Backup/Personal/
echo -e "${COPY}Copying Downloads${NC}"
cp -ir /home/$USER/Downloads /tmp/Backup/Personal/

mkdir -p /tmp/Backup/Personal/Media
echo -e "${COPY}Copying Pictures${NC}"
cp -ir /home/$USER/Pictures /tmp/Backup/Personal/Media/
echo -e "${COPY}Copying Music${NC}"
cp -ir /home/$USER/Music /tmp/Backup/Personal/Media/
echo -e "${COPY}Copying Videos${NC}"
cp -ir /home/$USER/Videos /tmp/Backup/Personal/Media/

mkdir -p /tmp/Backup/System/Icons
mkdir -p /tmp/Backup/System/Themes
mkdir -p /tmp/Backup/System/Configs
echo -e "${COPY}Copying .icons${NC}"
cp -ir /home/$USER/.icons/* /tmp/Backup/System/Icons
echo -e "${COPY}Copying .themes${NC}"
cp -ir /home/$USER/.themes/* /tmp/Backup/System/Themes
echo -e "${COPY}Copying .configs${NC}"
#cp -ir /home/$USER/.configs/* /tmp/Backup/System/Configs

echo -e "${STATUS}Generating Package List${NC}"
pacman -Qt > /tmp/Backup/System/packages.txt
pacman -Qm > /tmp/Backup/System/aur.txt

echo -e "${STATUS}Finishing up${NC}"
date > /tmp/Backup/dated
zip -r /home/$USER/${1}.zip /tmp/Backup/*

echo -e "${STATUS}cleaning generated temp${NC}"
rm -R /tmp/Backup

echo -e "${STATUS}Backup Generated at ${COPY}~${NC}"
