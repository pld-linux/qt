Summary:	The Qt2 GUI application framework
Summary(pl):	Biblioteka Qt2 do tworzenia GUI
Name:		qt
%define		alt_version 2.2.0-beta2
%define		libqt_version 2.2.0
%define		libqutil_version 1.0.0
Version:	2.2.0_beta2
Release:	1
License:	QPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.troll.no/qt/source/%{name}-x11-%{alt_version}.tar.gz
BuildRequires:	libungif-devel
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Contains the shared library needed to run Qt applications, as well as
the README files for Qt.

%description -l pl
Zawiera bibliotekê Qt wymagan± przez aplikacje, które z niej
korzystaj±.

%package devel
Summary:	Include files and documentation needed to compile
Summary(pl):	Pliki nag³ówkowe, przyk³ady i dokumentacja do biblioteki 
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Contains the files necessary to develop applications using Qt: header
files, the Qt meta object compiler, man pages, HTML documentation and
example programs. See http://www.troll.no/ for more information about
Qt, or file:/usr/share/doc/%{name}-devel-%{version}/index.html for Qt
documentation in HTML.

%description -l pl devel
Pakiet tem zawiera pliki potrzebne do tworzenia i kompilacji aplikacji
korzystaj±cych z biblioteki Qt, jak pliki nag³ówkowe, meta kompiler
(moc), dokumentacjê. Zobacz http://www.troll.no/ aby dowiedzieæ siê
wiêcej o Qt. Dokumentacjê do biblioteki znajdziesz tak¿e pod:
/usr/share/doc/%{name}-devel-%{version}/index.html

#%package extensions
#Summary:	Qt extensions, library
#Summary(pl):	Qt extensions, rozrze¿enia dla QT biblioteki 
#Group:		X11/Libraries
#Group(pl):	X11/Biblioteki
#Requires:	%{name} = %{version}
#Obsoletes:	qt-GL
#Obsoletes:	qt-Xt

#%description extensions
#Contains the Qt extension files with library. Contains extension for
#Motif/Lesstif, OpenGL, image manipulation.

#%description -l pl extensions
#Pakiet zawiera zestaw rozsze¿eñ dla biblioteki Qt. Biblioteki dla
#nastêpuj±cych pakietów: Motif/Lestif, OpenGL, Netscape oraz operacji
#na obrazach.

%package examples
Summary:	Qt tutorial/examples
Summary(pl):	Qt przyk³ady
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description examples
Qt tutorial/examples

%description -l pl examples
Qt przyk³ady

%prep 
%setup -q -n %{name}-%{alt_version}

%build
QTDIR=`/bin/pwd`; export QTDIR
./configure \
	-shared \
	-sm \
	-system-zlib \
	-gif \
	-system-libpng <<_EOF_
yes
_EOF_

LD_LIBRARY_PATH=%{_libdir} ;				export LD_LIBRARY_PATH
SYSCONF_CFLAGS="-pipe -DNO_DEBUG $RPM_OPT_FLAGS" ;	export SYSCONF_CFLAGS
SYSCONF_CXXFLAGS="-pipe -DNO_DEBUG $RPM_OPT_FLAGS" ;	export SYSCONF_CXXFLAGS
%{__make} SYSCONF_CFLAGS="$RPM_OPT_FLAGS" SYSCONF_CXXFLAGS="$RPM_OPT_FLAGS" \
	symlinks  moc src-mt src tools

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir},%{_mandir}/man3}
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}
install -d $RPM_BUILD_ROOT%{_datadir}/tutorial/%{name}

install bin/* $RPM_BUILD_ROOT%{_bindir}/

install -s lib/libqt.so.%{libqt_version} $RPM_BUILD_ROOT%{_libdir}
ln -sf libqt.so.%{libqt_version} $RPM_BUILD_ROOT%{_libdir}/libqt.so

install -s lib/libqutil.so.%{libqutil_version} $RPM_BUILD_ROOT%{_libdir}
ln -sf libqutil.so.%{libqutil_version} $RPM_BUILD_ROOT%{_libdir}/libqutil.so

# empty symlinks
rm -f include/qt_mac.h include/qt_windows.h include/jri.h \
	include/jritypes.h include/npapi.h include/npupp.h
install include/* $RPM_BUILD_ROOT/%{_includedir}

strip --strip-unneeded $RPM_BUILD_ROOT/%{_bindir}/* || :
strip --strip-unneeded $RPM_BUILD_ROOT/%{_libdir}/*.so*

gzip -9nf LICENSE.QPL doc/man/man*/*

install doc/man/man3/* $RPM_BUILD_ROOT%{_mandir}/man3

for a in {tutorial,examples}/{Makefile,*/Makefile}; do
        cat $a | sed 's-^SYSCONF_MOC.*-SYSCONF_MOC = %{_bindir}/moc -' | \
	sed 's-^SYSCONF_CXXFLAGS_QT     = \$(QTDIR)/include-SYSCONF_CXXFLAGS_QT = %{_includedir}-' | \
	sed 's-^SYSCONF_LFLAGS_QT       = \$(QTDIR)/lib-SYSCONF_LFLAGS_QT = %{_libdir}-' > $a.
        mv -f $a. $a
done

cp -dpr examples $RPM_BUILD_ROOT/usr/src/examples/%{name}
cp -dpr tutorial $RPM_BUILD_ROOT%{_datadir}/tutorial/%{name}
				
%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.QPL.gz
%attr(755,root,root) %{_libdir}/libqt.so.*.*
%attr(755,root,root) %{_libdir}/libqutil.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/libqt.so
%{_libdir}/libqutil.so
%{_includedir}/*.h
%{_mandir}/man*/*

%files examples
%defattr(644,root,root,755)
/usr/src/examples/%{name}
%{_datadir}/tutorial/%{name}

#%files extensions
#%defattr(644,root,root,755)
#%{_libdir}/libqxt.a
