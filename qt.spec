#
# Conditional build:
%bcond_with	nas		# enable NAS audio support
%bcond_with	nvidia		# prelink Qt/KDE and depend on NVIDIA binaries
%bcond_without	single		# don't build single-threaded libraries
%bcond_without	static_libs	# don't build static libraries
%bcond_without	cups		# disable CUPS support
%bcond_without	mysql		# don't build MySQL plugin
%bcond_without	odbc		# don't build unixODBC plugin
%bcond_without	pgsql		# don't build PostgreSQL plugin
%bcond_without	designer	# don't build designer (it takes long)
%bcond_without	sqlite		# don't build SQLite plugin
%bcond_with	ibase		# build ibase (InterBase/Firebird) plugin
%bcond_with	pch		# enable pch in qmake
%bcond_with	pch_devel	# enable experimental boost (for developers only!)
#
%define		_withsql	1
%{!?with_sqlite:%{!?with_ibase:%{!?with_mysql:%{!?with_pgsql:%{!?with_odbc:%undefine _withsql}}}}}

%define		_snap		040422
%define		_ver		3.3.2
%define		_packager	adgor

Summary:	The Qt3 GUI application framework
Summary(es):	Biblioteca para ejecutar aplicaciones GUI Qt
Summary(pl):	Biblioteka Qt3 do tworzenia GUI
Summary(pt_BR):	Estrutura para rodar aplicações GUI Qt
Name:		qt
#Version:	%{_ver}.%{_snap}
Version:	%{_ver}
Release:	3
Epoch:		6
License:	GPL/QPL
Group:		X11/Libraries
#Source0:	http://ep09.pld-linux.org/~%{_packager}/kde/%{name}-copy-%{_snap}.tar.bz2
Source0:	ftp://ftp.trolltech.com/qt/source/%{name}-x11-free-%{version}.tar.bz2
# Source0-md5:	903cad618274ad84d7d13fd0027a6c3c
Source1:	http://ep09.pld-linux.org/~%{_packager}/kde/%{name}-copy-patches-040427.tar.bz2
# Source1-md5:	ec9cfcbeee331483184bed6807cd8394
Source2:	%{name}config.desktop
Source3:	designer.desktop
Source4:	assistant.desktop
Source5:	linguist.desktop
Patch0:		%{name}-tools.patch
Patch1:		%{name}-FHS.patch
Patch2:		%{name}-qmake-nostatic.patch
Patch3:		%{name}-disable_tutorials.patch
Patch4:		%{name}-locale.patch
Patch5:		%{name}-make_use_of_locale.patch
Patch6:		%{name}-qmake-opt.patch
Patch7:		%{name}-xcursor_version.patch
Patch8:		%{name}-gcc34.patch
# for troll only
Patch9:		%{name}-autodetect-pch.patch
Patch10:	%{name}-antialias.patch
URL:		http://www.trolltech.com/products/qt/
BuildRequires:	OpenGL-devel
%{?with_nvidia:BuildRequires:	XFree86-driver-nvidia-devel < 1.0.4620}
# incompatible with bison
BuildRequires:	byacc
%{?with_cups:BuildRequires:	cups-devel}
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.0
%{?with_pch:BuildRequires:	gcc >= 5:3.4.0}
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel >= 1.0.0
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libungif-devel
%{?with_mysql:BuildRequires:	mysql-devel}
%ifarch %{ix86}
%{?with_ibase:BuildRequires:Firebird-devel}
%endif
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	perl-base
%{?with_pgsql:BuildRequires:	postgresql-backend-devel}
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	sed >= 4.0
%{?with_odbc:BuildRequires:	unixODBC-devel}
%{?with_sqlite:BuildRequires:	sqlite-devel}
BuildRequires:	xcursor-devel
BuildRequires:	xft-devel
BuildRequires:	xrender-devel
BuildRequires:	zlib-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	kdelibs <= 8:3.2-0.030602.1
Obsoletes:	qt-extensions

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

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
Contém as bibliotecas compartilhadas necessárias para rodar aplicações
Qt, bem como os arquivos README.

