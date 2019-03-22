# https://en.opensuse.org/openSUSE:Build_Service_Tutorial#Create_Patterns
# https://doc.opensuse.org/projects/libzypp/HEAD/zypp-pattern-packages.html
# https://build.opensuse.org/package/show/openSUSE:Leap:15.0/patterns-gnome

Name:           patterns-kamarada-gnome
Summary:        Patterns for Linux Kamarada with GNOME desktop
Url:            https://github.com/openSUSE/patterns
Version:        15.0.2018052601
Release:        0
Group:          Metapackages
License:        MIT
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Provides:       pattern() = kamarada-gnome
Provides:       pattern-visible()
#Provides:       pattern-icon() = pattern-kamarada-gnome
Provides:       pattern-order() = 1012

Requires:       kernel-default

Recommends:     branding-openSUSE

Requires:       pattern() = enhanced_base
# dig, host and nslookup
Requires:       bind-utils

Requires:       pattern() = x11_enhanced

Requires:       pattern() = gnome_basis
Requires:       MozillaFirefox
Recommends:     MozillaFirefox-branding-openSUSE
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

Requires:       pattern() = gnome_utilities
Requires:       gedit
Requires:       gnome-calculator


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
