# TODO:
# - hack assistant, to use some global config file with documentation list
# - hack linguist to make it use translations
# - hack qt to use translations
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

#%%define 	_snap	030723

%define 	_withsql	1

%{?_without_mysql:%{?_without_pgsql:%{?_without_odbc:%define _withsql 0}}}

Summary:	The Qt3 GUI application framework
Summary(es):	Biblioteca para ejecutar aplicaciones GUI Qt
Summary(pl):	Biblioteka Qt3 do tworzenia GUI
Summary(pt_BR):	Estrutura para rodar aplicações GUI Qt
Name:		qt
Version:	3.2.0
Release:	1
Epoch:		6
License:	GPL / QPL
Group:		X11/Libraries
Source0:	ftp://ftp.trolltech.com/qt/source/%{name}-x11-free-%{version}.tar.bz2
# Source0-md5:	9a639588000d0274666bcbb19e3d0af6
#Source0:	http://www.kernel.pl/~adgor/kde/%{name}-copy-%{_snap}.tar.bz2
#Source1:	ftp://ftp.trolltech.com/qsa/%{name}-designer-changes-qsa-beta3.tar.gz
#%% Source1-md5:	61dbb6efe50e04fcaa5a592e9bf58664
Patch0:		%{name}-tools.patch
Patch1:		%{name}-postgresql_7_2.patch
Patch2:		%{name}-mysql_includes.patch
Patch3:		%{name}-FHS.patch
#Patch4:	%{name}-qmake-opt.patch
#Patch5:	%{name}-cursors.patch
Patch6:         %{name}-qmake-nostatic.patch
Patch7:		%{name}-disable_tutorials.patch
Patch8:         %{name}-locale.patch
URL:		http://www.trolltech.com/products/qt/
BuildRequires:	OpenGL-devel
# incompatible with bison
BuildRequires:	byacc
%{!?_without_cups:BuildRequires:        cups-devel}
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel >= 1.0.0
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libungif-devel
%{!?_without_mysql:BuildRequires:	mysql-devel}
%{?_with_nas:BuildRequires:		nas-devel}
BuildRequires:	perl
%{!?_without_pgsql:BuildRequires:	postgresql-backend-devel}
%{!?_without_pgsql:BuildRequires:	postgresql-devel}
%{!?_without_odbc:BuildRequires:	unixODBC-devel}
BuildRequires:	xcursor-devel
BuildRequires:	xft-devel
BuildRequires:	zlib-devel
%{?_with_single:Provides:	%{name}-st = %{epoch}:%{version}-%{release}}
Requires:	OpenGL
Requires:	XFree86-libs >= 4.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	kdelibs =< 8:3.2-0.030602.1
Obsoletes:	qt-extensions

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_includedir	%{_prefix}/include/qt

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
Pakiet ten zawiera bibliotekê niezbêdn± do uruchamiania aplikacji Qt,
jak równie¿ pliki README z Qt.

%description -l pt_BR
Contém as bibliotecas compartilhadas necessárias para rodar aplicações Qt, bem
como os arquivos README.

%package devel
Summary:	Development files and documentation for the Qt GUI toolkit
Summary(es):	Archivos de inclusión y documentación necesaria para compilar aplicaciones Qt
Summary(pl):	Pliki nag³ówkowe, przyk³ady i dokumentacja do biblioteki
Summary(pt_BR):	Arquivos de inclusão e documentação necessária para compilar aplicações Qt
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
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
example programs. See http://www.trolltech.com for more information about
Qt, or file:/usr/share/doc/%{name}-%{version}/html/index.html for Qt
documentation in HTML.

%description devel -l es
Contiene los archivos necesarios para desarrollar aplicaciones
usando Qt: archivos de inclusión, compilador de metaobjetos Qt,
páginas de manual, documentación HTML y programas ejemplo. Mira
http://www.trolltech.com para más información sobre el Qt, o el
archivo file:/usr/share/doc/%{name}-%{version}/html/index.html en la
documentación en HTML.