%package devel
Summary:	Development files and documentation for the Qt GUI toolkit
Summary(es):	Archivos de inclusión y documentación necesaria para compilar aplicaciones Qt
Summary(pl):	Pliki nag³ówkowe, przyk³ady i dokumentacja do biblioteki
Summary(pt_BR):	Arquivos de inclusão e documentação necessária para compilar aplicações Qt
Group:		X11/Development/Libraries
Requires:	OpenGL-devel
Requires:	freetype-devel
Requires:	libjpeg-devel
Requires:	libmng-devel
Requires:	libpng-devel
Requires:	libstdc++-devel
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	qt2-devel

%description devel
Contains the files necessary to develop applications using Qt: header
files, the Qt meta object compiler, man pages, HTML documentation and
example programs. See http://www.trolltech.com/ for more information
about Qt, or file:/usr/share/doc/%{name}-%{version}/html/index.html
for Qt documentation in HTML.

%description devel -l es
Contiene los archivos necesarios para desarrollar aplicaciones usando
Qt: archivos de inclusión, compilador de metaobjetos Qt, páginas de
manual, documentación HTML y programas ejemplo. Mira
http://www.trolltech.com/ para más información sobre el Qt, o el
archivo file:/usr/share/doc/%{name}-%{version}/html/index.html en la
documentación en HTML.

%description devel -l pl
Pakiet tem zawiera pliki potrzebne do tworzenia i kompilacji aplikacji
korzystaj±cych z biblioteki Qt, jak pliki nag³ówkowe, meta kompiler
(moc), dokumentacjê. Zobacz http://www.trolltech.com/ aby dowiedzieæ
siê wiêcej o Qt. Dokumentacjê do biblioteki znajdziesz tak¿e pod:
/usr/share/doc/%{name}-%{version}/html/index.html

%description devel -l pt_BR
Contém os arquivos necessários para desenvolver aplicações usando Qt:
arquivos de inclusão, compilador de meta-objetos Qt, veja
http://www.trolltech.com/ para mais informações sobre ele.

%package static
Summary:	Qt static library
Summary(pl):	Biblioteka statyczna Qt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static Qt library.

%description static -l pl
Statyczna biblioteka Qt.

%package doc
Summary:	QT Documentation in HTML format
Summary(pl):	Dokumentacja QT w formacie HTML
Group:		X11/Development/Libraries
Obsoletes:	qt-doc-html

%description doc
Qt documentation in HTML format.

%description doc -l pl
Dokumentacja qt w formacie HTML.

%package man
Summary:	QT man pages
Summary(pl):	QT - strony man
Group:		X11/Development/Libraries
Obsoletes:	qt-doc-man

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

%package plugin-ibase
Summary:	Database plugin for InterBase/Firebird Qt support
Summary(pl):	Wtyczka InterBase/Firebird do Qt
Summary(pt_BR):	Plugin de suporte a InterBase/Firebird para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-plugin-sql
Requires:	Firebird-lib

%description plugin-ibase
Database plugin for InterBase/Firebird Qt support.

%description plugin-ibase -l pl
Wtyczka InterBase/Firebird do Qt.

%description plugin-ibase -l pt_BR
Plugin de suporte a InterBase/Firebird para Qt.

%package plugin-mysql
Summary:	Database plugin for MySQL Qt support
Summary(pl):	Wtyczka MySQL do Qt
Summary(pt_BR):	Plugin de suporte a MySQL para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-plugin-sql
Obsoletes:	qt-plugins-mysql

%description plugin-mysql
Database plugin for MySQL Qt support.

%description plugin-mysql -l pl
Wtyczka MySQL do Qt.

%description plugin-mysql -l pt_BR
Plugin de suporte a MySQL para Qt.

%package plugin-odbc
Summary:	Database plugin for ODBC Qt support
Summary(pl):	Wtyczka ODBC do Qt
Summary(pt_BR):	Plugin de suporte a ODBC para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-plugin-sql
Obsoletes:	qt-plugins-odbc

%description plugin-odbc
Database plugin for ODBC Qt support.

%description plugin-odbc -l pl
Wtyczka ODBC do Qt.

%description plugin-odbc -l pt_BR
Plugin de suporte a ODBC para Qt.

