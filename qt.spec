Summary:	The Qt3 GUI application framework
Summary(pl):	Biblioteka Qt3 do tworzenia GUI
Name:		qt
%define		libqui_version 1.0.0
%define		libeditor_version 1.0.0
Version:	3.0.0
Release:	0.1
Epoch:		1
License:	GPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.troll.no/qt/source/%{name}-x11-free-%{version}.tar.gz
Patch0:		%{name}-tools.patch
Patch1:		%{name}-huge_val.patch
Patch2:		%{name}-charset.patch
Patch3:		http://www.research.att.com/~leonb/objprelink/qt-configs.patch
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel >= 4.0.2
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel >= 1.0.0
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libungif-devel
BuildRequires:	zlib-devel
BuildRequires:	mysql-devel
BuildRequires:	unixODBC-devel
BuildRequires:	postgresql-devel
BuildRequires:	freetype-devel
#%ifnarch alpha
#BuildRequires:	objprelink
#%endif
Requires:	OpenGL
Requires:	XFree86-libs >= 4.0.2
Requires:	libmng
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	qt-extensions

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_includedir	%{_prefix}/include/qt
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
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	XFree86-devel
Requires:	libstdc++-devel

%description devel
Contains the files necessary to develop applications using Qt: header
files, the Qt meta object compiler, man pages, HTML documentation and
example programs. See http://www.troll.no/ for more information about
Qt, or file:/usr/share/doc/%{name}-devel-%{version}/index.html for Qt
documentation in HTML.

%description devel -l pl
Pakiet tem zawiera pliki potrzebne do tworzenia i kompilacji aplikacji
korzystaj±cych z biblioteki Qt, jak pliki nag³ówkowe, meta kompiler
(moc), dokumentacjê. Zobacz http://www.troll.no/ aby dowiedzieæ siê
wiêcej o Qt. Dokumentacjê do biblioteki znajdziesz tak¿e pod:
/usr/share/doc/%{name}-devel-%{version}/index.html

%package static
Summary:	Qt static libraries
Summary(pl):	Biblioteki statyczne Qt.
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static QT libraries.

%description static -l pl
Statyczne biblioteki Qt.

%package examples
Summary:	Qt tutorial/examples
Summary(pl):	Qt æwiczenia/przyk³ady
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description examples
Qt tutorial/examples.

%description examples -l pl
Qt æwiczenia/przyk³ady.

%package plugins-mysql
Summary:	Qt MySQL plugin
Summary(pl):	Plugin MySQL do Qt
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description plugins-mysql
Qt MySQL plugin.

%description plugins-mysql -l pl
Plugin MySQL do Qt.

%package plugins-psql
Summary:	Qt PostgreSQL plugin
Summary(pl):	Plugin PostgreSQL do Qt
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description plugins-psql
Qt PostgreSQL plugin.

%description plugins-psql -l pl
Plugin PostgreSQL do Qt.

%package plugins-odbc
Summary:	Qt ODBC plugin
Summary(pl):	Plugin ODBC do Qt
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description plugins-odbc
Qt ODBC plugin.

%description plugins-odbc -l pl
Plugin ODBC do Qt.

%prep
%setup -q -n %{name}-x11-free-%{version}
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1
#%ifnarch alpha
#%patch3 -p0
#%endif

%build
QTDIR=`/bin/pwd`; export QTDIR
LD_LIBRARY_PATH=%{_libdir}
SYSCONF_CFLAGS="-pipe -DNO_DEBUG %{rpmcflags}"
SYSCONF_CXXFLAGS="-pipe -DNO_DEBUG %{rpmcflags}"
export LD_LIBRARY_PATH SYSCONF_CFLAGS SYSCONF_CXXFLAGS

DEFAULTOPT="-prefix %{_prefix} -bindir %{_bindir} -libdir %{_libdir} -docdir %{_docdir} \
            -headerdir include/qt -release -qt-gif -system-zlib -no-g++-exceptions \
	    -stl -remote -system-libpng -system-libjpeg -system-libmng -sm -xinerama \
	    -xrender -xft -xkb"

./configure \
	$DEFAULTOPT \
	-shared <<_EOF_
yes
_EOF_

%{__make} symlinks src-qmake src-moc sub-src sub-tools \
	SYSCONF_CFLAGS="%{rpmcflags}" \
	SYSCONF_CXXFLAGS="%{rpmcflags}"

# Build extra tools and plugins
(cd plugins/src/sqldrivers/mysql && $QTDIR/bin/qmake -o Makefile \
	"INCLUDEPATH+=/usr/include/mysql" "LIBS+=-L/usr/lib -lmysqlclient" mysql.pro)
(cd plugins/src/sqldrivers/odbc && $QTDIR/bin/qmake \
	"INCLUDEPATH+=/usr/include" "LIBS+=-L/usr/lib -lodbc")            
(cd plugins/src/sqldrivers/psql && $QTDIR/bin/qmake \
	"INCLUDEPATH+=/usr/include/postgresql" "LIBS+=-L/usr/lib -lpq")

