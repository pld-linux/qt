Summary:	The Qt GUI application framework: Shared library
Summary(pl):	Biblioteka Qt do tworzenia GUI
Name:		qt
Version:	1.44
Release:	6
Copyright:	distributable
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://ftp.troll.no/qt/source/%{name}-%{version}.tar.gz
Patch0:		qt.patch
Patch1:		qt-opt.patch
Patch2:		qt-enablegif.patch
URL:		http://www.troll.no/
Buildroot:	/tmp/%{name}-%{version}-root
Conflicts:	glibc <= 2.0.7

%description
Contains the shared library needed to run Qt applications, as well as
the README files for Qt.

%description -l pl
Zawiera bibliotekê Qt wymagan± przez aplikacje, które z niej korzystaj±.

%package devel
Summary:	Include files and documentation needed to compile
Summary(pl):	Pliki nag³ówkowe, przyk³ady i dokumentacja do biblioteki 
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}
Requires:	%{name}-extensions = %{version}

%description devel
Contains the files necessary to develop applications using Qt: header
files, the Qt meta object compiler, man pages, HTML documentation and
example programs. See http://www.troll.no/ for more information about
Qt, or file:/usr/doc/%{name}-devel-%{version}/html/index.html for Qt
documentation in HTML.

%description -l pl devel
Pakiet tem zawiera pliki potrzebne do tworzenia i kompilacji aplikacji
korzystaj±cych z biblioteki Qt jak pliki nag³ówkowe, meta kompiler (moc),
dokumentacjê. Zobacz http://www.troll.no/ aby dowiedzieæ siê wiêcej o Qt.
Dokumentacjê do biblioteki znajdziesz tak¿e pod:
/usr/doc/%{name}-%{version}/html/index.html  

%package extensions
Summary:	Qt extensions, library and headers file
Summary(pl):	Qt extensions, rozrze¿enia dla QT biblioteki i pliki nag³ówkowe 
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}
Conflicts:	glibc <= 2.0.7

%description extensions
Contains the Qt extension files with library and include files.
Contains extension for Motif/Lesstif, OpenGL, image manipulation.

%description -l pl extensions
Pakiet zawiera zestaw rozsze¿eñ dla biblioteki Qt. Biblioteki oraz pliki
nag³ówkowe dla nastêpuj±cych pakietów: Motif/Lestif, OpenGL, Netscape oraz
operacji na obrazach.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
QTDIR=`/bin/pwd`; export QTDIR
make linux-g++-shared

LD_LIBRARY_PATH=/usr/X11R6/lib make

(cd extensions/imageio/src; LD_LIBRARY_PATH=/usr/X11R6/lib make)
(cd extensions/opengl/src; LD_LIBRARY_PATH=/usr/X11R6/lib make)
(cd extensions/xt/src; LD_LIBRARY_PATH=/usr/X11R6/lib \
 make INCPATH="-I/usr/X11R6/include -I../../../include")

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/{bin,include/X11/qt,lib,man/{man1,man3}}

install -s bin/moc $RPM_BUILD_ROOT/usr/X11R6/bin/moc
install -s lib/libqt.so.*.* $RPM_BUILD_ROOT/usr/X11R6/lib
ln -sf libqt.so.%{version} $RPM_BUILD_ROOT/usr/X11R6/lib/libqt.so
install man/man1/* $RPM_BUILD_ROOT/usr/X11R6/man/man1
install man/man3/* $RPM_BUILD_ROOT/usr/X11R6/man/man3
install include/* $RPM_BUILD_ROOT/usr/X11R6/include/X11/qt

install -s lib/libqimgio.so.*.* $RPM_BUILD_ROOT/usr/X11R6/lib
ln -sf libqimgio.so.0.1 $RPM_BUILD_ROOT/usr/X11R6/lib/libqimgio.so
install extensions/imageio/src/*.h $RPM_BUILD_ROOT/usr/X11R6/include/X11/qt

install lib/libqgl.a $RPM_BUILD_ROOT/usr/X11R6/lib
install extensions/opengl/src/*.h $RPM_BUILD_ROOT/usr/X11R6/include/X11/qt

if [ -f lib/libqxt.a ] ; then
	install lib/libqxt.a $RPM_BUILD_ROOT/usr/X11R6/lib
fi
install extensions/xt/src/*.h $RPM_BUILD_ROOT/usr/X11R6/include/X11/qt

for a in {tutorial,examples}/{Makefile,*/Makefile}; do
	cat $a | sed 's-^SYSCONF_MOC.*-SYSCONF_MOC              = /usr/X11R6/bin/moc-' | \
	sed 's-^SYSCONF_CXXFLAGS_QT     =\$(QTDIR)/include-SYSCONF_CXXFLAGS_QT = /usr/X11R6/include/qt-' | \
	sed 's-^SYSCONF_LFLAGS_QT       = \$(QTDIR)/lib-SYSCONF_LFLAGS_QT = /usr/X11R6/lib-' > $a.
	mv -vf $a. $a
