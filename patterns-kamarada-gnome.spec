# https://en.opensuse.org/openSUSE:Build_Service_Tutorial#Create_Patterns
# https://doc.opensuse.org/projects/libzypp/HEAD/zypp-pattern-packages.html
# https://build.opensuse.org/package/show/openSUSE:Leap:15.0/patterns-gnome

Name:           patterns-kamarada-gnome
Summary:        Patterns for Linux Kamarada with GNOME desktop
Url:            https://github.com/openSUSE/patterns
Version:        15.1
Release:        0
Group:          Metapackages
License:        MIT
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Provides:       pattern() = kamarada-gnome
Provides:       pattern-visible()
#Provides:       pattern-icon() = pattern-kamarada-gnome
Provides:       pattern-order() = 1012

################################################################################

Requires:       pattern() = apparmor

################################################################################

#Requires:       pattern() = base

Recommends:     branding-openSUSE

# kamarada/Linux-Kamarada-GNOME#48 - Time synchronization with NTP
Requires:       chrony

Recommends:     util-linux-lang

################################################################################

Requires:       pattern() = enhanced_base

# ll (alias of ls -l)
Requires:       aaa_base-extras

# dig, host and nslookup
Requires:       bind-utils

# cnf
Requires:       command-not-found

# kamarada/Linux-Kamarada-GNOME#41 - Printing support - CUPS
Requires:       cups
Requires:       cups-client

# kamarada/Linux-Kamarada-GNOME#24 - Firewall
Requires:       firewalld
Recommends:     firewalld-lang

# Filesystem in Userspace (FUSE)
Requires:       fuse

# kamarada/Linux-Kamarada-GNOME#37 - CLI - Text editor - JOE
Requires:       joe

Requires:       less

Requires:       man

# kamarada/Linux-Kamarada-GNOME#37 - CLI - Text editor - GNU nano
Requires:       nano
Recommends:     nano-lang

Requires:       netcat-openbsd

# Mount NTFS filesystems
Requires:       ntfs-3g

# Utilities for managing processes: pstree, killall and fuser
Requires:       psmisc
Recommends:     psmisc-lang

Requires:       sudo

# kamarada/Linux-Kamarada-GNOME#40 - Translations for Brazilian Portuguese (pt_BR)
Recommends:     translation-update
Suggests:       translation-update-en
Suggests:       translation-update-en_US
Suggests:       translation-update-pt
Suggests:       translation-update-pt_BR

# lsusb
Requires:       usbutils

# kamarada/Linux-Kamarada-GNOME#37 - CLI - Text editor - Vi and Vim
Requires:       vim

Requires:       wget

# kamarada/Linux-Kamarada-GNOME#8 - CLI - Archiving programs - Zip archives
Requires:       zip

################################################################################

#Requires:       pattern() = enhanced_base_opt

Requires:       man-pages
Requires:       man-pages-posix

# kamarada/Linux-Kamarada-GNOME#8 - CLI - Archiving programs - Zip archives
Requires:       unzip

Requires:       tcpdump

################################################################################

#Requires:       pattern() = minimal_base

# kamarada/Linux-Kamarada-GNOME#34 - GUI - System - System recovery
Requires:       snapper

################################################################################

#Requires:       pattern() = x11

Requires:       xorg-x11-driver-video
Requires:       xorg-x11-fonts

# kamarada/Linux-Kamarada-GNOME#38 - GUI - System - YaST
Requires:       libyui-qt
Requires:       libyui-qt-pkg
Requires:       yast2-control-center
Requires:       yast2-scanner

################################################################################

Requires:       pattern() = x11_enhanced

#Requires:       MozillaFirefox
#Recommends:     MozillaFirefox-translations
#Recommends:     MozillaFirefox-branding-openSUSE

################################################################################

#Requires:       pattern() = gnome_x11

# kamarada/Linux-Kamarada-GNOME#20 - GUI - GNOME core apps - Disk Usage Analyzer (Baobab)
Requires:       baobab
Recommends:     baobab-lang

# kamarada/Linux-Kamarada-GNOME#21 - GUI - Accessories - Notes
Requires:       bijiben
Recommends:     bijiben-lang

# kamarada/Linux-Kamarada-GNOME#29 - GUI - Sound & Video - CD/DVD burner
Requires:       brasero
Recommends:     brasero-lang

# kamarada/Linux-Kamarada-GNOME#19 - GUI - Sound & Video - Webcam application
Requires:       cheese
Recommends:     cheese-lang

