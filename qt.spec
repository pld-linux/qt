Summary:	The Qt2 GUI application framework
Summary(pl):	Biblioteka Qt2 do tworzenia GUI
Name:		qt
%define		libqutil_version 1.0.0
Version:	2.2.1
Release:	1
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.troll.no/qt/source/%{name}-x11-%{version}.tar.gz
Patch0:		%{name}-tools.patch
BuildRequires:	libungif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	qt-extensions

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Contains the shared library needed to run Qt applications, as well as
the README files for Qt.

%description -l pl
Zawiera bibliotek� Qt wymagan� przez aplikacje, kt�re z niej
korzystaj�.

%package devel
Summary:	Include files and documentation needed to compile
Summary(pl):	Pliki nag��wkowe, przyk�ady i dokumentacja do biblioteki 
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
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
korzystaj�cych z biblioteki Qt, jak pliki nag��wkowe, meta kompiler
(moc), dokumentacj�. Zobacz http://www.troll.no/ aby dowiedzie� si�
wi�cej o Qt. Dokumentacj� do biblioteki znajdziesz tak�e pod:
/usr/share/doc/%{name}-devel-%{version}/index.html

%package examples
Summary:	Qt tutorial/examples
Summary(pl):	Qt przyk�ady
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description examples
Qt tutorial/examples.

%description -l pl examples
Qt przyk�ady.

%prep 
%setup -q
%patch0 -p1

%build
QTDIR=`/bin/pwd`; export QTDIR
./configure \
	-shared \
	-sm \
	-system-zlib \
	-gif \
	-thread \
	-system-zlib \
	-system-jpeg \
	-system-libpng <<_EOF_
yes
_EOF_

LD_LIBRARY_PATH=%{_libdir}
SYSCONF_CFLAGS="-pipe -DNO_DEBUG $RPM_OPT_FLAGS"
SYSCONF_CXXFLAGS="-pipe -DNO_DEBUG $RPM_OPT_FLAGS"
export LD_LIBRARY_PATH SYSCONF_CFLAGS SYSCONF_CXXFLAGS

%{__make} SYSCONF_CFLAGS="$RPM_OPT_FLAGS" SYSCONF_CXXFLAGS="$RPM_OPT_FLAGS" \
	symlinks  src-moc src-mt sub-src sub-tools

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir},%{_mandir}/man3} \
	$RPM_BUILD_ROOT/usr/src/examples/%{name} \
	$RPM_BUILD_ROOT%{_datadir}/tutorial/%{name} \

install bin/* $RPM_BUILD_ROOT%{_bindir}/
install tools/msg2qm/msg2qm $RPM_BUILD_ROOT%{_bindir}/
install tools/mergetr/mergetr $RPM_BUILD_ROOT%{_bindir}/

install -s lib/libqt.so.%{version} $RPM_BUILD_ROOT%{_libdir}
ln -sf libqt.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libqt.so

install -s lib/libqutil.so.%{libqutil_version} $RPM_BUILD_ROOT%{_libdir}
ln -sf libqutil.so.%{libqutil_version} $RPM_BUILD_ROOT%{_libdir}/libqutil.so

install -s lib/libqt-mt.so.%{version} $RPM_BUILD_ROOT%{_libdir}
ln -sf libqt-mt.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libqt-mt.so

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
%attr(755,root,root) %{_libdir}/libqt-mt.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/libqt.so
%{_libdir}/libqutil.so
%{_libdir}/libqt-mt.so
%{_includedir}/*.h
%{_mandir}/man*/*

%files examples
%defattr(644,root,root,755)
/usr/src/examples/%{name}
%{_datadir}/tutorial/%{name}