%package plugin-psql
Summary:	Database plugin for PostgreSQL Qt support
Summary(pl):	Wtyczka PostgreSQL do Qt
Summary(pt_BR):	Plugin de suporte a pgsql para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%{?with_single:Requires:	%{name}-st = %{epoch}:%{version}-%{release}}
Provides:	%{name}-plugin-sql
%{?with_single:Provides:	%{name}-plugin-sql-st = %{epoch}:%{version}-%{release}}
Obsoletes:	qt-plugins-psql

%description plugin-psql
Database plugin for pgsql Qt support.

%description plugin-psql -l pl
Wtyczka PostgreSQL do Qt.

%description plugin-psql -l es
Plugin de suporte a pgsql para Qt.

%package plugin-sqlite
Summary:	Database plugin for SQLite Qt support
Summary(pl):	Wtyczka SQLite do Qt
Summary(pt_BR):	Plugin de suporte a SQLite para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-plugin-sql

%description plugin-sqlite
Database plugin for SQLite Qt support.

%description plugin-sqlite -l pl
Wtyczka SQLite do Qt.

%description plugin-sqlite -l pt_BR
Plugin de suporte a SQLite para Qt.

%package st
Summary:	Single-threaded Qt library
Summary(pl):	Jednow±tkowa wersja biblioteki Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description st
Single-threaded Qt library (deprecated, for foreign applications
only).

%description st -l pl
Jednow±tkowa wersja biblioteki Qt (nie zalecana, instniej±ca na
potrzeby obcych aplikacji).

%package st-devel
Summary:	Development files for single-threaded Qt library
Summary(pl):	Pliki programistyczne dla jednow±tkowej biblioteki Qt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-st = %{epoch}:%{version}-%{release}

%description st-devel
Development files for single-threaded Qt library.

%description st-devel -l pl
Pliki programistyczne dla jednow±tkowej biblioteki Qt.

%package st-static
Summary:	Single-threaded Qt static libraries
Summary(pl):	Jednow±tkowa statyczna biblioteka Qt
Group:		X11/Development/Libraries
Requires:	%{name}-st-devel = %{epoch}:%{version}-%{release}

%description st-static
Single-threaded Qt static libraries.

%description st-static -l pl
Jednow±tkowa statyczna biblioteka Qt.

%package st-plugin-ibase
Summary:	Database plugin for InterBase/Firebird support in single-threaded Qt
Summary(pl):	Wtyczka InterBase/Firebird do jednow±tkowej wersji Qt
Group:		X11/Libraries
Requires:	%{name}-st = %{epoch}:%{version}-%{release}
Provides:	%{name}-st-plugin-sql = %{epoch}:%{version}-%{release}

%description st-plugin-ibase
Database plugin for InterBase/Firebird support in single-threaded Qt.

%description st-plugin-ibase -l pl
Wtyczka InterBase/Firebird do jednow±tkowej wersji Qt.

%package st-plugin-mysql
Summary:	Database plugin for MySQL support in single-threaded Qt
Summary(pl):	Wtyczka MySQL do jednow±tkowej wersji Qt
Group:		X11/Libraries
Requires:	%{name}-st = %{epoch}:%{version}-%{release}
Provides:	%{name}-st-plugin-sql = %{epoch}:%{version}-%{release}

%description st-plugin-mysql
Database plugin for MySQL support in single-threaded Qt.

%description st-plugin-mysql -l pl
Wtyczka MySQL do jednow±tkowej wersji Qt.

%package st-plugin-odbc
Summary:	Database plugin for ODBC support in single-threaded Qt
Summary(pl):	Wtyczka ODBC do jednow±tkowej wersji Qt
Group:		X11/Libraries
Requires:	%{name}-st = %{epoch}:%{version}-%{release}
Provides:	%{name}-st-plugin-sql = %{epoch}:%{version}-%{release}

%description st-plugin-odbc
Database plugin for ODBC support in single-threaded Qt.

%description st-plugin-odbc -l pl
Wtyczka ODBC do jednow±tkowej wersji Qt.

%package st-plugin-psql
Summary:	Database plugin for PostgreSQL support in single-threaded Qt
Summary(pl):	Wtyczka PostgreSQL do jednow±tkowej wersji Qt
Summary(pt_BR):	Plugin de suporte a pgsql para Qt
Group:		X11/Libraries
Requires:	%{name}-st = %{epoch}:%{version}-%{release}
Provides:	%{name}-st-plugin-sql = %{epoch}:%{version}-%{release}

