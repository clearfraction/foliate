%global appid com.github.johnfactotum.Foliate
%global abi_package %{nil}

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
BuildRequires:  appstream-glib glib-dev
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
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569975130
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


%files -f %{appid}.lang
%license COPYING
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
/usr/share/metainfo/%{appid}.appdata.xml


%changelog
# based on https://koji.fedoraproject.org/koji/packageinfo?packageID=28865