Requires:       dconf-editor
Recommends:     dconf-editor-lang

# kamarada/Linux-Kamarada-GNOME#15 - GUI - Utilities - Document viewer
Requires:       evince
Requires:       evince-plugin-pdfdocument
Requires:       evince-plugin-xpsdocument
Requires:       evince-plugin-djvudocument
Requires:       evince-plugin-tiffdocument
Requires:       evince-plugin-psdocument
Recommends:     evince-lang

# kamarada/Linux-Kamarada-GNOME#24 - Firewall
Requires:       firewall-config

# kamarada/Linux-Kamarada-GNOME#42 - Bluetooth support
Requires:       gnome-bluetooth
Recommends:     gnome-bluetooth-lang

# kamarada/Linux-Kamarada-GNOME#20 - GUI - GNOME core apps - Characters
Requires:       gnome-characters
Recommends:     gnome-characters-lang

# kamarada/Linux-Kamarada-GNOME#20 - GUI - GNOME core apps - Clocks
Requires:       gnome-clocks
Recommends:     gnome-clocks-lang

# kamarada/Linux-Kamarada-GNOME#13 - GUI - Office - Address book
Requires:       gnome-contacts
Recommends:     gnome-contacts-lang

# kamarada/Linux-Kamarada-GNOME#20 - GUI - GNOME core apps - Disks (gnome-disk-utility)
Requires:       gnome-disk-utility
Recommends:     gnome-disk-utility-lang

# kamarada/Linux-Kamarada-GNOME#20 - GUI - GNOME core apps - Documents
Requires:       gnome-documents
Recommends:     gnome-documents-lang

# kamarada/Linux-Kamarada-GNOME#20 - GUI - GNOME core apps - Logs (gnome-logs)
Requires:       gnome-logs
Recommends:     gnome-logs-lang

# kamarada/Linux-Kamarada-GNOME#26 - GUI - System - Package updater
Requires:       gnome-packagekit
Recommends:     gnome-packagekit-lang
# These are installed by default with openSUSE:
Requires:       PackageKit
Requires:       PackageKit-backend-zypp
Requires:       PackageKit-branding-openSUSE
Requires:       PackageKit-gstreamer-plugin
Requires:       PackageKit-gtk3-module
Recommends:     PackageKit-lang

# kamarada/Linux-Kamarada-GNOME#25 - GUI - System - Partition manager
Requires:       gparted
Recommends:     gparted-lang

# kamarada/Linux-Kamarada-GNOME#41 - Printing support - Gutenprint
Requires:       gutenprint

# kamarada/Linux-Kamarada-GNOME#45 - GUI - Internet - Instant messaging client
Requires:       pidgin
Requires:       libpurple-plugin-facebook
Recommends:     libpurple-lang

# kamarada/Linux-Kamarada-GNOME#28 - GUI - Utilities - Password manager
Requires:       seahorse
Recommends:     seahorse-lang

# kamarada/Linux-Kamarada-GNOME#35 - GUI - Utilities - Remote desktop client
Requires:       vinagre
Recommends:     vinagre-lang

# kamarada/Linux-Kamarada-GNOME#39 - XDG user directories
Requires:       xdg-user-dirs
Recommends:     xdg-user-dirs-lang
Requires:       xdg-user-dirs-gtk
Recommends:     xdg-user-dirs-gtk-lang

################################################################################

Requires:       pattern() = gnome_basis

Requires:       NetworkManager
Requires:       NetworkManager-applet
Recommends:     gdm-branding-kamarada

# kamarada/Linux-Kamarada-GNOME#33 - GUI - System - Power statistics
Requires:       gnome-power-manager
Recommends:     gnome-power-manager-lang

# kamarada/Linux-Kamarada-GNOME#1 - GUI - System - Terminal
Requires:       gnome-terminal
Recommends:     gnome-terminal-lang

# we need something for xdg-su
Requires:       libgnomesu
Recommends:     libgnomesu-lang

# kamarada/Linux-Kamarada-GNOME#2 - GUI - Accessories - File manager
Requires:       nautilus
# Notifies when a USB stick is plugged in
Requires:       gvfs-backends
Recommends:     nautilus-lang

# kamarada/Linux-Kamarada-GNOME#46 - Support to Windows networks and Active Directory
Requires:       samba

# kamarada/Linux-Kamarada-GNOME#20 - GUI - GNOME core apps - Help (Yelp)
Requires:       yelp
Recommends:     yelp-lang