%description st-plugin-psql
Database plugin for PostgreSQL support in single-threaded Qt.

%description st-plugin-psql -l pl
Wtyczka PostgreSQL do jednow±tkowej wersji Qt.

%package st-plugin-sqlite
Summary:	Database plugin for SQLite support in single-threaded Qt
Summary(pl):	Wtyczka SQLite do jednow±tkowej wersji Qt
Group:		X11/Libraries
Requires:	%{name}-st = %{epoch}:%{version}-%{release}
Provides:	%{name}-st-plugin-sql = %{epoch}:%{version}-%{release}

%description st-plugin-sqlite
Database plugin for SQLite support in single-threaded Qt.

%description st-plugin-sqlite -l pl
Wtyczka SQLite do jednow±tkowej wersji Qt.

%package style-cde
Summary:	Qt style - CDE
Summary(pl):	Styl Qt - CDE
Group:		X11/Amusements
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	qt =< 6:3.3.0.040207-1

%description style-cde
Qt style - CDE.

%description style-cde -l pl
Styl Qt - CDE.

%package style-compact
Summary:	Qt style - Compact
Summary(pl):	Styl Qt - Compact
Group:		X11/Amusements
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	qt =< 6:3.3.0.040207-1

%description style-compact
Qt style - Compact.

%description style-compact -l pl
Styl Qt - Compact.

%package utils
Summary:	QT Utils
Summary(pl):	Narzêdzia QT
Group:		X11/Development/Tools
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description utils
QT Development Utilities.

%description utils -l pl
Narzêdzia programistyczne QT.

%package -n qtconfig
Summary:	QT widgets configuration tool
Summary(pl):	Narzêdzie do konfigurowania widgetów QT
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n qtconfig
A tool for configuring look and behavior of QT widgets.

%description -n qtconfig -l pl
Narzêdie do konfiguracji wygl±du i zachowania widgetów QT.

%package designer
Summary:	IDE used for GUI designing with QT library
Summary(pl):	IDE s³u¿±ce do projektowania GUI za pomoc± biblioteki QT
Group:		X11/Applications
Requires:	%{name}-designer-libs = %{epoch}:%{version}-%{release}

%description designer
IDE used for GUI designing with QT library.

%description designer -l pl
IDE s³u¿±ce do projektowania GUI za pomoc± biblioteki QT.

%package designer-libs
Summary:	Libraries IDE used for GUI designing with QT library
Summary(pl):	Biblioteki do IDE s³u¿±cego do projektowania GUI za pomoc± biblioteki QT
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description designer-libs
Libraries IDE used for GUI designing with QT library.

%description designer-libs -l pl
Biblioteki do IDE s³u¿±cego do projektowania GUI za pomoc± biblioteki
QT.

%prep
#setup -q -n %{name}-copy-%{_snap}
%setup -q -n %{name}-x11-free-%{version} -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

cat >> patches/DISABLED <<EOF
0005
0039
0042
0043
0047
EOF
./apply_patches

# change QMAKE_CFLAGS_RELEASE to build
# properly optimized libs
plik="mkspecs/linux-g++/qmake.conf"

perl -pi -e "
	s|/usr/X11R6/lib|/usr/X11R6/%{_lib}|;
	s|/usr/lib|%{_libdir}|;
	s|\\(QTDIR\\)/lib|\\(QTDIR\\)/%{_lib}|;
	" $plik

cat $plik \
	|grep -v QMAKE_CFLAGS_RELEASE \
	|grep -v QMAKE_CXXFLAGS_RELEASE \
	|grep -v QMAKE_CFLAGS_DEBUG \
	|grep -v QMAKE_CXXFLAGS_DEBUG \
	> $plik.1

mv $plik.1 $plik
echo >> $plik
echo -e "QMAKE_CFLAGS_RELEASE\t=\t%{rpmcflags}" >> $plik
echo -e "QMAKE_CXXFLAGS_RELEASE\t=\t%{rpmcflags}" >> $plik
echo -e "QMAKE_CFLAGS_DEBUG\t=\t%{debugcflags}" >> $plik
echo -e "QMAKE_CXXFLAGS_DEBUG\t=\t%{debugcflags}" >> $plik
%{?with_pch:echo -e "DEFINES\t+=\tUSING_PCH" >> $plik}

