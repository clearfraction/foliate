%global appid com.github.johnfactotum.Foliate
%global abi_package %{nil}

Name:           foliate
Version:        3.1.1
Release:        3
Summary:        Simple and modern GTK eBook reader
License:        GPLv3+
URL:            https://johnfactotum.github.io/foliate/
#Source0:        https://github.com/johnfactotum/foliate/archive/%%{version}/%%{name}-%%{version}.tar.gz
Source:         https://github.com/johnfactotum/foliate/archive/refs/heads/master.zip
BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  appstream-glib glib-dev
BuildRequires:  meson
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  webkitgtk60-dev
BuildRequires:  pkgconfig(iso-codes)
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
%setup -n foliate-master

%build
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang %{appid}

%post
glib-compile-schemas /usr/share/glib-2.0/schemas

%files -f %{appid}.lang
%license COPYING
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
/usr/share/metainfo/*.xml


%changelog
# based on https://koji.fedoraproject.org/koji/packageinfo?packageID=28865
