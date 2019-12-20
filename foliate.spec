%global appname com.github.johnfactotum.Foliate

Name:           foliate
Version:        1.5.3
Release:        1%{?dist}
Summary:        Simple and modern GTK eBook reader

License:        GPLv3+
URL:            https://johnfactotum.github.io/foliate/
Source0:        https://github.com/johnfactotum/foliate/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  appstream-glib-lib
BuildRequires:  meson
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
Requires:       hicolor-icon-theme
# For text-to-speech (TTS) support
# Recommends:     espeak-ng
# Support for viewing .mobi, .azw, and .azw3 files
# Recommends:     python3 >= 3.4
# Alternative text-to-speech (TTS) engines
# Suggests:       espeak
# Suggests:       festival

%description
A simple and modern GTK eBook viewer, built with GJS and Epub.js.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
# Ambiguous python shebang
find %{buildroot}%{_datadir}/%{appname}/assets/KindleUnpack/ -type f -name "*.py" -exec sed -e 's@/usr/bin/env python@/usr/bin/python3@g' -i "{}" \;
find %{buildroot}%{_datadir}/%{appname}/assets/KindleUnpack/ -type f -name "mobiml2xhtml.py" -exec sed -e 's@/usr/bin/python@/usr/bin/python3@g' -i "{}" \;

%find_lang %{appname}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appname}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appname}.desktop

%files -f %{appname}.lang
%license COPYING
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/%{appname}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_metainfodir}/%{appname}.appdata.xml

%changelog
# based on https://koji.fedoraproject.org/koji/packageinfo?packageID=28865