%build
export QTDIR=`/bin/pwd`
export YACC='byacc -d'
export PATH=$QTDIR/bin:$PATH
export LD_LIBRARY_PATH=$QTDIR/%{_lib}:$LD_LIBRARY_PATH

if [ "%{_lib}" != "lib" ] ; then
	ln -s lib "%{_lib}"
fi

# pass OPTFLAGS to build qmake itself with optimization
export OPTFLAGS="%{rpmcflags}"

#%{__make} -f Makefile.cvs

##################################
# DEFAULT OPTIONS FOR ALL BUILDS #
##################################

DEFAULTOPT=" \
	-DQT_CLEAN_NAMESPACE \
	-verbose \
	-prefix %{_prefix} \
	-libdir %{_libdir} \
	-headerdir %{_includedir}/qt \
	-datadir %{_datadir}/qt \
	-docdir %{_docdir}/%{name}-doc \
	-sysconfdir %{_sysconfdir}/qt \
	-translationdir %{_datadir}/locale/ \
	-fast \
	-qt-gif \
	-system-libjpeg \
	-system-libmng \
	-system-libpng \
	-system-zlib \
	-no-exceptions \
	-ipv6 \
	-I%{_includedir}/postgresql/server \
	-I%{_includedir}/mysql \
	%{!?with_cups:-no-cups} \
	%{?with_nas:-system-nas-sound} \
	%{?with_nvidia:-dlopen-opengl} \
	%{?debug:-debug}"

##################################
#   OPTIONS FOR STATIC-{ST,MT}   #
##################################

%if %{with static_libs}
STATICOPT=" \
	-qt-imgfmt-jpeg \
	-qt-imgfmt-mng \
	-qt-imgfmt-png \
	%{?with_mysql:-qt-sql-mysql} \
	%{?with_odbc:-qt-sql-odbc} \
	%{?with_pgsql:-qt-sql-psql} \
	%{?with_sqlite:-qt-sql-sqlite} \
	%{?with_ibase:-qt-sql-ibase} \
	-static"
%endif

##################################
#      STATIC SINGLE-THREAD      #
##################################

%if %{with static_libs} && %{with single}
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

##################################
#      STATIC MULTI-THREAD       #
##################################

%if %{with static_libs}
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

##################################
#   OPTIONS FOR SHARED-{ST,MT}   #
##################################

SHAREDOPT=" \
	-plugin-imgfmt-jpeg \
	-plugin-imgfmt-mng \
	-plugin-imgfmt-png \
	%{?with_mysql:-plugin-sql-mysql} \
	%{?with_odbc:-plugin-sql-odbc} \
	%{?with_pgsql:-plugin-sql-psql} \
	%{?with_sqlite:-plugin-sql-sqlite} \
	%{?with_ibase:-plugin-sql-ibase} \
	-plugin-style-cde \
	-plugin-style-compact \
	-plugin-style-motif \
	-plugin-style-motifplus \
	-plugin-style-platinum \
	-plugin-style-sgi \
	-plugin-style-windows"

##################################
#      SHARED SINGLE-THREAD      #
##################################

%if %{with single}
# workaround for some nasty bug to avoid
# linking plugins statically with -lqt-mt
rm -f %{_lib}/libqt-mt.prl

./configure \
	$DEFAULTOPT \
	$SHAREDOPT \
	-plugindir %{_libdir}/qt/plugins-st \
	<<_EOF_
yes
_EOF_

# Do not build tutorial and examples. Provide them as sources.
%{__make} symlinks src-qmake src-moc sub-src

# Do not make tools, only plugins.
%{__make} -C plugins/src sub-imageformats sub-sqldrivers sub-styles

# This will not remove previously compiled libraries. But WILL remove
# plugins. And even if they weren't removed, they would be overwritten
# by next compilation. So they must be backed up.
rm -rf plugins-st
mkdir plugins-st
cp -R plugins/{imageformats,styles} plugins-st
%{?_withsql:cp -R plugins/sqldrivers plugins-st}
%{__make} clean
%endif

##################################
#      SHARED MULTI-THREAD       #
##################################

./configure \
	$DEFAULTOPT \
	$SHAREDOPT \
	-thread \
	-plugindir %{_libdir}/qt/plugins-mt \
	<<_EOF_
