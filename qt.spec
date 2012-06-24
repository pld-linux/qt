#
# TODO:
#   qmake generates Makefile with INCPATH containing -I$(QTDIR)/include/. It
#   should be -I$(QTDIR)/include/qt
#
#   *.png files aren't installed.
#
# Conditional build:
# _with_prelink		- witht objprelink (problems with new binutils?)
# _without_mysql	- without mysql support
# _without_psql		- without PostgreSQL support
# _without_odbc		- without unixODBC support
#

%ifarch saprc sparcv9 sparc64 alpha

Summary:	The Qt3 GUI application framework
Summary(es):	Biblioteca para ejecutar aplicaciones GUI Qt
Summary(pl):	Biblioteka Qt3 do tworzenia GUI
Summary(pt_BR):	Estrutura para rodar aplica��es GUI Qt
Name:		qt
Version:	3.0.4
Release:	3
Epoch:		3
License:	GPL / QPL
Group:		X11/Libraries
Source0:	ftp://ftp.trolltech.com/qt/source/%{name}-x11-free-%{version}.tar.bz2
Patch0:		%{name}-tools.patch
Patch1:		%{name}-qmake.patch
Patch2:		%{name}-parse_error.patch
Patch3:		%{name}-postgresql_7_2.patch
Patch4:		%{name}-mysql_includes.patch
Patch5:		%{name}-FHS.patch
Patch6:		%{name}-configure.patch
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel >= 4.0.2
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel >= 1.0.0
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libungif-devel
%if %{!?_without_mysql:1}%{?_without_mysql:0}
BuildRequires:	mysql-devel
%endif
BuildRequires:	nas-devel
BuildRequires:	perl
%if %{!?_without_psql:1}%{?_without_psql:0}
BuildRequires:	postgresql-backend-devel
BuildRequires:	postgresql-devel
%endif
%if %{!?_without_odbc:1}%{?_without_odbc:0}
BuildRequires:	unixODBC-devel
%endif
BuildRequires:	zlib-devel
%{?_witht_prelink:BuildRequires:	objprelink}
Requires:	OpenGL
Requires:	XFree86-libs >= 4.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	qt-extensions

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_includedir	%{_prefix}/include/qt
%define		_mandir		%{_prefix}/man

%description
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications for the X
Window System. Qt is written in C++ and is fully object-oriented.

This package contains the shared library needed to run Qt
applications, as well as the README files for Qt.

%description -l es
Contiene las bibliotecas compartidas necesarias para ejecutar
aplicaciones Qt, bien como los archivos README.

%description -l pl
Pakiet ten zawiera bibliotek� niezb�dn� do uruchamiania aplikacji Qt,
jak r�wnie� pliki README z Qt.

%description -l pt_BR
Cont�m as bibliotecas compartilhadas necess�rias para rodar aplica��es Qt, bem
como os arquivos README.

%package devel
Summary:	Development files and documentation for the Qt GUI toolkit
Summary(es):	Archivos de inclusi�n y documentaci�n necesaria para compilar aplicaciones Qt
Summary(pl):	Pliki nag��wkowe, przyk�ady i dokumentacja do biblioteki
Summary(pt_BR):	Arquivos de inclus�o e documenta��o necess�ria para compilar aplica��es Qt
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	XFree86-devel
Requires:	freetype-devel
Requires:	libjpeg-devel
Requires:	libmng-devel
Requires:	libpng-devel
Requires:	libstdc++-devel
Conflicts:	qt2-devel

%description devel
Contains the files necessary to develop applications using Qt: header
files, the Qt meta object compiler, man pages, HTML documentation and
example programs. See http://www.troll.no/ for more information about
Qt, or file:/usr/share/doc/%{name}-devel-%{version}/index.html for Qt
documentation in HTML.

%description devel -l es
Contiene los archivos necesarios para desarrollar aplicaciones
usando Qt: archivos de inclusi�n, compilador de metaobjetos Qt,
p�ginas de manual, documentaci�n HTML y programas ejemplo. Mira
http://www.troll.no para m�s informaci�n sobre el Qt, o el
archivo file:/usr/lib/qt/html/index.html en la documentaci�n
en HTML.

%description devel -l pl
Pakiet tem zawiera pliki potrzebne do tworzenia i kompilacji aplikacji
korzystaj�cych z biblioteki Qt, jak pliki nag��wkowe, meta kompiler
(moc), dokumentacj�. Zobacz http://www.troll.no/ aby dowiedzie� si�
wi�cej o Qt. Dokumentacj� do biblioteki znajdziesz tak�e pod:
/usr/share/doc/%{name}-devel-%{version}/index.html

%description devel -l pt_BR
Cont�m os arquivos necess�rios para desenvolver aplica��es usando Qt: arquivos
de inclus�o, compilador de meta-objetos Qt, veja http://www.trolltech.com para
mais informa��es sobre ele.

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
Summary:	Example programs made with Qt version %{version}
Summary(pl):	�wiczenia i przyk�ady do Qt
Summary(pt_BR):	Programas exemplo desenvolvidos com o Qt 
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description examples
Example programs made with Qt version %{version}.

%description examples -l pl
�wiczenia/przyk�ady do Qt.

%description examples -l pt_BR
Programas exemplo para o Qt vers�o %{version}.

%if %{!?_without_mysql:1}%{?_without_mysql:0}
%package plugins-mysql
Summary:	Database plugin for mysql Qt support
Summary(pl):	Wtyczka MySQL do Qt
Summary(pt_BR):	Plugin de suporte a mysql para Qt
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description plugins-mysql
Database plugin for mysql Qt support.

%description plugins-mysql -l pl
Wtyczka MySQL do Qt.

