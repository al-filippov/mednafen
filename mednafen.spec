Name:           mednafen
Version:        0.9.38.7
Release:        1%{?dist}
Summary:        A multi-system emulator utilizing OpenGL and SDL
#mednafen is a monstrosity build out of many emulators hence the colourful licensing
License:        GPLv2+ and BSD and ISC and LGPLv2+ and MIT and zlib 
URL:            http://mednafen.sourceforge.net
Source0:        http://mednafen.fobby.net/releases/files/mednafen-%{version}.tar.bz2
Patch0:         patch_abs_fix.patch
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
* Neo Geo Pocket (Color)
* WonderSwan
* GameBoy (Color)
* GameBoy Advance
* Nintendo Entertainment System
* Super Nintendo Entertainment System/Super Famicom
* Virtual Boy
* PC Engine/TurboGrafx 16 (CD)
* SuperGrafx
* PC-FX
* Sega Game Gear
* Sega Genesis/Megadrive
* Sega Master System
* Sony PlayStation
Mednafen has the ability to remap hotkey functions and virtual system
inputs to a keyboard, a joystick or both simultaneously. Save states are
supported, as is real-time game rewinding. Screen snapshots may be taken at the
press of a button and are saved in the popular PNG file format. To play Atari
Lynx games you will also need lynxboot.img which is not included for legal
reasons.


%prep
%setup -q -n %{name}
%patch -P0

# Permission cleanups for debuginfo
find \( -name \*.c\* -or -name \*.h\* \) -exec chmod -x {} \;


%build
%configure --disable-rpath
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# Documentation cleanup
rm -rf Documentation/*.def Documentation/*.php Documentation/generate.sh \
    Documentation/Makefile.* Documentation/docgen.inc

%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%doc AUTHORS ChangeLog COPYING TODO Documentation/*


%changelog
* Thu Dec 31 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.38.7-1
- Updated to 0.9.38.7

* Sun Sep 27 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.38.6-1
- Updated to 0.9.38.6

* Tue Jul 14 2015 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.38.5-1
- Updated to 0.9.38.5

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 0.9.33.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Apr 29 2014 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.33.3-1
- Updated to 0.9.33.3
- Updared the Source URL

* Sun Nov 10 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.32-0.1
- Updated to 0.9.32-WIP

* Tue May 14 2013 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.28-0.1
- Updated to 0.9.28-WIP

* Mon Apr 29 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.9.25-0.3
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 09 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.25-0.1
- Updated to 0.9.25-WIP

* Sat Aug 25 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.24-0.1
- Updated to 0.9.24-WIP

* Mon Jul 02 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.22-0.1
- Updated to 0.9.22-WIP

* Wed May 02 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.21-0.1
- Updated to 0.9.21-WIP
- Dropped upstreamed gcc-47 patch

* Fri Feb 10 2012 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.19-0.1
- Updated to 0.9.19-WIP
- Dropped obsolete Group, Buildroot, %%clean and %%defattr
- Updated %%description

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.9.18-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 27 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.18-0.1
- Updated to 0.9.18-WIP
- Dropped the NES sound patch

* Sat Aug 27 2011 Julian Weissgerber <sloevenh1@googlemail.com> - 0.9.17-0.2
- Patch to fix segfault when NES sound is enabled

* Wed Jun 15 2011 Julian Sikorski <belegdol@fedoraproject.org> - 0.9.17-0.1
- Updated to 0.9.17-WIP
- Updated the License tag

* Thu Apr 29 2010 Julian Sikorski <belegdol@fedoraproject.org> - 0.8.12-2.0.8.C
- Rebuilt for new libcdio

* Thu Jul 09 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.12-1.0.8.C
- Updated to 0.8.C
- Dropped the upstreamed gcc44 patch

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.8.11-2.0.8.B
- rebuild for new F11 features

* Sun Mar 08 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0.8.11-1.0.8.B
- Updated to 0.8.B
- ExcludeArch: ppc64 on Fedora 11+

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