done

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man[13]/* \
	README* LICENSE FAQ ANNOUNCE changes-* doc/*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   -p /sbin/ldconfig extensions
%postun -p /sbin/ldconfig extensions

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.gz README*.gz FAQ.gz
%attr(755,root,root) /usr/X11R6/lib/libqt.so.*.*

%files devel
%defattr(644,root,root,755)
%doc html tutorial examples doc changes-*.gz ANNOUNCE.gz
%attr(755,root,root) /usr/X11R6/bin/*
%attr(755,root,root) /usr/X11R6/lib/lib*.so
/usr/X11R6/lib/lib*.a
/usr/X11R6/man/man[13]/*
/usr/X11R6/include/X11/qt

%files extensions
%attr(755,root,root) /usr/X11R6/lib/libqimgio.so.*.*

%changelog
* Sat Apr 24 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.44-6]
- new qt-opt.patch (added -fno-rtti -fno-exceptions .. it cuts libqt code
  size ~ 1/3 !?!),
- added patch for enabling internal GIF reading,
- recompiles on new rpm.

* Fri Mar  5 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.43-1]
- removed compressing html doc,
- fixed passing $RPM_OPT_FLAGS,
- added "Conflicts: glibc <= 2.0.7" for prevent installing packages
  in proper enviroment,
- now devel subpackage is depends on main and extensions,
- fixed SYSCONF_LFLAGS_QT and SYSCONF_CXXFLAGS_QT in all Makefiles in
  tutorial and examples sources (not use $QTDIR),
- removed man group from man pages.

* Wed Feb 17 1999 Micha³ Kuratczyk <kura@wroclaw.art.pl>
  [1.42-4]
- added gzipping documentation
- removed man group from man pages.

* Fri Feb  5 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [1.42-3]
- separate extensions.

* Tue Jan  7 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- added extensions.

* Mon Dec  9 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.42-2]
- added gzipping man pages,
- recompiled against libstdc++.so.2.9.

* Tue Sep 15 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.40-3]
- added pl translation (based on translation maked by Jacek Konieczny
  <jajcus@zeus.polsl.gliwice.pl>),
- removed PORTING from %doc,
- ANNOUNCE and changes-* moved to devel %doc,
- changed install base directory to /usr/X11R6.

* Mon Aug  3 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.40-2]
- added -q %setup parameter and removed -n parameter,
- package rewrited for using Buildroot,
- added using %%{name} and %%{version} macros in Source,
- "rm -rf $RPM_BUILD_ROOT" moved from %prep to %install,
- spec file rewritten for using Buildroot,
- added %clean section,
- added URL,
- removed compiling tutorial and examples during building (qt.patch),
- fixed dependences for devel by adding "Requires: %%{name} = %%{version}",
- html, tutorial, examples and doc are marked as %doc in devel subpackage,
- header files moved to /usr/include/qt (to be consistent with FSSTND),
- replaced "mkdir -p" with "install -d" in %install,
- added striping binaries,
- /usr/lib/lib*.so moved to devel,
- fiew simplification in %files and %install,
- added using $RPM_OPT_FLAGS during compile,
- /sbin/ldconfig is now -p parameter in %post[un],
- added %defattr and %attr macros in %files (allows building package from
  non-root account).jri.h