%description plugins-mysql -l pt_BR
Plugin de suporte a mysql para Qt.
%endif

%if %{!?_without_psql:1}%{?_without_psql:0}
%package plugins-psql
Summary:	Database plugin for pgsql Qt support
Summary(pl):	Wtyczka PostgreSQL do Qt
Summary(pt_BR):	Plugin de suporte a pgsql para Qt
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description plugins-psql
Database plugin for pgsql Qt support.

%description plugins-psql -l pl
Wtyczka PostgreSQL do Qt.

%description plugins-psql -l es
Plugin de suporte a pgsql para Qt.
%endif

%if %{!?_without_odbc:1}%{?_without_odbc:0}
%package plugins-odbc
Summary:	Database plugin for ODBC Qt support
Summary(pl):	Wtyczka ODBC do Qt
Summary(pt_BR):	Plugin de suporte a ODBC para Qt
Group:		X11/Libraries
Requires:	%{name} = %{version}

%description plugins-odbc
Database plugin for ODBC Qt support.

%description plugins-odbc -l pl
Wtyczka ODBC do Qt.

%description plugins-odbc -l pt_BR
Plugin de suporte a ODBC para Qt.
%endif

%prep
%setup -q -n %{name}-x11-free-%{version}
%patch0 -p1
%ifnarch %{ix86} ppc
%{!?_witht_prelink:%patch1 -p1}
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
STYLESLIST="cde compact motif motifplus platinum sgi windows"

########################################################################
# STATIC SINGLE-THREAD
########################################################################

DEFAULTSTYLES=""
for i in $STYLESLIST; do
	DEFAULTSTYLES="$DEFAULTSTYLES -qt-style-$i"
done

./configure \
	$DEFAULTOPT \
	-no-thread \
	-static \
	-qt-imgfmt-png \
	-qt-imgfmt-jpeg \
	-qt-imgfmt-mng \
%if %{!?_without_odbc:1}%{?_without_odbc:0}
	-qt-sql-mysql \
%endif
%if %{!?_without_odbc:1}%{?_without_odbc:0}
	-qt-sql-odbc \
%endif
%if %{!?_without_odbc:1}%{?_without_odbc:0}
	-qt-sql-psql \
%endif
	$DEFAULTSTYLES \
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
%if %{!?_without_odbc:1}%{?_without_odbc:0}
	-qt-sql-mysql \
%endif
%if %{!?_without_odbc:1}%{?_without_odbc:0}
	-qt-sql-odbc \
%endif
%if %{!?_without_odbc:1}%{?_without_odbc:0}
	-qt-sql-psql \
%endif
	$DEFAULTSTYLES \
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

DEFAULTSTYLES=""
for i in $STYLESLIST; do
	DEFAULTSTYLES="$DEFAULTSTYLES -plugin-style-$i"
done


# This will not remove previously compiled libraries.
%{__make} clean

./configure \
	$DEFAULTOPT \
	-no-thread \
	-shared \
	-plugindir %{_libdir}/qt/plugins-st \
	-plugin-imgfmt-png \
	-plugin-imgfmt-jpeg \
	-plugin-imgfmt-mng \
%if %{!?_without_odbc:1}%{?_without_odbc:0}
	-plugin-sql-mysql \
%endif
%if %{!?_without_odbc:1}%{?_without_odbc:0}
	-plugin-sql-odbc \
%endif
%if %{!?_without_odbc:1}%{?_without_odbc:0}
	-plugin-sql-psql \
%endif
	$DEFAULTSTYLES \
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
%if %{!?_without_mysql:1}%{?_without_mysql:0}
	-plugin-sql-mysql \
%endif
%if %{!?_without_odbc:1}%{?_without_odbc:0}
	-plugin-sql-odbc \
%endif
%if %{!?_without_psql:1}%{?_without_psql:0}
	-plugin-sql-psql \
%endif
	$DEFAULTSTYLES \
	-no-style-windowsxp \
	<<_EOF_
yes
_EOF_

# Do not build tutorial and examples. Provide them as sources.
%{__make} symlinks src-qmake src-moc sub-src sub-tools

%install
rm -rf $RPM_BUILD_ROOT

QTDIR=`/bin/pwd`; export QTDIR
LD_LIBRARY_PATH="$QTDIR/lib" ; export LD_LIBRARY_PATH
PATH="$QTDIR/bin:$PATH"

%{__make} install INSTALL_ROOT=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man{1,3} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}/lib \
	$RPM_BUILD_ROOT%{_libdir}/qt/plugins-st

install bin/findtr tools/msg2qm/msg2qm tools/mergetr/mergetr $RPM_BUILD_ROOT%{_bindir}

install doc/man/man1/*		$RPM_BUILD_ROOT%{_mandir}/man1
install doc/man/man3/*		$RPM_BUILD_ROOT%{_mandir}/man3

install lib/libqt.a		$RPM_BUILD_ROOT%{_libdir}
install lib/libqt-mt.a		$RPM_BUILD_ROOT%{_libdir}

install lib/libqt.so.*.*.*	$RPM_BUILD_ROOT%{_libdir}
ln -s libqt.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libqt.so

cp -R plugins-st/* $RPM_BUILD_ROOT%{_libdir}/qt/plugins-st/

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

%if %{!?_without_mysql:1}%{?_without_mysql:0}
%files plugins-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins*/sqldrivers/lib*mysql.so
%endif

%if %{!?_without_psql:1}%{?_without_psql:0}
%files plugins-psql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins*/sqldrivers/lib*psql.so
%endif

%if %{!?_without_odbc:1}%{?_without_odbc:0}
%files plugins-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins*/sqldrivers/lib*odbc.so
%endif