%description devel -l pl
Pakiet tem zawiera pliki potrzebne do tworzenia i kompilacji aplikacji
korzystaj±cych z biblioteki Qt, jak pliki nag³ówkowe, meta kompiler
(moc), dokumentacjê. Zobacz http://www.trolltech.com aby dowiedzieæ siê
wiêcej o Qt. Dokumentacjê do biblioteki znajdziesz tak¿e pod:
/usr/share/doc/%{name}-%{version}/html/index.html

%description devel -l pt_BR
Contém os arquivos necessários para desenvolver aplicações usando Qt: arquivos
de inclusão, compilador de meta-objetos Qt, veja http://www.trolltech.com para
mais informações sobre ele.

%package static
Summary:	Qt static libraries
Summary(pl):	Biblioteki statyczne Qt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
%{?_with_single:Provides: %{name}-static-st = %{epoch}:%{version}-%{release}}

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
Summary(pl):	Æwiczenia i przyk³ady do Qt
Summary(pt_BR):	Programas exemplo desenvolvidos com o Qt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description examples
Example programs made with Qt version %{version}.

%description examples -l pl
Æwiczenia/przyk³ady do Qt.

%description examples -l pt_BR
Programas exemplo para o Qt versão %{version}.

%package plugin-mysql
Summary:	Database plugin for mysql Qt support
Summary(pl):	Wtyczka MySQL do Qt
Summary(pt_BR):	Plugin de suporte a mysql para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%{?_with_single:Requires: %{name}-st = %{epoch}:%{version}-%{release}}
Provides:	%{name}-plugin-sql
%{?_with_single:Provides: %{name}-plugin-sql-st = %{epoch}:%{version}-%{release}}
Obsoletes:	%{name}-plugins-mysql

%description plugin-mysql
Database plugin for mysql Qt support.

%description plugin-mysql -l pl
Wtyczka MySQL do Qt.

%description plugin-mysql -l pt_BR
Plugin de suporte a mysql para Qt.

%package plugin-psql
Summary:	Database plugin for pgsql Qt support
Summary(pl):	Wtyczka PostgreSQL do Qt
Summary(pt_BR):	Plugin de suporte a pgsql para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%{?_with_single:Requires: %{name}-st = %{epoch}:%{version}-%{release}}
Provides:	%{name}-plugin-sql
%{?_with_single:Provides: %{name}-plugin-sql-st = %{epoch}:%{version}-%{release}}
Obsoletes:	%{name}-plugins-psql

%description plugin-psql
Database plugin for pgsql Qt support.

%description plugin-psql -l pl
Wtyczka PostgreSQL do Qt.

%description plugin-psql -l es
Plugin de suporte a pgsql para Qt.

%package plugin-odbc
Summary:	Database plugin for ODBC Qt support
Summary(pl):	Wtyczka ODBC do Qt
Summary(pt_BR):	Plugin de suporte a ODBC para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%{?_with_single:Requires: %{name}-st = %{epoch}:%{version}-%{release}}
Provides:	%{name}-plugin-sql
%{?_with_single:Provides: %{name}-plugin-sql-st = %{epoch}:%{version}-%{release}}
Obsoletes:	%{name}-plugins-odbc

%description plugin-odbc
Database plugin for ODBC Qt support.

%description plugin-odbc -l pl
Wtyczka ODBC do Qt.

%description plugin-odbc -l pt_BR
Plugin de suporte a ODBC para Qt.

%package utils
Summary:	QT Utils
Summary(pl):	Narzêdzia QT
Group:		X11/Development/Tools
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description utils
QT Development Utilities.

%description utils -l pl
Narzedzia programistyczne QT.

%prep
#%%setup -q -n %{name}-copy
%setup -q -n %{name}-x11-free-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
#%patch4 -p1
#%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
export QTDIR=`/bin/pwd`
export YACC='byacc -d'

# change QMAKE_CFLAGS_RELEASE to build
# properly optimized libs
perl -pi -e "
	s|-O2|%{rpmcflags}|;
	" mkspecs/linux-g++/qmake.conf

#%{__make} -f Makefile.cvs

#./apply_patches

##################################
# DEFAULT OPTIONS FOR ALL BUILDS #
##################################

