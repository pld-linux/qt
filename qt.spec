%define		_snapshot	ss20020126
Summary:	The Qt3 GUI application framework
Summary(pl):	Biblioteka Qt3 do tworzenia GUI
Name:		qt
%define		libqui_version 1.0.0
%define		libeditor_version 1.0.0
Version:	3.0.2
Release:	0.0.%{_snapshot}.1
Epoch:		1
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.troll.no/qt/source/%{name}-x11-free-%{version}%{_snapshot}.tar.gz
Patch0:		%{name}-tools.patch
Patch1:		%{name}-huge_val.patch
Patch2:		%{name}-charset.patch
# prelinking
Patch3:		%{name}-qmake.patch
Patch4:		%{name}-no_bashisms.patch
Patch5:		%{name}-parse_error.patch
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel >= 4.0.2
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel >= 1.0.0
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libungif-devel
BuildRequires:	mysql-devel
BuildRequires:	postgresql-backend-devel
BuildRequires:	postgresql-devel
BuildRequires:	unixODBC-devel
BuildRequires:	zlib-devel
%ifnarch alpha
BuildRequires:	objprelink
%endif
Requires:	OpenGL
Requires:	XFree86-libs >= 4.0.2
Requires:	libmng
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	qt-extensions

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_includedir	%{_prefix}/include/qt
%define		_mandir		%{_prefix}/man

%description
This package contains the shared library needed to run Qt
applications, as well as the README files for Qt.

%description -l pl
Pakiet ten zawiera bibliotek� niezb�dn� do uruchamiania aplikacji Qt,
jak r�wnie� pliki README z Qt.

%package devel
Summary:	Include files and documentation needed to compile
Summary(pl):	Pliki nag��wkowe, przyk�ady i dokumentacja do biblioteki
Group:		X11/Development/Libraries
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
korzystaj�cych z biblioteki Qt, jak pliki nag��wkowe, meta kompiler
(moc), dokumentacj�. Zobacz http://www.troll.no/ aby dowiedzie� si�
wi�cej o Qt. Dokumentacj� do biblioteki znajdziesz tak�e pod:
/usr/share/doc/%{name}-devel-%{version}/index.html

%package static
Summary:	Qt static libraries
Summary(pl):	Biblioteki statyczne Qt.
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static QT libraries.

%description static -l pl
Statyczne biblioteki Qt.

%package examples
Summary:	Qt tutorial/examples
Summary(pl):	Qt �wiczenia/przyk�ady
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description examples
Qt tutorial/examples.

%description examples -l pl
Qt �wiczenia/przyk�ady.

%package plugins-mysql
Summary:	Qt MySQL plugin
Summary(pl):	Wtyczka MySQL do Qt
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description plugins-mysql
Qt MySQL plugin.

%description plugins-mysql -l pl
Wtyczka MySQL do Qt.

%package plugins-psql
Summary:	Qt PostgreSQL plugin
Summary(pl):	Wtyczka PostgreSQL do Qt
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description plugins-psql
Qt PostgreSQL plugin.

%description plugins-psql -l pl
Wtyczka PostgreSQL do Qt.

%package plugins-odbc
Summary:	Qt ODBC plugin
Summary(pl):	Wtyczka ODBC do Qt
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description plugins-odbc
Qt ODBC plugin.

%description plugins-odbc -l pl
Wtyczka ODBC do Qt.

%prep
%setup -q -n %{name}-x11-free-%{version}
%patch0 -p1
#%patch1 -p1
#%patch2 -p1
%ifnarch alpha
%patch3 -p1
%endif
%patch4 -p1
%patch5 -p1

# There is no file pointed by this sym-link and there is cp -L in %%install
rm include/qt_windows.h

%build
QTDIR=`/bin/pwd`; export QTDIR
LD_LIBRARY_PATH=%{_libdir} ; export LD_LIBRARY_PATH

# change QMAKE_CFLAGS_RELEASE
sed 's/-O2/%{rpmcflags}/' mkspecs/linux-g++/qmake.conf > qmk.tmp
mv -f qmk.tmp mkspecs/linux-g++/qmake.conf

DEFAULTOPT="-prefix %{_prefix} -bindir %{_bindir} -libdir %{_libdir} -docdir %{_docdir} \
            -headerdir include/qt -release -qt-gif -system-zlib -no-g++-exceptions \
	    -stl -remote -system-libpng -system-libjpeg -system-libmng -sm -xinerama \
	    -xrender -xft -xkb"

./configure \
	$DEFAULTOPT \
	-shared <<_EOF_
yes
_EOF_

%{__make} symlinks src-qmake src-moc sub-src sub-tools

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
  %{__make} -C $dir
done

./configure \
	$DEFAULTOPT \
	-thread <<_EOF_
yes
_EOF_

%{__make} symlinks src-qmake src-moc sub-src

./configure \
	$DEFAULTOPT \
	-static <<_EOF_
yes
_EOF_

%{__make} symlinks src-qmake src-moc sub-src

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_mandir}/man{1,3}} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name} \
	$RPM_BUILD_ROOT%{_datadir}/tutorial/%{name} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/{sqldrivers,imageformats,designer,styles}

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
ln -sf	libqt.so.%{version}	$RPM_BUILD_ROOT%{_libdir}/libqt.so

install lib/libqui.so.%{libqui_version}	$RPM_BUILD_ROOT%{_libdir}
ln -sf	libqui.so.%{libqui_version}	$RPM_BUILD_ROOT%{_libdir}/libqui.so

install lib/libqt-mt.so.%{version}	$RPM_BUILD_ROOT%{_libdir}
ln -sf	libqt-mt.so.%{version}		$RPM_BUILD_ROOT%{_libdir}/libqt-mt.so

install lib/libeditor.so.%{libeditor_version}	$RPM_BUILD_ROOT%{_libdir}
ln -sf	libeditor.so.%{libeditor_version}	$RPM_BUILD_ROOT%{_libdir}/libeditor.so

install lib/*.a		$RPM_BUILD_ROOT%{_libdir}

cp -pRL include/*	$RPM_BUILD_ROOT%{_includedir}

install doc/man/man1/*	$RPM_BUILD_ROOT%{_mandir}/man1
install doc/man/man3/*	$RPM_BUILD_ROOT%{_mandir}/man3

# $(QTDIR)/{bin,lib,include} is used - change to /usr/X11R6/{bin,lib,include}
# also remove -I referring to qt build directory
for a in {tutorial,examples}/{Makefile,*/Makefile}; do
	sed 's@\$(QTDIR)@%{_prefix}@g;s@-I[^ ]linux-g++@@g' $a > $a.
	mv -f $a. $a
done

cp -dpr examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}
cp -dpr tutorial $RPM_BUILD_ROOT%{_datadir}/tutorial/%{name}

gzip -9nf LICENSE.QPL

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.QPL.gz
%attr(755,root,root) %{_libdir}/libqt.so.*.*
%attr(755,root,root) %{_libdir}/libqui.so.*.*
%attr(755,root,root) %{_libdir}/libeditor.so.*.*
%attr(755,root,root) %{_libdir}/libqt-mt.so.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/imageformats
%dir %{_libdir}/%{name}/plugins/styles
%dir %{_libdir}/%{name}/plugins/sqldrivers
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
%dir %{_libdir}/%{name}/plugins/designer
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
%attr(755,root,root) %{_libdir}/%{name}/plugins/sqldrivers/lib*psql.so

%files plugins-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/sqldrivers/lib*odbc.so