# kamarada/Linux-Kamarada-GNOME#36 - GUI - Artwork for 15.1 - Branding packages
Recommends:     gio-branding-kamarada
Recommends:     gtk2-branding-kamarada
Recommends:     gtk3-branding-kamarada
Recommends:     hicolor-icon-theme-branding-openSUSE

################################################################################

#Requires:       pattern() = gnome_basic

# kamarada/Linux-Kamarada-GNOME#7 - GUI - Utilities - Archive manager
Requires:       file-roller
Recommends:     file-roller-lang

# kamarada/Linux-Kamarada-GNOME#20 - GUI - GNOME core apps - Software
Requires:       gnome-software
Recommends:     gnome-software-lang

# kamarada/Linux-Kamarada-GNOME#9 - GUI - Utilities - System monitor
Requires:       gnome-system-monitor
Recommends:     gnome-system-monitor-lang

# kamarada/Linux-Kamarada-GNOME#22 - GUI - Utilities - Tweaks
Requires:       gnome-tweak-tool
Recommends:     gnome-tweak-tool-lang
Requires:       gsettings-backend-dconf

# kamarada/Linux-Kamarada-GNOME#2 - GUI - Accessories - File manager - Open in Terminal
Requires:       nautilus-extension-terminal

################################################################################

#Requires:       pattern() = gnome_games

# kamarada/Linux-Kamarada-GNOME#23 - GUI - Games - Chess
Recommends:     gnome-chess
Recommends:     gnome-chess-lang
Recommends:     gnuchess

# kamarada/Linux-Kamarada-GNOME#23 - GUI - Games - Mahjongg
Recommends:     gnome-mahjongg
Recommends:     gnome-mahjongg-lang

# kamarada/Linux-Kamarada-GNOME#23 - GUI - Games - Mines
Recommends:     gnome-mines
Recommends:     gnome-mines-lang

# kamarada/Linux-Kamarada-GNOME#23 - GUI - Games - Nibbles
Recommends:     gnome-nibbles
Recommends:     gnome-nibbles-lang

# kamarada/Linux-Kamarada-GNOME#23 - GUI - Games - Sudoku
Recommends:     gnome-sudoku
Recommends:     gnome-sudoku-lang

# kamarada/Linux-Kamarada-GNOME#23 - GUI - Games - Iagno
Recommends:     iagno
Recommends:     iagno-lang

# kamarada/Linux-Kamarada-GNOME#23 - GUI - Games - Quadrapassel
Recommends:     quadrapassel
Recommends:     quadrapassel-lang

################################################################################

#Requires:       pattern() = gnome_imaging

# kamarada/Linux-Kamarada-GNOME#17 - GUI - Utilities - Image viewer
Requires:       eog
Recommends:     eog-lang

# kamarada/Linux-Kamarada-GNOME#16 - GUI - Graphics - Scanning
Requires:       simple-scan
Recommends:     simple-scan-lang

# kamarada/Linux-Kamarada-GNOME#20 - GUI - GNOME core apps - Photos
Requires:       gnome-photos
Recommends:     gnome-photos-lang

################################################################################

#Requires:       pattern() = gnome_internet

# kamarada/Linux-Kamarada-GNOME#11 - GUI - Internet - E-mail client
Requires:       evolution
Recommends:     evolution-lang

# kamarada/Linux-Kamarada-GNOME#53 - GNOME Online Accounts
Requires:       evolution-ews
Recommends:     evolution-ews-lang
Requires:       gnome-control-center-goa
Requires:       gnome-online-accounts
Recommends:     gnome-online-accounts-lang

# kamarada/Linux-Kamarada-GNOME#30 - GUI - Internet - BitTorrent client
Requires:       transmission
Requires:       transmission-gtk
Recommends:     transmission-gtk-lang

################################################################################

Requires:       pattern() = gnome_utilities

# kamarada/Linux-Kamarada-GNOME#4 - GUI - Accessories - Text editor
Requires:       gedit
Recommends:     gedit-lang

# kamarada/Linux-Kamarada-GNOME#3 - GUI - Accessories - Calculator
Requires:       gnome-calculator
Recommends:     gnome-calculator-lang

# kamarada/Linux-Kamarada-GNOME#10 - GUI - Utilities - Screenshot
Requires:       gnome-screenshot
Recommends:     gnome-screenshot-lang