DEFAULTOPT=" \
	-prefix %{_prefix} \
	-headerdir %{_includedir} \
	-datadir %{_datadir}/qt \
	-docdir %{_docdir}/%{name}-doc \
	-sysconfdir %{_sysconfdir} \
	-fast \
	-qt-gif \
	-system-libjpeg \
	-system-libmng \
	-system-libpng \
	-system-zlib \
	-no-exceptions \
	%{?_without_cups:-no-cups} \
	%{?_with_nas:-system-nas-sound} \
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

./configure \
	$DEFAULTOPT \
	$SHAREDOPT \
	-thread \
	-plugindir %{_libdir}/qt/plugins-mt \
	<<_EOF_
yes
_EOF_

# Do not build tutorial and examples. Provide them as sources.
#%%{__make} symlinks src-qmake src-moc sub-src sub-tools
%{__make} sub-tools

%install
rm -rf $RPM_BUILD_ROOT

export QTDIR=`/bin/pwd`

%{__make} install INSTALL_ROOT=$RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT%{_libdir}/qt/plugins-mt/{network,qsa} \
	%{?_with_single:$RPM_BUILD_ROOT%{_libdir}/qt/plugins-st/network} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}/lib \
	$RPM_BUILD_ROOT%{_mandir}/man{1,3} \
	
install bin/{findtr,qt20fix,qtrename140} \
	tools/{msg2qm/msg2qm,mergetr/mergetr} \
	$RPM_BUILD_ROOT%{_bindir}

%if %{?_with_static:1}0
install lib/libqt*.a		$RPM_BUILD_ROOT%{_libdir}
%endif

%if %{?_with_single:1}0
install lib/libqt.so.*.*.*	$RPM_BUILD_ROOT%{_libdir}
ln -sf libqt.so.%{version}	$RPM_BUILD_ROOT%{_libdir}/libqt.so
cp -R plugins-st/*		$RPM_BUILD_ROOT%{_libdir}/qt/plugins-st/
%endif

install doc/man/man1/*.1	$RPM_BUILD_ROOT%{_mandir}/man1
install doc/man/man3/*.3qt	$RPM_BUILD_ROOT%{_mandir}/man3

cp -dpR examples tutorial $RPM_BUILD_ROOT%{_examplesdir}/%{name}
	
mv $RPM_BUILD_ROOT{%{_libdir}/*.prl,%{_examplesdir}/%{name}/lib}

cd $RPM_BUILD_ROOT
rm -rf `find . -name CVS`
cd -

perl -pi -e "
	s|(QMAKE_INCDIR_QT\\s*=\\s*\\\$\\(QTDIR\\)/include)|\$1/qt|
	" $RPM_BUILD_ROOT/%{_datadir}/qt/mkspecs/linux-g++/qmake.conf

plik="$RPM_BUILD_ROOT/%{_datadir}/qt/mkspecs/linux-g++/qmake.conf"
cat $plik \
	|grep -v QMAKE_CFLAGS_RELEASE \
	|grep -v QMAKE_CXXFLAGS_RELEASE \
	|grep -v QMAKE_CFLAGS_DEBUG \
	|grep -v QMAKE_CXXFLAGS_DEBUG \
	> $plik.1

echo -e "QMAKE_CFLAGS_RELEASE\t=\t%{rpmcflags}" > $plik
echo -e "QMAKE_CXXFLAGS_RELEASE\t=\t%{rpmcflags}" >> $plik
echo -e "QMAKE_CFLAGS_DEBUG\t=\t%{debugcflags}" >> $plik
echo -e "QMAKE_CXXFLAGS_DEBUG\t=\t%{debugcflags}" >> $plik
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
%attr(755,root,root) %{_libdir}/libqassistantclient.so.*.*.*
%attr(755,root,root) %{_libdir}/libdesignercore.so.*.*.*
%attr(755,root,root) %{_libdir}/libeditor.so.*.*.*
%attr(755,root,root) %{_libdir}/libqui.so.*.*.*
%attr(755,root,root) %{_libdir}/libqt*.so.*.*.*
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
%{_libdir}/libdesignercore.so
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
%files plugin-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-?t/sqldrivers/lib*mysql.so
%endif

%if %{!?_without_pgsql:1}0
%files plugin-psql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-?t/sqldrivers/lib*psql.so
%endif

%if %{!?_without_odbc:1}0
%files plugin-odbc
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