yes
_EOF_

%if %{without designer}
grep -v designer tools/tools.pro > tools/tools.pro.1
mv tools/tools.pro{.1,}
%{__make} -C tools/designer/uic \
	UIC="LD_PRELOAD=$QTDIR/%{_lib}/libqt-mt.so.3 $QTDIR/bin/uic -L $QTDIR/plugins"
%endif

# Do not build tutorial and examples. Provide them as sources.
#%%{__make} symlinks src-qmake src-moc sub-src sub-tools
%{__make} sub-tools \
	UIC="LD_PRELOAD=$QTDIR/%{_lib}/libqt-mt.so.3 $QTDIR/bin/uic -L $QTDIR/plugins"

%if %{with designer}
cd tools/designer/designer
LD_PRELOAD=$QTDIR/%{_lib}/libqt-mt.so.3 lrelease designer_de.ts
LD_PRELOAD=$QTDIR/%{_lib}/libqt-mt.so.3 lrelease designer_fr.ts
%endif
cd $QTDIR/tools/assistant
LD_PRELOAD=$QTDIR/%{_lib}/libqt-mt.so.3 lrelease assistant_de.ts
LD_PRELOAD=$QTDIR/%{_lib}/libqt-mt.so.3 lrelease assistant_fr.ts
cd $QTDIR/tools/linguist/linguist
LD_PRELOAD=$QTDIR/%{_lib}/libqt-mt.so.3 lrelease linguist_de.ts
LD_PRELOAD=$QTDIR/%{_lib}/libqt-mt.so.3 lrelease linguist_fr.ts
cd $QTDIR

##make -C extensions/nsplugin/src

%install
rm -rf $RPM_BUILD_ROOT

export QTDIR=`/bin/pwd`

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT%{_sysconfdir}/qt \
	$RPM_BUILD_ROOT%{_libdir}/qt/plugins-mt/{crypto,network} \
	%{?with_single:$RPM_BUILD_ROOT%{_libdir}/qt/plugins-st/network} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}/lib \
	$RPM_BUILD_ROOT%{_mandir}/man{1,3} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install bin/{findtr,qt20fix,qtrename140} \
	tools/{msg2qm/msg2qm,mergetr/mergetr} \
	$RPM_BUILD_ROOT%{_bindir}

%if %{with static_libs}
install %{_lib}/libqt*.a		$RPM_BUILD_ROOT%{_libdir}
%endif

%if %{with single}
install %{_lib}/libqt.so.*.*.*	$RPM_BUILD_ROOT%{_libdir}
ln -sf libqt.so.%{_ver}		$RPM_BUILD_ROOT%{_libdir}/libqt.so
install %{_lib}/qt.pc		$RPM_BUILD_ROOT%{_pkgconfigdir}
cp -R plugins-st/*		$RPM_BUILD_ROOT%{_libdir}/qt/plugins-st
%endif

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%if %{with designer}
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}/designer.desktop
%endif

install %{SOURCE4} $RPM_BUILD_ROOT%{_desktopdir}/
install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}/


%if %{without designer}
install bin/uic $RPM_BUILD_ROOT%{_bindir}
%endif

install tools/qtconfig/images/appicon.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/qtconfig.png

install doc/man/man1/*.1	$RPM_BUILD_ROOT%{_mandir}/man1
install doc/man/man3/*.3qt	$RPM_BUILD_ROOT%{_mandir}/man3

cp -dpR examples tutorial $RPM_BUILD_ROOT%{_examplesdir}/%{name}

mv $RPM_BUILD_ROOT{%{_libdir}/*.prl,%{_examplesdir}/%{name}/lib}

# From now QMAKE_INCDIR_QT becomes %{_includedir}/qt
perl -pi -e "
	s|(QMAKE_INCDIR_QT\\s*=\\s*\\\$\\(QTDIR\\)/include)|\$1/qt|
	" $RPM_BUILD_ROOT/%{_datadir}/qt/mkspecs/linux-g++/qmake.conf

# We provide qt style classes as plugins,
# so make corresponding changes to the qconfig.h.
chmod 644 $RPM_BUILD_ROOT%{_includedir}/qt/qconfig.h

cat >> $RPM_BUILD_ROOT%{_includedir}/qt/qconfig.h << EOF

/* All of these style classes we provide as plugins */
#define QT_NO_STYLE_CDE
#define QT_NO_STYLE_COMPACT
#define QT_NO_STYLE_MOTIF
#define QT_NO_STYLE_MOTIFPLUS
#define QT_NO_STYLE_PLATINUM
#define QT_NO_STYLE_SGI
#define QT_NO_STYLE_WINDOWS

