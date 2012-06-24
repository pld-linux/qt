# TODO:
# - hack assistant, to use some global config file with documentation list
#
# Conditional build:
# _with_nas		- enable nas audio support
# _with_single		- build also single threaded libraries
# _with_static		- build also static libraries
#
# _without_cups		- disable cups support
# _without_mysql	- without mysql support
# _without_odbc		- without unixODBC support
# _without_pgsql	- without PostgreSQL support
#

%define 	_snap	030405

%define 	_withsql	1

%{?_without_mysql:%{?_without_pgsql:%{?_without_odbc:%define _withsql 0}}}

Summary:	The Qt3 GUI application framework
Summary(es):	Biblioteca para ejecutar aplicaciones GUI Qt
Summary(pl):	Biblioteka Qt3 do tworzenia GUI
Summary(pt_BR):	Estrutura para rodar aplica��es GUI Qt
Name:		qt
Version:	3.2
Release:	0.%{_snap}.4
Epoch:		6
License:	GPL / QPL
Group:		X11/Libraries
#Source0:	ftp://ftp.trolltech.com/qt/source/%{name}-x11-free-%{version}.tar.bz2
Source0:	%{name}-copy-%{_snap}.tar.bz2
Source1:	ftp://ftp.trolltech.com/qsa/%{name}-designer-changes-qsa-beta3.tar.gz
Patch0:		%{name}-tools.patch
Patch1:		%{name}-postgresql_7_2.patch
Patch2:		%{name}-mysql_includes.patch
Patch3:		%{name}-FHS.patch
Patch4:		%{name}-qmake-opt.patch
Patch5:		%{name}-cursors.patch
Patch6:         %{name}-qmake-nostatic.patch
Patch7:		%{name}-disable_tutorials.patch
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel >= 4.3.0
BuildRequires:	XFree86-xft-devel
# incompatible with bison
BuildRequires:	byacc
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel >= 1.0.0
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libungif-devel
%{!?_without_mysql:BuildRequires:	mysql-devel}
BuildRequires:	perl
%{!?_without_pgsql:BuildRequires:	postgresql-backend-devel}
%{!?_without_pgsql:BuildRequires:	postgresql-devel}
%{!?_without_odbc:BuildRequires:	unixODBC-devel}
%{!?_without_cups:BuildRequires:        cups-devel}
%{?_with_nas:BuildRequires:	nas-devel}
BuildRequires:	zlib-devel
%{?_with_prelink:BuildRequires:	objprelink}
%{?_with_single:Provides:	qt-st}
Requires:	OpenGL
Requires:	XFree86-libs >= 4.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	qt-extensions

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_includedir	%{_prefix}/include/qt
%define         _qt_sl		3.1.2

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
Qt, or file:/usr/share/doc/%{name}-%{version}/html/index.html for Qt
documentation in HTML.

%description devel -l es
Contiene los archivos necesarios para desarrollar aplicaciones
usando Qt: archivos de inclusi�n, compilador de metaobjetos Qt,
p�ginas de manual, documentaci�n HTML y programas ejemplo. Mira
http://www.troll.no para m�s informaci�n sobre el Qt, o el
archivo file:/usr/share/doc/%{name}-%{version}/html/index.html en la
documentaci�n en HTML.

%description devel -l pl
Pakiet tem zawiera pliki potrzebne do tworzenia i kompilacji aplikacji
korzystaj�cych z biblioteki Qt, jak pliki nag��wkowe, meta kompiler
(moc), dokumentacj�. Zobacz http://www.troll.no/ aby dowiedzie� si�
wi�cej o Qt. Dokumentacj� do biblioteki znajdziesz tak�e pod:
/usr/share/doc/%{name}-%{version}/html/index.html

%description devel -l pt_BR
Cont�m os arquivos necess�rios para desenvolver aplica��es usando Qt: arquivos
de inclus�o, compilador de meta-objetos Qt, veja http://www.trolltech.com para
mais informa��es sobre ele.

%package static
Summary:	Qt static libraries
Summary(pl):	Biblioteki statyczne Qt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static QT libraries.

%description static -l pl
Statyczne biblioteki Qt.

%package doc
Summary:	QT Documentation in HTML format
Summary(pl):	Dokumentacja QT w formacie HTML
Group:		X11/Development/Libraries
Obsoletes:	%{name}-doc-html