for dir in tools/mergetr tools/msg2qm tools/makeqpf tools/qembed tools/qvfb \
           extensions/xt/src plugins/src/accessible plugins/src/codecs \
	   plugins/src/imageformats plugins/src/styles \
	   plugins/src/sqldrivers/mysql plugins/src/sqldrivers/odbc \
	   plugins/src/sqldrivers/psql ; do
  %{__make} -C $dir \
	SYSCONF_CFLAGS="%{rpmcflags}" \
	SYSCONF_CXXFLAGS="%{rpmcflags}"
done

./configure \
	$DEFAULTOPT \
	-thread <<_EOF_
yes
_EOF_

%{__make} symlinks src-qmake src-moc sub-src \
	SYSCONF_CFLAGS="%{rpmcflags}" \
	SYSCONF_CXXFLAGS="%{rpmcflags}"

./configure \
	$DEFAULTOPT \
	-static <<_EOF_
yes
_EOF_

%{__make} symlinks src-qmake src-moc sub-src \
	SYSCONF_CFLAGS="%{rpmcflags}" \
	SYSCONF_CXXFLAGS="%{rpmcflags}"
	
%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_mandir}/man{1,3}} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name} \
	$RPM_BUILD_ROOT%{_datadir}/tutorial/%{name} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/{sqldrivers,imageformats,designer}

rm -f   bin/*.bat
install bin/*			$RPM_BUILD_ROOT%{_bindir}/
install tools/msg2qm/msg2qm	$RPM_BUILD_ROOT%{_bindir}/
install tools/mergetr/mergetr	$RPM_BUILD_ROOT%{_bindir}/
install tools/makeqpf/makeqpf	$RPM_BUILD_ROOT%{_bindir}/
install tools/qembed/qembed	$RPM_BUILD_ROOT%{_bindir}/
install tools/qvfb/qvfb		$RPM_BUILD_ROOT%{_bindir}/
install qmake/qmake		$RPM_BUILD_ROOT%{_bindir}/

install plugins/sqldrivers/*.so		$RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/sqldrivers
install plugins/imageformats/*.so	$RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/imageformats
install plugins/designer/*.so		$RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/designer
#install plugins/styles/*.so		$RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/styles

install lib/libqt.so.%{version}	$RPM_BUILD_ROOT%{_libdir}
ln -s -f libqt.so.%{version}	$RPM_BUILD_ROOT%{_libdir}/libqt.so

install lib/libqui.so.%{libqui_version}	$RPM_BUILD_ROOT%{_libdir}
ln -s -f libqui.so.%{libqui_version}	$RPM_BUILD_ROOT%{_libdir}/libqui.so

install lib/libqt-mt.so.%{version}	$RPM_BUILD_ROOT%{_libdir}
ln -s -f libqt-mt.so.%{version}		$RPM_BUILD_ROOT%{_libdir}/libqt-mt.so

install lib/libeditor.so.%{libeditor_version}	$RPM_BUILD_ROOT%{_libdir}
ln -s -f libeditor.so.%{libeditor_version}	$RPM_BUILD_ROOT%{_libdir}/libeditor.so

install lib/*.a		$RPM_BUILD_ROOT%{_libdir}

cp -pRL include/*	$RPM_BUILD_ROOT%{_includedir}

install doc/man/man1/*	$RPM_BUILD_ROOT%{_mandir}/man1
install doc/man/man3/*	$RPM_BUILD_ROOT%{_mandir}/man3

for a in {tutorial,examples}/{Makefile,*/Makefile}; do
	cat $a | sed 's-^SYSCONF_MOC.*-SYSCONF_MOC = %{_bindir}/moc -' | \
	sed 's-^SYSCONF_CXXFLAGS_QT	= \$(QTDIR)/include-SYSCONF_CXXFLAGS_QT = %{_includedir}-' | \
	sed 's-^SYSCONF_LFLAGS_QT	= \$(QTDIR)/lib-SYSCONF_LFLAGS_QT = %{_libdir}-' > $a.
	mv -f $a. $a
done

cp -dpr examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}
cp -dpr tutorial $RPM_BUILD_ROOT%{_datadir}/tutorial/%{name}
				
gzip -9nf LICENSE.QPL

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.QPL.gz
%attr(755,root,root) %{_libdir}/libqt.so.*.*
%attr(755,root,root) %{_libdir}/libqui.so.*.*
%attr(755,root,root) %{_libdir}/libeditor.so.*.*
%attr(755,root,root) %{_libdir}/libqt-mt.so.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plguins
%dir %{_libdir}/%{name}/plguins/imageformats
%dir %{_libdir}/%{name}/plguins/styles
%dir %{_libdir}/%{name}/plguins/sqldrivers
%attr(755,root,root) %{_libdir}/%{name}/plugins/imageformats/*.so
#%attr(755,root,root) %{_libdir}/%{name}/plugins/styles/*.so

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/libqt.so
%{_libdir}/libqui.so
%{_libdir}/libeditor.so
%{_libdir}/libqt-mt.so
%{_includedir}
%{_mandir}/man?/*
%dir %{_libdir}/%{name}/plguins/designer
%attr(755,root,root) %{_libdir}/%{name}/plugins/designer/*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files examples
%defattr(644,root,root,755)
/usr/src/examples/%{name}
%{_datadir}/tutorial/%{name}

%files plugins-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/sqldrivers/lib*mysql.so

%files plugins-psql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/sqldrivers/lib*osql.so

%files plugins-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/sqldrivers/lib*odbc.so