EOF

%if %{with pch_devel}
cd $RPM_BUILD_ROOT%{_includedir}/qt
for h in qevent.h qglist.h qmap.h qobject.h qpixmap.h \
	qptrlist.h qstring.h qstrlist.h qstringlist.h \
	qvaluelist.h qwidget.h; do
	%{__cxx} -s $h
done
cd -
%endif

install -d $RPM_BUILD_ROOT%{_datadir}/locale/{ar,de,fr,ru,he,cs,sk}/LC_MESSAGES
install translations/qt_ar.qm $RPM_BUILD_ROOT%{_datadir}/locale/ar/LC_MESSAGES/qt.qm
install translations/qt_de.qm $RPM_BUILD_ROOT%{_datadir}/locale/de/LC_MESSAGES/qt.qm
install translations/qt_fr.qm $RPM_BUILD_ROOT%{_datadir}/locale/fr/LC_MESSAGES/qt.qm
install translations/qt_ru.qm $RPM_BUILD_ROOT%{_datadir}/locale/ru/LC_MESSAGES/qt.qm
install translations/qt_iw.qm $RPM_BUILD_ROOT%{_datadir}/locale/he/LC_MESSAGES/qt.qm
install translations/qt_cs.qm $RPM_BUILD_ROOT%{_datadir}/locale/cs/LC_MESSAGES/qt.qm
install translations/qt_sk.qm $RPM_BUILD_ROOT%{_datadir}/locale/sk/LC_MESSAGES/qt.qm


%if %{with designer}
install tools/designer/designer/designer_de.qm $RPM_BUILD_ROOT%{_datadir}/locale/de/LC_MESSAGES/designer.qm
install tools/designer/designer/designer_fr.qm $RPM_BUILD_ROOT%{_datadir}/locale/fr/LC_MESSAGES/designer.qm
%endif

install tools/assistant/assistant_de.qm $RPM_BUILD_ROOT%{_datadir}/locale/de/LC_MESSAGES/assistant.qm
install tools/assistant/assistant_fr.qm $RPM_BUILD_ROOT%{_datadir}/locale/fr/LC_MESSAGES/assistant.qm

install tools/linguist/linguist/linguist_de.qm $RPM_BUILD_ROOT%{_datadir}/locale/de/LC_MESSAGES/linguist.qm
install tools/linguist/linguist/linguist_fr.qm $RPM_BUILD_ROOT%{_datadir}/locale/fr/LC_MESSAGES/linguist.qm

install tools/linguist/qm2ts/qm2ts.1 $RPM_BUILD_ROOT%{_mandir}/man1

rm -rf `find $RPM_BUILD_ROOT -name CVS`

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

cat << EOF

 *******************************************************
 *                                                     *
 *  NOTE:                                              *
 *  After qt 3.2.0 the single threaded version was     *
 *  separated. Please install qt-st if You really need *
 *  it. If You do not use qt-st explicitly, please     *
 *  ignore this, as You will not notice any changes.   *
 *  In most cases do not install qt-st, as it is       *
 *  obsoleted.                                         *
 *                                                     *
 *******************************************************

EOF

%postun 	-p /sbin/ldconfig

%post 	st 	-p /sbin/ldconfig
%postun	st 	-p /sbin/ldconfig