%description doc
Qt documentation in HTML format.

%description doc -l pl
Dokumentacja qt w formacie HTML.

%package man
Summary:	QT man pages
Summary(pl):	QT - strony man
Group:		X11/Development/Libraries
Obsoletes:	%{name}-doc-man

%description man
Qt documentation in man pages format.

%description man -l pl
Dokumentacja qt w formacie stron man.

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

%package plugins-mysql
Summary:	Database plugin for mysql Qt support
Summary(pl):	Wtyczka MySQL do Qt
Summary(pt_BR):	Plugin de suporte a mysql para Qt
Group:		X11/Libraries
Requires:	%{name} = %{version}
Provides:	qt-plugin-sql

%description plugins-mysql
Database plugin for mysql Qt support.

%description plugins-mysql -l pl
Wtyczka MySQL do Qt.

%description plugins-mysql -l pt_BR
Plugin de suporte a mysql para Qt.

%package plugins-psql
Summary:	Database plugin for pgsql Qt support
Summary(pl):	Wtyczka PostgreSQL do Qt
Summary(pt_BR):	Plugin de suporte a pgsql para Qt
Group:		X11/Libraries
Requires:	%{name} = %{version}
Provides:       qt-plugin-sql

%description plugins-psql
Database plugin for pgsql Qt support.

%description plugins-psql -l pl
Wtyczka PostgreSQL do Qt.

%description plugins-psql -l es
Plugin de suporte a pgsql para Qt.

%package plugins-odbc
Summary:	Database plugin for ODBC Qt support
Summary(pl):	Wtyczka ODBC do Qt
Summary(pt_BR):	Plugin de suporte a ODBC para Qt
Group:		X11/Libraries
Requires:	%{name} = %{version}
Provides:       qt-plugin-sql

%description plugins-odbc
Database plugin for ODBC Qt support.

%description plugins-odbc -l pl
Wtyczka ODBC do Qt.

%description plugins-odbc -l pt_BR
Plugin de suporte a ODBC para Qt.

%package utils
Summary:	QT Utils
Summary(pl):	Narz�dzia QT
Group:		X11/Development/Tools
Requires:	%{name}-devel = %{version}

%description utils
QT Development Utilities.

%description utils -l pl
Narzedzia programistyczne QT.

%prep
%setup -q -n %{name}-copy -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

# Remove CVS stuff
rm -rf `find . -name CVS`

# There is no file pointed by this sym-link
# and there is cp -L in %%install
rm -f include/qt_windows.h

%build
export QTDIR=`/bin/pwd`
export LD_LIBRARY_PATH="$QTDIR/lib"
PATH="$QTDIR/bin:$PATH"

# change QMAKE_CFLAGS_RELEASE to build
# properly optimized libs
perl -pi -e "
	s|-O2|%{rpmcflags}|;
	" mkspecs/linux-g++/qmake.conf

%{__make} -f Makefile.cvs

##################################
# DEFAULT OPTIONS FOR ALL BUILDS #
##################################

DEFAULTOPT=" \
	-datadir %{_datadir}/qt \
	-docdir %{_docdir}/%{name}-doc \
	-fast \
	-headerdir %{_includedir} \
	%{?_without_cups:-no-cups} \
	-no-exceptions \
	-no-style-windowsxp \
	-prefix %{_prefix} \
	-qt-gif \
	-system-libjpeg \
	-system-libmng \
	-system-libpng \
	%{?_with_nas:-system-nas-sound} \
	-system-zlib \
	%{?debug:-debug}"

##############################
# OPTIONS FOR STATIC-{ST,MT} #
##############################

%if %{?_with_static:1}0
STATICOPT=" \
	-qt-imgfmt-jpeg \
	-qt-imgfmt-mng \
	-qt-imgfmt-png \
	%{!?_without_mysql:-qt-sql-mysql} \
	%{!?_without_odbc:-qt-sql-odbc} \
	%{!?_without_pgsql:-qt-sql-psql} \
	-static"
%endif

########################
# STATIC SINGLE-THREAD #
########################

%if %{?_with_static:%{?_with_single:1}}0
done

OPTFLAGS="%{rpmcflags}" \
./configure \
	$DEFAULTOPT \
	$STATICOPT \
	<<_EOF_
