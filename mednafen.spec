%define _version 0.8.B

Name:           mednafen
Version:        0.8.11
Release:        1.%{_version}%{?dist}
Summary:        A multi-system emulator utilizing OpenGL and SDL
Group:          Applications/Emulators
License:        GPLv2+
URL:            http://mednafen.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{_version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{_version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gettext
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  SDL_net-devel >= 1.2.0
BuildRequires:  libsndfile-devel => 1.0.2
BuildRequires:  libcdio-devel
BuildRequires:  libGLU-devel
BuildRequires:  zlib-devel
BuildRequires:  jack-audio-connection-kit-devel

%description
A portable command-line driven, multi-system emulator which uses OpenGL and
SDL. It emulates the following:
* Atari Lynx
* Famicom
* GameBoy (Color)
* GameBoy Advance
* Neo Geo Pocket (Color)
* NES (NTSC & PAL)
* PC Engine
* TurboGrafx 16 (CD)
* SuperGrafx
* PC-FX
Mednafen has the ability to remap hotkey functions and virtual system
inputs to a keyboard, a joystick or both simultaneously. Save states are
supported, as is real-time game rewinding. Screen snapshots may be taken at the
press of a button and are saved in the popular PNG file format. To play Atari
Lynx games you will also need lynxboot.img which is not included for legal
reasons.


%prep
%setup -q -n %{name}

# Permission cleanups for debuginfo
chmod -x src/wswan/dis/*


%build
%configure --disable-rpath
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%find_lang %{name}


%clean
rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/%{name}
%doc AUTHORS ChangeLog COPYING TODO Documentation/*


%changelog
* Sun Mar 08 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.11-1.0.8.B
- Updated to 0.8.B

* Thu Nov  6 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.10-2.0.8.A
- Rebuilt. Something has mangled the x86_64 rpm

* Sun Nov  2 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.10-1.0.8.A
- Updated to 0.8.A

* Sat Sep 20 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.9-1
- Updated to 0.8.9
- Dropped the rpath patch, does not seem to be necessary

* Tue Jan 08 2008 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.7-1
- Upgrade to 0.8.7

* Sun Nov 25 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.5-1
- Upgrade to 0.8.5

* Sun Nov 18 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.4-1
- Upgrade to 0.8.4
- Removed several patches which have been applied upstream
- License change due to new guidelines
- New URL as project homepage has changed

* Sat Apr 28 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.1-2
- Added patch to fix crashes with wonderswan roms
- Added patch to fix compilation on ppc

* Thu Apr 26 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.1-1
- Upgrade to 0.8.1

* Tue Feb 13 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.7.2-1
- Upgrade to 0.7.2

* Wed Jan 03 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.7.1-1
- Upgrade to 0.7.1
- Updated rpath patch
- Added support for jack

* Fri Oct 06 2006 Ian Chapman <packages[AT]amiga-hardware.ocm> 0.6.5-2
- Rebuild for new version of libcdio in fc6

* Thu Sep 07 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.5-1
- Upgrade to 0.6.5

* Wed Aug 23 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.4-1
- Upgrade to 0.6.4
- Minor alteration to RPM description due to new features

* Sat Aug 12 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.3-1
- Upgrade to 0.6.3
- Drop the libtool buildrequire and use the patch for fixing rpath

* Mon Jun 19 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.2-1
- Upgrade to 0.6.2

* Sun Jun 04 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.1-2
- Removed gawk buildrequire. Doesn't seem to be needed.
- Removed bison buildrequire. Doesn't seem to be needed.
- Replaced xorg-x11-devel with libGLU-devel for compatibility reasons with
  modular and non modular X
- Removed SDL-devel buildrequire, implied by SDL_net-devel

* Tue May 23 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.6.1-1.iss
- Initial Release
