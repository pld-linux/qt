#
# Conditional build:
# _without_prelink	- without objprelink (problems with new binutils?)
#
Summary:	The Qt3 GUI application framework
Summary(pl):	Biblioteka Qt3 do tworzenia GUI
Name:		qt
Version:	3.0.4
Release:	0.9.2
Epoch:		1
License:	GPL / QPL
Group:		X11/Libraries
Source0:	ftp://ftp.trolltech.com/qt/source/%{name}-x11-free-%{version}.tar.bz2
Patch0:		%{name}-tools.patch
# prelinking
Patch1:		%{name}-qmake.patch
Patch2:		%{name}-parse_error.patch
Patch3:		%{name}-postgresql_7_2.patch
Patch4:		%{name}-mysql_includes.patch
Patch5:		%{name}-FHS.patch
Patch6:		%{name}-configure.patch
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
# Requires by ./configure.
BuildRequires:	sed
BuildRequires:	perl
BuildRequires:	findutils
BuildRequires:	unixODBC-devel
BuildRequires:	zlib-devel
%ifarch %{ix86} ppc
%{!?_without_prelink:BuildRequires:	objprelink}
%endif
Requires:	OpenGL
Requires:	XFree86-libs >= 4.0.2
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
Pakiet ten zawiera bibliotekê niezbêdn± do uruchamiania aplikacji Qt,
jak równie¿ pliki README z Qt.

%package devel
Summary:	Include files and documentation needed to compile
Summary(pl):	Pliki nag³ówkowe, przyk³ady i dokumentacja do biblioteki
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
korzystaj±cych z biblioteki Qt, jak pliki nag³ówkowe, meta kompiler
(moc), dokumentacjê. Zobacz http://www.troll.no/ aby dowiedzieæ siê
wiêcej o Qt. Dokumentacjê do biblioteki znajdziesz tak¿e pod:
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
Summary(pl):	Æwiczenia i przyk³ady do Qt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description examples
Qt tutorial/examples.

%description examples -l pl
Æwiczenia/przyk³ady do Qt.

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
%ifnarch %{ix86} ppc
%{!?_without_prelink:%patch1 -p1}
%endif
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

# There is no file pointed by this sym-link and there is cp -L in %%install
rm -f include/qt_windows.h

%build
QTDIR=`/bin/pwd`; export QTDIR
LD_LIBRARY_PATH="$QTDIR/lib" ; export LD_LIBRARY_PATH
PATH="$QTDIR/bin:$PATH"
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
	PNGCFLAGS=" `pkg-config libpng12 --cflags`"
fi

# change QMAKE_CFLAGS_RELEASE
perl -pi -e "s|-O2|%{rpmcflags}${PNGCFLAGS}|" mkspecs/linux-g++/qmake.conf

# Fix examples (second part in install section).
find examples -name '*.pro' -exec \
	perl -pi -e 's|(DEPENDPATH=)../../include|$1%{_includedir}|' {} \;

DEFAULTOPT="-prefix %{_prefix} -bindir %{_bindir} -libdir %{_libdir} \
	    -docdir %{_docdir}/%{name}-%{version} -headerdir %{_includedir} \
	    -datadir %{_datadir}/qt
	    -release -qt-gif -system-zlib -no-g++-exceptions -stl -remote -system-libpng \
	    -system-libjpeg -system-libmng -sm -xinerama -xrender -xft -xkb"

########################################################################
# STATIC SINGLE-THREAD
########################################################################

./configure \
	$DEFAULTOPT \
	-no-thread \
	-static \
	-qt-imgfmt-png \
	-qt-imgfmt-jpeg \
	-qt-imgfmt-mng \
	-qt-sql-mysql \
	-qt-sql-odbc \
	-qt-sql-psql \
	-qt-style-cde \
	-qt-style-compact \
	-qt-style-motif \
	-qt-style-motifplus \
	-qt-style-platinum \
	-qt-style-sgi \
	-qt-style-windows \
	-no-style-windowsxp \
	<<_EOF_
yes
_EOF_

# Build libraries and everything needed to do this. Do not build examples and 
# such. They will be built with shared, sigle-thread libraries.
%{__make} symlinks src-qmake src-moc sub-src

########################################################################
# STATIC MULTI-THREAD
########################################################################

# This will not remove previously compiled libraries.
%{__make} clean

./configure \
	$DEFAULTOPT \
	-thread \
	-static \
	-qt-imgfmt-png \
	-qt-imgfmt-jpeg \
	-qt-imgfmt-mng \
	-qt-sql-mysql \
	-qt-sql-odbc \
	-qt-sql-psql \
	-qt-style-cde \
	-qt-style-compact \
	-qt-style-motif \
	-qt-style-motifplus \
	-qt-style-platinum \
	-qt-style-sgi \
	-qt-style-windows \
	-no-style-windowsxp \
	<<_EOF_
yes
_EOF_

# Build libraries and everything needed to do this. Do not build examples and 
# such. They will be built with shared, sigle-thread libraries.
%{__make} symlinks src-qmake src-moc sub-src

########################################################################
# SHARED SINGLE-THREAD
########################################################################

# This will not remove previously compiled libraries.
%{__make} clean