# kamarada/Linux-Kamarada-GNOME#20 - GUI - GNOME core apps - Weather
Requires:       gnome-weather
Recommends:     gnome-weather-lang

################################################################################

#Requires:       pattern() = gnome_yast

# kamarada/Linux-Kamarada-GNOME#38 - GUI - System - YaST
Requires:       yast2-control-center-qt

################################################################################

#Requires:       pattern() = yast2_basis

# kamarada/Linux-Kamarada-GNOME#38 - GUI - System - YaST
# kamarada/Linux-Kamarada-GNOME#46 - Support to Windows networks and Active Directory
# kamarada/Linux-Kamarada-GNOME#48 - Time synchronization with NTP
Requires:       yast2-auth-client
Requires:       yast2-country
Requires:       yast2-metapackage-handler
Requires:       yast2-network
Requires:       yast2-ntp-client
Requires:       yast2-packager
Requires:       yast2-printer
Requires:       yast2-samba-client
Requires:       yast2-samba-server
Requires:       yast2-storage-ng
Requires:       yast2-sudo
Requires:       yast2-sysconfig
Requires:       yast2-theme
Requires:       yast2-users

################################################################################

#Requires:       pattern() = yast2_install_wf

# kamarada/Linux-Kamarada-GNOME#38 - GUI - System - YaST
Requires:       yast2-bootloader

################################################################################

# kamarada/Linux-Kamarada-GNOME#23 - GUI - Games - Aisleriot
Recommends:     aisleriot
Recommends:     aisleriot-lang

Requires:       bash-completion

# kamarada/Linux-Kamarada-GNOME#42 - Bluetooth support - Configuration that automatically enables all bluetooth devices
Requires:       bluez-auto-enable-devices

# kamarada/Linux-Kamarada-GNOME#5 - GUI - Internet - Web browser
Requires:       chromium

# kamarada/Linux-Kamarada-GNOME#43 - Smart card support
Requires:       coolkey

# kamarada/Linux-Kamarada-GNOME#40 - Translations for installed desktop files
Recommends:     desktop-translations

# Not really necessary, just in case anyone wants to make openSUSE related artwork
Recommends:     fifth-leg-font

# kamarada/Linux-Kamarada-GNOME#36 - GUI - Artwork for 15.1 - Adapta GTK theme
Requires:       gedit-theme-adapta

# kamarada/Linux-Kamarada-GNOME#12 - GUI - Office - Calendar
Requires:       gnome-calendar
Recommends:     gnome-calendar-lang

# kamarada/Linux-Kamarada-GNOME#20 - GUI - GNOME core apps - Fonts (gnome-font-viewer)
Requires:       gnome-font-viewer
Recommends:     gnome-font-viewer-lang

# kamarada/Linux-Kamarada-GNOME#36 - GUI - Artwork for 15.1 - Adapta GTK theme
Requires:       gnome-shell-extension-user-theme 
Requires:       gnome-shell-theme-adapta

# kamarada/Linux-Kamarada-GNOME#18 - GUI - Sound & Video - Sound recorder
Requires:       gnome-sound-recorder
Recommends:     gnome-sound-recorder-lang

# kamarada/Linux-Kamarada-GNOME#20 - GUI - GNOME core apps - To Do
Requires:       gnome-todo
Recommends:     gnome-todo-lang

# kamarada/Linux-Kamarada-GNOME#34 - GUI - System - System recovery
Requires:       grub2-snapper-plugin

# kamarada/Linux-Kamarada-GNOME#36 - GUI - Artwork for 15.1 - Adapta GTK theme
Requires:       gtk2-metatheme-adapta
Requires:       gtk3-metatheme-adapta

# kamarada/Linux-Kamarada-GNOME#41 - Printing support - HPLIP
Suggests:       hplip

Requires:       htop

# kamarada/Linux-Kamarada-GNOME#27 - GUI - System - Image writer
Requires:       imagewriter

Requires:       iotop

# Open JAR files with Java
Requires:       java-jar-launcher

Requires:       kernel-default

# Enables many hardware devices (including my Intel Dual Band Wireless-AC 8265)
Requires:       kernel-firmware

# Make Qt apps look nice on GNOME
Requires:       libqt5-qtbase-platformtheme-gtk3
Requires:       libqt5-qtstyleplugins-platformtheme-gtk2