%post	designer-libs -p /sbin/ldconfig
%postun	designer-libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc FAQ LICENSE.* README* changes*
%dir %{_sysconfdir}/qt
%attr(755,root,root) %{_libdir}/libqassistantclient.so.*.*.*
%attr(755,root,root) %{_libdir}/libqt-mt.so.*.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins-mt
%dir %{_libdir}/%{name}/plugins-mt/crypto
%dir %{_libdir}/%{name}/plugins-mt/imageformats
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/imageformats/*.so
%dir %{_libdir}/%{name}/plugins-mt/network
%{?_withsql:%dir %{_libdir}/%{name}/plugins-mt/sqldrivers}
%dir %{_libdir}/%{name}/plugins-mt/styles
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/styles/*.so
%dir %{_datadir}/qt
%lang(ar) %{_datadir}/locale/ar/LC_MESSAGES/qt.qm
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/qt.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/qt.qm
%lang(he) %{_datadir}/locale/he/LC_MESSAGES/qt.qm
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/qt.qm
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/qt.qm
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/qt.qm

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/findtr
%attr(755,root,root) %{_bindir}/lrelease
%attr(755,root,root) %{_bindir}/lupdate
%attr(755,root,root) %{_bindir}/mergetr
%attr(755,root,root) %{_bindir}/moc
%attr(755,root,root) %{_bindir}/msg2qm
%attr(755,root,root) %{_bindir}/qm2ts
%attr(755,root,root) %{_bindir}/qmake
%attr(755,root,root) %{_bindir}/qt20fix
#%attr(755,root,root) %{_bindir}/qt32castcompat
%attr(755,root,root) %{_bindir}/qtrename140
%attr(755,root,root) %{_bindir}/uic
%{_includedir}/qt
%{_libdir}/libqassistantclient.so
%{_libdir}/libqt-mt.so
%{_datadir}/qt/[!d]*
%{_mandir}/man1/*
%{_pkgconfigdir}/qt-mt.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libqt-mt.a
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

%if %{with mysql}
%files plugin-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/sqldrivers/lib*mysql.so
%endif

%if %{with pgsql}
%files plugin-psql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/sqldrivers/lib*psql.so
%endif

%if %{with odbc}
%files plugin-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/sqldrivers/lib*odbc.so
%endif

%if %{with sqlite}
%files plugin-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/sqldrivers/lib*sqlite.so
%endif

%if %{with ibase}
%files plugin-ibase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/sqldrivers/lib*ibase.so
%endif

%if %{with single}
%files st
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqt.so.*.*.*
%dir %{_libdir}/%{name}/plugins-st
%dir %{_libdir}/%{name}/plugins-st/network
%{?_withsql:%dir %{_libdir}/%{name}/plugins-st/sqldrivers}
%dir %{_libdir}/%{name}/plugins-st/imageformats
%attr(755,root,root) %{_libdir}/%{name}/plugins-st/imageformats/*.so
%dir %{_libdir}/%{name}/plugins-st/styles
%attr(755,root,root) %{_libdir}/%{name}/plugins-st/styles/*.so

%files st-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqt.so
%{_pkgconfigdir}/qt.pc

%if %{with static_libs}
%files st-static
%defattr(644,root,root,755)
%{_libdir}/libqt.a
%endif

%if %{with mysql}
%files st-plugin-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-st/sqldrivers/lib*mysql.so
%endif

%if %{with pgsql}
%files st-plugin-psql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-st/sqldrivers/lib*psql.so
%endif

%if %{with odbc}
%files st-plugin-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-st/sqldrivers/lib*odbc.so
%endif

%if %{with sqlite}
%files st-plugin-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-st/sqldrivers/lib*sqlite.so
%endif

%if %{with ibase}
%files st-plugin-ibase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-st/sqldrivers/lib*ibase.so
%endif
%endif

%if %{with designer}
%files designer-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdesignercore.so.*.*.*
%attr(755,root,root) %{_libdir}/libeditor.so.*.*.*
%attr(755,root,root) %{_libdir}/libqui.so.*.*.*
%attr(755,root,root) %{_libdir}/libdesignercore.so
%attr(755,root,root) %{_libdir}/libeditor.so
%attr(755,root,root) %{_libdir}/libqui.so

%files designer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/designer
%{_desktopdir}/designer.desktop
%dir %{_libdir}/%{name}/plugins-?t/designer
%attr(755,root,root) %{_libdir}/%{name}/plugins-?t/designer/*.so
%{_datadir}/qt/designer
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/designer.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/designer.qm
%endif

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/assistant
%attr(755,root,root) %{_bindir}/linguist
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/assistant.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/assistant.qm
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/linguist.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/linguist.qm
%{_desktopdir}/assistant.desktop
%{_desktopdir}/linguist.desktop

%files -n qtconfig
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtconfig
%{_desktopdir}/qtconfig.desktop
%{_pixmapsdir}/qtconfig.png