./configure \
	$DEFAULTOPT \
	-no-thread \
	-shared \
	-plugindir %{_libdir}/qt/plugins \
	-plugin-imgfmt-png \
	-plugin-imgfmt-jpeg \
	-plugin-imgfmt-mng \
	-plugin-sql-mysql \
	-plugin-sql-odbc \
	-plugin-sql-psql \
	-plugin-style-cde \
	-plugin-style-compact \
	-plugin-style-motif \
	-plugin-style-motifplus \
	-plugin-style-platinum \
	-plugin-style-sgi \
	-plugin-style-windows \
	-no-style-windowsxp \
	<<_EOF_
yes
_EOF_

# Build libraries and everything needed to do this. Do not build examples and 
# such. They will be built with shared, multi-thread libraries.
%{__make} symlinks src-qmake src-moc sub-src
# Dont make tools, only plugins.
%{__make} -C plugins/src/ sub-imageformats sub-sqldrivers sub-styles

########################################################################
# SHARED MULTI-THREAD
########################################################################

# This will not remove previously compiled libraries. But WILL remove
# plugins. And even if they weren't removed, they would be overwritten
# by next compilation. So they must be backed up.
mkdir plugins-st
cp -R plugins/{imageformats,sqldrivers,styles} plugins-st
%{__make} clean

./configure \
	$DEFAULTOPT \
	-thread \
	-shared \
	-plugindir %{_libdir}/qt/plugins-mt \
	-plugin-imgfmt-png \
	-plugin-imgfmt-jpeg \
	-plugin-imgfmt-mng \
	-plugin-sql-mysql \
	-plugin-sql-odbc \
	-plugin-sql-psql \
	-plugin-style-cde \
	-plugin-style-compact \
	-plugin-style-motif \
	-plugin-style-motifplus \
	-plugin-style-platinum \
	-plugin-style-sgi \
	-plugin-style-windows \
	-no-style-windowsxp \
	<<_EOF_
yes
_EOF_

# Do not build tutorial and examples. Provide them as sources.
%{__make} symlinks src-qmake src-moc sub-src sub-tools

%install
cd qt-x11-free-3.0.4
rm -rf $RPM_BUILD_ROOT

QTDIR=`/bin/pwd`; export QTDIR
LD_LIBRARY_PATH="$QTDIR/lib" ; export LD_LIBRARY_PATH
PATH="$QTDIR/bin:$PATH"

%{__make} install INSTALL_ROOT=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man{1,3} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}/lib \
	$RPM_BUILD_ROOT%{_libdir}/qt/plugins

install doc/man/man1/*		$RPM_BUILD_ROOT%{_mandir}/man1
install doc/man/man3/*		$RPM_BUILD_ROOT%{_mandir}/man3

install lib/libqt.a		$RPM_BUILD_ROOT%{_libdir}
install lib/libqt-mt.a		$RPM_BUILD_ROOT%{_libdir}

install lib/libqt.so.*.*.*	$RPM_BUILD_ROOT%{_libdir}
ln -s libqt.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libqt.so

cp -R plugins-st/* $RPM_BUILD_ROOT%{_libdir}/qt/plugins

cp -p lib/libqt-mt.prl $RPM_BUILD_ROOT%{_examplesdir}/%{name}/lib
cp -dpR .qmake.cache examples tutorial \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}

# Fix Makefiles for tutorial and examples. How people who made so cool
# library could screw build process so badly?
find $RPM_BUILD_ROOT%{_examplesdir}/%{name} -regex '.*/\(examples\|tutorial\).*/Makefile$' -exec \
	perl -pi -e '
		print "QTDIR    = %{_prefix}\n" if $. == 1;
		s|(-I\$\(QTDIR\)/include)|$1/qt|g;
		s|(\$\(QTDIR\))(/mkspecs)|$1/share/qt$2|g;
		s|'$QTDIR'|%{_prefix}|g;
	' {} \;

gzip -9nf LICENSE.QPL

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.QPL.gz
%attr(755,root,root) %{_libdir}/libqt.so.*
%attr(755,root,root) %{_libdir}/libqui.so.*
%attr(755,root,root) %{_libdir}/libeditor.so.*
%attr(755,root,root) %{_libdir}/libqt-mt.so.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins*
%dir %{_libdir}/%{name}/plugins*/imageformats
%dir %{_libdir}/%{name}/plugins*/styles
%dir %{_libdir}/%{name}/plugins*/sqldrivers
%attr(755,root,root) %{_libdir}/%{name}/plugins*/imageformats/*.so
%attr(755,root,root) %{_libdir}/%{name}/plugins*/styles/*.so

%files devel
%defattr(644,root,root,755)
%doc %{_docdir}
%attr(755,root,root) %{_bindir}/*
%{_libdir}/libqt.so
%{_libdir}/libqt-mt.so
%{_libdir}/libqui.so
%{_libdir}/libeditor.so
%{_includedir}
%{_mandir}/man?/*
%dir %{_libdir}/%{name}/plugins*/designer
%attr(755,root,root) %{_libdir}/%{name}/plugins*/designer/*.so
%dir %{_datadir}/qt
%{_datadir}/qt/mkspecs
%{_datadir}/qt/designer

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files examples
%defattr(644,root,root,755)
/usr/src/examples/%{name}

%files plugins-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins*/sqldrivers/lib*mysql.so

%files plugins-psql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins*/sqldrivers/lib*psql.so

%files plugins-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins*/sqldrivers/lib*odbc.so