yes
_EOF_

# Do not build tutorial and examples. Provide them as sources.
%{__make} symlinks src-qmake src-moc sub-src

# This will not remove previously compiled libraries.
%{__make} clean
%endif

#######################
# STATIC MULTI-THREAD #
#######################

%if %{?_with_static:1}0
OPTFLAGS="%{rpmcflags}" \
./configure \
	$DEFAULTOPT \
	$STATICOPT \
	-thread \
	<<_EOF_
yes
_EOF_

# Do not build tutorial and examples. Provide them as sources.
%{__make} symlinks src-qmake src-moc sub-src

# This will not remove previously compiled libraries.
%{__make} clean
%endif

##############################
# OPTIONS FOR SHARED-{ST,MT} #
##############################

SHAREDOPT=" \
	-plugin-imgfmt-jpeg \
	-plugin-imgfmt-mng \
	-plugin-imgfmt-png \
	%{!?_without_mysql:-plugin-sql-mysql} \
	%{!?_without_odbc:-plugin-sql-odbc} \
	%{!?_without_pgsql:-plugin-sql-psql} \
	-plugin-style-cde \
	-plugin-style-compact \
	-plugin-style-motif \
	-plugin-style-motifplus \
	-plugin-style-platinum \
	-plugin-style-sgi \
	-plugin-style-windows"
	
########################
# SHARED SINGLE-THREAD #
########################

%if %{?_with_single:1}0
# workaround for some nasty bug to avoid
# linking plugins statically with -lqt-mt
rm -f lib/libqt-mt.prl

OPTFLAGS="%{rpmcflags}" \
./configure \
	$DEFAULTOPT \
	$SHAREDOPT \
	-plugindir %{_libdir}/qt/plugins-st \
	<<_EOF_
yes
_EOF_

# Do not build tutorial and examples. Provide them as sources.
%{__make} symlinks src-qmake src-moc sub-src

# Dont make tools, only plugins.
%{__make} -C plugins/src/ sub-imageformats sub-sqldrivers sub-styles

# This will not remove previously compiled libraries. But WILL remove
# plugins. And even if they weren't removed, they would be overwritten
# by next compilation. So they must be backed up.
rm -rf plugins-st
mkdir plugins-st
cp -R plugins/{imageformats,styles} plugins-st
%{?_withsql:cp -R plugins/sqldrivers plugins-st}
%{__make} clean
%endif

#######################
# SHARED MULTI-THREAD #
#######################

OPTFLAGS="%{rpmcflags}" \
./configure \
	$DEFAULTOPT \
	$SHAREDOPT \
	-thread \
	-plugindir %{_libdir}/qt/plugins-mt \
	<<_EOF_
yes
_EOF_

# Do not build tutorial and examples. Provide them as sources.
%{__make} symlinks src-qmake src-moc sub-src sub-tools

%install
rm -rf $RPM_BUILD_ROOT

export QTDIR=`/bin/pwd`

%{__make} install INSTALL_ROOT=$RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT%{_libdir}/qt/plugins-mt/network \
	%{?_with_single:$RPM_BUILD_ROOT%{_libdir}/qt/plugins-st/network} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}/lib \
	$RPM_BUILD_ROOT%{_mandir}/man{1,3} \
	$RPM_BUILD_ROOT%{_libdir}/qt/plugins-mt/qsa
	
install bin/{findtr,qt20fix,qtrename140} \
	tools/{msg2qm/msg2qm,mergetr/mergetr} \
	$RPM_BUILD_ROOT%{_bindir}

%if %{?_with_static:1}0
install lib/libqt*.a		$RPM_BUILD_ROOT%{_libdir}
%endif

