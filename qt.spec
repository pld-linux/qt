Summary:	The Qt2 GUI application framework
Summary(pl):	Biblioteka Qt2 do tworzenia GUI
Name:		qt
Version:	2.1.0
Release:	1
Copyright:	QPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://ftp.troll.no/qt/source/%{name}-x11-%{version}.tar.gz
BuildRequires:	libungif-devel
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	Mesa-devel
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel
BuildRequires:	lesstif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Contains the shared library needed to run Qt applications, as well as
the README files for Qt.

%description -l pl
Zawiera bibliotekê Qt wymagan± przez aplikacje, które z niej korzystaj±.

%package devel
Summary:        Include files and documentation needed to compile
Summary(pl):    Pliki nag³ówkowe, przyk³ady i dokumentacja do biblioteki 
Group:          X11/Development/Libraries
Group(pl):      X11/Programowanie/Biblioteki
Requires:       %{name} = %{version}

%description devel
Contains the files necessary to develop applications using Qt: header
files, the Qt meta object compiler, man pages, HTML documentation and
example programs. See http://www.troll.no/ for more information about
Qt, or file:/usr/share/doc/%{name}-devel-%{version}/index.html 
for Qt documentation in HTML.

%description -l pl devel
Pakiet tem zawiera pliki potrzebne do tworzenia i kompilacji aplikacji
korzystaj±cych z biblioteki Qt, jak pliki nag³ówkowe, meta kompiler (moc),
dokumentacjê. Zobacz http://www.troll.no/ aby dowiedzieæ siê wiêcej o Qt.
Dokumentacjê do biblioteki znajdziesz tak¿e pod:
/usr/share/doc/%{name}-devel-%{version}/index.html  

%package extensions
Summary:        Qt extensions, library
Summary(pl):    Qt extensions, rozrze¿enia dla QT biblioteki 
Group:          X11/Libraries
Group(pl):      X11/Biblioteki
Requires:       %{name} = %{version}

%description extensions
Contains the Qt extension files with library.
Contains extension for Motif/Lesstif, OpenGL, image manipulation.

%description -l pl extensions
Pakiet zawiera zestaw rozsze¿eñ dla biblioteki Qt. Biblioteki dla 
nastêpuj±cych pakietów: Motif/Lestif, OpenGL, Netscape oraz
operacji na obrazach.

%prep 
%setup -q

%build
QTDIR=`/bin/pwd`; export QTDIR
./configure \
	-shared \
	-sm \
	-system-zlib \
	-gif \
	-system-libpng

LD_LIBRARY_PATH=%{_libdir} ;	export LD_LIBRARY_PATH
SYSCONF_CFLAGS="-pipe -DNO_DEBUG $RPM_OPT_FLAGS" ;	export SYSCONF_CFLAGS
SYSCONF_CXXFLAGS="-pipe -DNO_DEBUG $RPM_OPT_FLAGS" ;	export SYSCONF_CXXFLAGS
make SYCONF_CFLAGS="$RPM_OPT_FLAGS" SYSCONF_CXXFLAGS="$RPM_OPT_FLAGS" moc
make SYSCONF_CXXFLAGS="$RPM_OPT_FLAGS" SYCONF_CFLAGS="$RPM_OPT_FLAGS" src
make util

echo " Compiling Extensions ..."
(cd extensions/opengl/src;LD_LIBRARY_PATH=%{_libdir};make)
(cd extensions/xt/src;LD_LIBRARY_PATH=%{_libdir};make \
	INCPATH="-I%{_includepatch} -I../../../include")

# tutorial
#(cd tutorial;LD_LIBRARY_PATH=%{_libdir};make)

#examples
# remover due to many errors in sources
#(cd examples;LD_LIBRARY_PATH=%{_libdir};make)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir},%{_mandir}/man3}
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}
install -d $RPM_BUILD_ROOT/usr/share/tutorial/%{name}

install bin/* $RPM_BUILD_ROOT%{_bindir}/

install -s lib/libqt.so.%{version} $RPM_BUILD_ROOT%{_libdir}
ln -sf libqt.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libqt.so

install lib/lib*.a $RPM_BUILD_ROOT%{_libdir}

# empty symlinks
rm -f include/qt_mac.h include/qt_windows.h
install include/* $RPM_BUILD_ROOT/%{_includedir}

# Extensions
install extensions/opengl/src/*.h $RPM_BUILD_ROOT%{_includedir}
install extensions/xt/src/*.h $RPM_BUILD_ROOT%{_includedir}

strip --strip-unneeded $RPM_BUILD_ROOT/%{_bindir}/* || :
strip --strip-unneeded $RPM_BUILD_ROOT/%{_libdir}/*.so*

gzip -9nf LICENSE.QPL doc/man/man*/*

install doc/man/man3/* $RPM_BUILD_ROOT%{_mandir}/man3

for a in {tutorial,examples}/{Makefile,*/Makefile}; do
        cat $a | sed 's-^SYSCONF_MOC.*-SYSCONF_MOC = %{_bindir}/moc -' | \
	sed 's-^SYSCONF_CXXFLAGS_QT     = \$(QTDIR)/include-SYSCONF_CXXFLAGS_QT = %{_includedir}-' | \
	sed 's-^SYSCONF_LFLAGS_QT       = \$(QTDIR)/lib-SYSCONF_LFLAGS_QT = %{_libdir}-' > $a.
        mv -vf $a. $a
done

cp -dpr examples $RPM_BUILD_ROOT/usr/src/examples/%{name}
cp -dpr tutorial $RPM_BUILD_ROOT/usr/share/tutorial/%{name}
				
%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc LICENSE.QPL.gz
%attr(755,root,root) %{_libdir}/libqt.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/libqt.so
%{_includedir}/*.h
%{_mandir}/man*/*
/usr/src/examples/%{name}
/usr/share/tutorial/%{name}

%files extensions
%defattr(644,root,root,755)
%{_libdir}/libqgl.a
%{_libdir}/libqxt.a
