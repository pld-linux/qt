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
BuildPrereq:	libstdc++-devel
BuildPrereq:	XFree86-devel
BuildPrereq:	Mesa-devel
BuildPrereq:	libjpeg-devel
Buildroot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6

%description
Contains the shared library needed to run Qt applications, as well as
the README files for Qt.

%description -l pl
Zawiera bibliotekê Qt wymagan± przez aplikacje, które z niej korzystaj±.

%package devel
Summary:	Include files and documentation needed to compile
Summary(pl):	Pliki nag³ówkowe, przyk³ady i dokumentacja do biblioteki 
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
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

%description extensions
Contains the Qt extension files with library and include files.
Contains extension for Motif/Lesstif, OpenGL, image manipulation.

%description -l pl extensions
Pakiet zawiera zestaw rozsze¿eñ dla biblioteki Qt. Biblioteki oraz pliki
nag³ówkowe dla nastêpuj±cych pakietów: Motif/Lestif, OpenGL, Netscape oraz
operacji na obrazach.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
QTDIR=`/bin/pwd`; export QTDIR
make linux-g++-shared

LD_LIBRARY_PATH=%{_libdir} make

(cd extensions/imageio/src; LD_LIBRARY_PATH=%{_libdir} make)
(cd extensions/opengl/src; LD_LIBRARY_PATH=%{_libdir} make)
(cd extensions/xt/src; LD_LIBRARY_PATH=%{_libdir} \
 make INCPATH="-I%{_includedir} -I../../../include")

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/X11/qt,%{_libdir},%{_mandir}/man{1,3}} \
	$RPM_BUILD_ROOT/usr/src/examples/%{name}

install -s bin/moc $RPM_BUILD_ROOT%{_bindir}/moc
install -s lib/libqt.so.*.* $RPM_BUILD_ROOT%{_libdir}
ln -sf libqt.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libqt.so
install man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
install man/man3/* $RPM_BUILD_ROOT%{_mandir}/man3
install include/* $RPM_BUILD_ROOT%{_includedir}/X11/qt

install -s lib/libqimgio.so.*.* $RPM_BUILD_ROOT%{_libdir}
ln -sf libqimgio.so.0.1 $RPM_BUILD_ROOT%{_libdir}/libqimgio.so
install extensions/imageio/src/*.h $RPM_BUILD_ROOT%{_includedir}/X11/qt

install lib/libqgl.a $RPM_BUILD_ROOT%{_libdir}
install extensions/opengl/src/*.h $RPM_BUILD_ROOT%{_includedir}/X11/qt

if [ -f lib/libqxt.a ] ; then
	install lib/libqxt.a $RPM_BUILD_ROOT%{_libdir}
fi
install extensions/xt/src/*.h $RPM_BUILD_ROOT%{_includedir}/X11/qt

for a in {tutorial,examples}/{Makefile,*/Makefile}; do
	cat $a | sed 's-^SYSCONF_MOC.*-SYSCONF_MOC              = %{_bindir}/moc-' | \
	sed 's-^SYSCONF_CXXFLAGS_QT     = \$(QTDIR)/include-SYSCONF_CXXFLAGS_QT = %{_includedir}/qt-' | \
	sed 's-^SYSCONF_LFLAGS_QT       = \$(QTDIR)/lib-SYSCONF_LFLAGS_QT = %{_libdir}-' > $a.
	mv -vf $a. $a
done

cp -dpr tutorial examples $RPM_BUILD_ROOT/usr/src/examples/%{name}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
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
%attr(755,root,root) %{_libdir}/libqt.so.*.*

%files devel
%defattr(644,root,root,755)
%doc html doc changes-*.gz ANNOUNCE.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_mandir}/man[13]/*
%{_includedir}/X11/qt
/usr/src/examples/%{name}

%files extensions
%defattr(755,root,root,755)
%{_libdir}/libqimgio.so.*.*

%changelog
* Mon May 24 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.44-6]
- spec writtren by me, modified by Wojciech "Sas" Ciêciwa
  <cieciwa@alpha.zarz.agh.edu.pl> and Micha³ Kuratczyk
  <kura@wroclaw.art.pl>.
- pl translation by Jacek Konieczny <jajcus@zeus.polsl.gliwice.pl>.