%if %{?_with_single:1}0
install lib/libqt.so.*.*.*	$RPM_BUILD_ROOT%{_libdir}
ln -sf libqt.so.%{_qt_sl}	$RPM_BUILD_ROOT%{_libdir}/libqt.so
cp -R plugins-st/*		$RPM_BUILD_ROOT%{_libdir}/qt/plugins-st/
%endif

install doc/man/man1/*		$RPM_BUILD_ROOT%{_mandir}/man1
install doc/man/man3/*		$RPM_BUILD_ROOT%{_mandir}/man3

cp -dpR examples tutorial $RPM_BUILD_ROOT%{_examplesdir}/%{name}
	
mv $RPM_BUILD_ROOT{%{_libdir}/*.prl,%{_examplesdir}/%{name}/lib}

perl -pi -e "
	s|(QMAKE_INCDIR_QT\\s*=\\s*\\\$\\(QTDIR\\)/include)|\$1/qt|
	" $RPM_BUILD_ROOT/%{_datadir}/qt/mkspecs/linux-g++/qmake.conf

plik="$RPM_BUILD_ROOT/%{_datadir}/qt/mkspecs/linux-g++/qmake.conf"
cat $plik|grep -v QMAKE_CFLAGS_RELEASE|grep -v QMAKE_CXXFLAGS_RELEASE|grep -v QMAKE_CFLAGS_DEBUG|grep -v QMAKE_CXXFLAGS_DEBUG > $plik.1

echo -e "QMAKE_CFLAGS_RELEASE\t=\t%%{rpmcflags}" > $plik
echo -e "QMAKE_CXXFLAGS_RELEASE\t=\t%%{rpmcflags}" >> $plik
echo -e "QMAKE_CFLAGS_DEBUG\t=\t%%{debugcflags}" >> $plik
echo -e "QMAKE_CXXFLAGS_DEBUG\t=\t%%{debugcflags}" >> $plik
cat $plik.1 >> $plik
rm $plik.1

# We provide qt style classes as plugins,
# so make corresponding changes to the qconfig.h.
chmod 644 $RPM_BUILD_ROOT%{_includedir}/qconfig.h

cat >> $RPM_BUILD_ROOT%{_includedir}/qconfig.h << EOF

/* All of these style classes we provide as plugins */
#define QT_NO_STYLE_CDE
#define QT_NO_STYLE_COMPACT
#define QT_NO_STYLE_MOTIF
#define QT_NO_STYLE_MOTIFPLUS
#define QT_NO_STYLE_PLATINUM
#define QT_NO_STYLE_SGI
#define QT_NO_STYLE_WINDOWS
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc FAQ LICENSE.* README* changes*
%attr(755,root,root) %{_libdir}/libqassistantclient.so.*
%attr(755,root,root) %{_libdir}/libdesigner.so.*
%attr(755,root,root) %{_libdir}/libeditor.so.*
%attr(755,root,root) %{_libdir}/libqui.so.*
%attr(755,root,root) %{_libdir}/libqt*.so.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins-?t
%dir %{_libdir}/%{name}/plugins-?t/imageformats
%dir %{_libdir}/%{name}/plugins-?t/network
# There wont be any qsa linked with st.
%dir %{_libdir}/%{name}/plugins-mt/qsa
%{?_withsql:%dir %{_libdir}/%{name}/plugins-?t/sqldrivers}
%dir %{_libdir}/%{name}/plugins-?t/styles
%attr(755,root,root) %{_libdir}/%{name}/plugins-?t/imageformats/*.so
%attr(755,root,root) %{_libdir}/%{name}/plugins-?t/styles/*.so
%dir %{_datadir}/qt

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/[!adl]*
%attr(755,root,root) %{_bindir}/l[!i]*
%{_libdir}/libqassistantclient.so
%{_libdir}/libdesigner.so
%{_libdir}/libeditor.so
%{_libdir}/libqui.so
%{_libdir}/libqt*.so
%{_includedir}
%{_datadir}/qt/[!d]*
%{_mandir}/man1/*

%if %{?_with_static:1}0
%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%endif

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-doc

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}

%files man
%defattr(644,root,root,755)
%{_mandir}/man3/*

%if %{!?_without_mysql:1}0
%files plugins-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-?t/sqldrivers/lib*mysql.so
%endif

%if %{!?_without_pgsql:1}0
%files plugins-psql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-?t/sqldrivers/lib*psql.so
%endif

%if %{!?_without_odbc:1}0
%files plugins-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-?t/sqldrivers/lib*odbc.so
%endif

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/[ad]*
%attr(755,root,root) %{_bindir}/li*
%dir %{_libdir}/%{name}/plugins*/designer
%attr(755,root,root) %{_libdir}/%{name}/plugins-?t/designer/*.so
%{_datadir}/qt/designer