# kamarada/Linux-Kamarada-GNOME#14 - GUI - Office - Office suite
Requires:       libreoffice
Requires:       libreoffice-writer
Requires:       libreoffice-calc
Requires:       libreoffice-impress
Requires:       libreoffice-draw
Requires:       libreoffice-base
Requires:       libreoffice-math
Requires:       libreoffice-gnome
Requires:       libreoffice-gtk3
Recommends:     libreoffice-branding-upstream
Recommends:     libreoffice-icon-theme-papirus
Suggests:       libreoffice-l10n-en
Suggests:       libreoffice-l10n-pt_BR

# kamarada/Linux-Kamarada-GNOME#47 - GUI - Internet - VoIP softphone
Requires:       linphone
Recommends:     liblinphone-lang

# kamarada/Linux-Kamarada-GNOME#43 - Smart card support
Requires:       mozilla-nss
Requires:       mozilla-nss-tools

# Spell-checker used by LibreOffice
Suggests:       myspell-en
Suggests:       myspell-en_US
Suggests:       myspell-lightproof-en
Suggests:       myspell-lightproof-pt_BR
Suggests:       myspell-pt_BR

# kamarada/Linux-Kamarada-GNOME#41 - Printing support - OpenPrinting
Requires:       OpenPrintingPPDs
Requires:       OpenPrintingPPDs-ghostscript
Requires:       OpenPrintingPPDs-hpijs
Requires:       OpenPrintingPPDs-postscript

# kamarada/Linux-Kamarada-GNOME#43 - Smart card support
Requires:       opensc
Requires:       pam_pkcs11

# kamarada/Linux-Kamarada-GNOME#36 - GUI - Artwork for 15.1 - Papirus icon theme
Requires:       papirus-icon-theme

# kamarada/Linux-Kamarada-GNOME#43 - Smart card support
Requires:       pcsc-ccid
Requires:       pcsc-lite
Requires:       pcsc-tools

# kamarada/Linux-Kamarada-GNOME#32 - GUI - Office - PDFsam
Recommends:     pdfsam-basic

# kamarada/Linux-Kamarada-GNOME#36 - GUI - Artwork for 15.1 - Plymouth theme
Recommends:     plymouth-branding-kamarada

# kamarada/Linux-Kamarada-GNOME#42 - Bluetooth audio (A2DP/HSP/HFP) support for the PulseAudio sound server
Requires:       pulseaudio-module-bluetooth

# kamarada/Linux-Kamarada-GNOME#41 - Printing support - Samba client
# kamarada/Linux-Kamarada-GNOME#46 - Support to Windows networks and Active Directory
Requires:       samba-client

# kamarada/Linux-Kamarada-GNOME#34 - GUI - System - System recovery
Requires:       snapper-zypp-plugin

Requires:       tree

Suggests:       ucode-amd
Suggests:       ucode-intel

# kamarada/Linux-Kamarada-GNOME#6 - GUI - Sound & Video - Media player
Requires:       vlc
Recommends:     vlc-lang

Requires:       whois

# kamarada/Linux-Kamarada-GNOME#44 - Wine
Requires:       wine
Recommends:     wine-32bit
Recommends:     wine-gecko
Recommends:     wine-mono

Requires:       xf86-video-fbdev
Requires:       xf86-video-vesa

# kamarada/Linux-Kamarada-GNOME#34 - GUI - System - System recovery
# kamarada/Linux-Kamarada-GNOME#38 - GUI - System - YaST
Requires:       yast2-proxy
Recommends:     yast2-qt-branding-kamarada
Suggests:       yast2-trans-en
Suggests:       yast2-trans-en_US
Suggests:       yast2-trans-pt
Suggests:       yast2-trans-pt_BR
Requires:       yast2-snapper
# Without yast2-x11, YaST Firstboot uses the ncurses interface
Requires:       yast2-x11

# kamarada/Linux-Kamarada-GNOME#40 - Translations for Brazilian Portuguese (pt_BR)
Recommends:     gnome-shell-extension-dash-to-dock-lang
Recommends:     gnome-shell-extension-topicons-plus-lang
Recommends:     gtk2-lang
Recommends:     gtk3-lang


%description
Install this package to have a fully functional Linux Kamarada installation with
GNOME desktop.


%prep
mkdir -p "%{buildroot}/usr/share/doc/packages/patterns"
i="kamarada-gnome"
echo "This file marks the pattern $i to be installed." \
    >"%{buildroot}/usr/share/doc/packages/patterns/$i.txt"


%clean
rm -r -f "$RPM_BUILD_ROOT"


%files
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/kamarada-gnome.txt
