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

################################################################################

Requires:       pattern() = enhanced_base

# dig, host and nslookup
Requires:       bind-utils

# kamarada/Linux-Kamarada-GNOME#24 - Firewall
Requires:       firewalld
Recommends:     firewalld-lang

Requires:       sudo

################################################################################

#Requires:       pattern() = x11

Requires:       xorg-x11-driver-video
Requires:       xorg-x11-fonts

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

# kamarada/Linux-Kamarada-GNOME#19 - GUI - Sound & Video - Webcam application
Requires:       cheese
Recommends:     cheese-lang

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

# kamarada/Linux-Kamarada-GNOME#25 - GUI - System - Partition manager
Requires:       gparted
Recommends:     gparted-lang

################################################################################

Requires:       pattern() = gnome_basis

Requires:       NetworkManager
Requires:       NetworkManager-applet
Recommends:     gdm-branding-openSUSE

# kamarada/Linux-Kamarada-GNOME#1 - GUI - System - Terminal
Requires:       gnome-terminal
Recommends:     gnome-terminal-lang

Recommends:     gtk2-branding-openSUSE
Recommends:     gtk3-branding-openSUSE
Recommends:     hicolor-icon-theme-branding-openSUSE

# kamarada/Linux-Kamarada-GNOME#2 - GUI - Accessories - File manager
Requires:       nautilus
Recommends:     nautilus-lang

# kamarada/Linux-Kamarada-GNOME#20 - GUI - GNOME core apps - Help (Yelp)
Requires:       yelp
Recommends:     yelp-lang

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

# kamarada/Linux-Kamarada-GNOME#23 - GUI - Games - Sudoku
Recommends:     gnome-sudoku
Recommends:     gnome-sudoku-lang

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

# kamarada/Linux-Kamarada-GNOME#23 - GUI - Games - Aisleriot
Recommends:     aisleriot
Recommends:     aisleriot-lang

# kamarada/Linux-Kamarada-GNOME#5 - GUI - Internet - Web browser
Requires:       chromium

# kamarada/Linux-Kamarada-GNOME#12 - GUI - Office - Calendar
Requires:       gnome-calendar
Recommends:     gnome-calendar-lang

# kamarada/Linux-Kamarada-GNOME#20 - GUI - GNOME core apps - Fonts (gnome-font-viewer)
Requires:       gnome-font-viewer
Recommends:     gnome-font-viewer-lang

# kamarada/Linux-Kamarada-GNOME#18 - GUI - Sound & Video - Sound recorder
Requires:       gnome-sound-recorder

# kamarada/Linux-Kamarada-GNOME#20 - GUI - GNOME core apps - To Do
Requires:       gnome-todo
Recommends:     gnome-todo-lang

Requires:       kernel-default

# kamarada/Linux-Kamarada-GNOME#14 - GUI - Office - Office suite
Requires:       libreoffice
Requires:       libreoffice-writer
Requires:       libreoffice-calc
Requires:       libreoffice-impress
Requires:       libreoffice-draw
Requires:       libreoffice-base
Requires:       libreoffice-math

# kamarada/Linux-Kamarada-GNOME#6 - GUI - Sound & Video - Media player
Requires:       vlc
Recommends:     vlc-lang

Requires:       xf86-video-fbdev
Requires:       xf86-video-vesa


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
