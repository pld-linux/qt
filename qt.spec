#
# Conditional build:
%bcond_with	nas	# enable NAS audio support
%bcond_without	single	# don't build single-threaded libraries
%bcond_without	static	# don't build static libraries
%bcond_without	cups	# disable CUPS support
%bcond_without	mysql	# disable MySQL support
%bcond_without	odbc	# disable unixODBC support
%bcond_without	pgsql	# disable PostgreSQL support

%define		_withsql	1
%{!?with_mysql:%{!?with_pgsql:%{!?with_odbc:%undefine _withsql}}}

%define		_pset 031029

Summary:	The Qt3 GUI application framework
Summary(es):	Biblioteca para ejecutar aplicaciones GUI Qt
Summary(pl):	Biblioteka Qt3 do tworzenia GUI
Summary(pt_BR):	Estrutura para rodar aplicações GUI Qt
Name:		qt
Version:	3.2.2
Release:	2
Epoch:		6
License:	GPL / QPL
Group:		X11/Libraries
Source0:	ftp://ftp.trolltech.com/qt/source/%{name}-x11-free-%{version}.tar.bz2
# Source0-md5:	77d6e71e603fa54b9898d3364ef42aef
Source1:	http://www.kernel.pl/~adgor/kde/%{name}-copy-patches-%{_pset}.tar.bz2
# Source1-md5:	d76fc8b81687dcf89c6b215d7e4048bf
Patch0:		%{name}-tools.patch
Patch1:		%{name}-postgresql_7_2.patch
Patch2:		%{name}-mysql_includes.patch
Patch3:		%{name}-FHS.patch
Patch4:		%{name}-qmake-nostatic.patch
Patch5:		%{name}-disable_tutorials.patch
Patch6:		%{name}-locale.patch
Patch7:		%{name}-make_use_of_locale.patch
Patch8:		%{name}-make_assistant_use_global_docs.patch
Patch9:		%{name}-qlineedit_khtml_fix.patch
Patch10:	%{name}-qmake-opt.patch
Patch11:	%{name}-qmake-la-and-pc-fix.patch
#Patch12:	%{name}-post321fixes.patch
URL:		http://www.trolltech.com/products/qt/
BuildRequires:	OpenGL-devel
# incompatible with bison
BuildRequires:	byacc
%{?with_cups:BuildRequires:	cups-devel}
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel >= 1.0.0
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libungif-devel
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	perl-base
%{?with_pgsql:BuildRequires:	postgresql-backend-devel}
%{?with_pgsql:BuildRequires:	postgresql-devel}
%{?with_nas:BuildRequires:	nas-devel}
%{?with_odbc:BuildRequires:	unixODBC-devel}
BuildRequires:	xcursor-devel
BuildRequires:	xft-devel
BuildRequires:	zlib-devel
Requires:	OpenGL
Requires:	XFree86-libs >= 4.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	kdelibs <= 8:3.2-0.030602.1
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
Contém as bibliotecas compartilhadas necessárias para rodar aplicações
Qt, bem como os arquivos README.

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
Summary:	Database plugin for MySQL Qt support
Summary(pl):	Wtyczka MySQL do Qt
Summary(pt_BR):	Plugin de suporte a MySQL para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-plugin-sql
Obsoletes:	%{name}-plugins-mysql

%description plugin-mysql
Database plugin for MySQL Qt support.

%description plugin-mysql -l pl
Wtyczka MySQL do Qt.

%description plugin-mysql -l pt_BR
Plugin de suporte a MySQL para Qt.

%package plugin-psql
Summary:	Database plugin for PostgreSQL Qt support
Summary(pl):	Wtyczka PostgreSQL do Qt
Summary(pt_BR):	Plugin de suporte a pgsql para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%{?with_single:Requires:	%{name}-st = %{epoch}:%{version}-%{release}}
Provides:	%{name}-plugin-sql
%{?with_single:Provides:	%{name}-plugin-sql-st = %{epoch}:%{version}-%{release}}
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
Provides:	%{name}-plugin-sql
Obsoletes:	%{name}-plugins-odbc

%description plugin-odbc
Database plugin for ODBC Qt support.

%description plugin-odbc -l pl
Wtyczka ODBC do Qt.

%description plugin-odbc -l pt_BR
Plugin de suporte a ODBC para Qt.

%package st
Summary:	Single-threaded Qt library
Summary(pl):	Jednow±tkowa wersja biblioteki Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description st
Single-threaded Qt library (deprecated, for foreign applications only).

%description st -l pl
Jednow±tkowa wersja biblioteki Qt (nie zalecana, instniej±ca na potrzeby
obcych aplikacji).

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

%package utils
Summary:	QT Utils
Summary(pl):	Narzêdzia QT
Group:		X11/Development/Tools
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description utils
QT Development Utilities.

%description utils -l pl
Narzêdzia programistyczne QT.

%prep
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
%patch11 -p1
#%patch12 -p1

rm -rf `find . -name CVS`

# They currently don't apply
cat >> patches/DISABLED << EOF
0005
0006
0007
0010
0029
EOF

./apply_patches

# change QMAKE_CFLAGS_RELEASE to build
# properly optimized libs
perl -pi -e "
	s|-O2|%{rpmcflags}|;
	" mkspecs/linux-g++/qmake.conf

%build
export QTDIR=`/bin/pwd`
export YACC='byacc -d'
export PATH=$QTDIR/bin:$PATH
export LD_LIBRARY_PATH=$QTDIR/lib:$LD_LIBRARY_PATH

# pass OPTFLAGS for qmake itself
export OPTFLAGS="%{rpmcflags}"

##################################
# DEFAULT OPTIONS FOR ALL BUILDS #
##################################

DEFAULTOPT=" \
	-prefix %{_prefix} \
	-headerdir %{_includedir} \
	-datadir %{_datadir}/qt \
	-docdir %{_docdir}/%{name}-doc \
	-sysconfdir %{_sysconfdir} \
	-translationdir %{_datadir}/locale/ \
	-fast \
	-qt-gif \
	-system-libjpeg \
	-system-libmng \
	-system-libpng \
	-system-zlib \
	-no-exceptions \
	%{!?with_cups:-no-cups} \
	%{?with_nas:-system-nas-sound} \
	%{?debug:-debug}"

##############################
# OPTIONS FOR STATIC-{ST,MT} #
##############################

%if %{with static}
STATICOPT=" \
	-qt-imgfmt-jpeg \
	-qt-imgfmt-mng \
	-qt-imgfmt-png \
	%{?with_mysql:-qt-sql-mysql} \
	%{?with_odbc:-qt-sql-odbc} \
	%{?with_pgsql:-qt-sql-psql} \
	-static"
%endif

########################
# STATIC SINGLE-THREAD #
########################

%if %{with static} && %{with single}
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

%if %{with static}
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
	%{?with_mysql:-plugin-sql-mysql} \
	%{?with_odbc:-plugin-sql-odbc} \
	%{?with_pgsql:-plugin-sql-psql} \
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

%if %{with single}
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

export Z=`/bin/pwd`

# Do not build tutorial and examples. Provide them as sources.
#%%{__make} symlinks src-qmake src-moc sub-src sub-tools
%{__make} sub-tools \
	UIC="LD_PRELOAD=$Z/lib/libqt-mt.so.3 $Z/bin/uic -L $Z/plugins"

cd tools/designer/designer
LD_PRELOAD=$Z/lib/libqt-mt.so.3 lrelease designer_de.ts
LD_PRELOAD=$Z/lib/libqt-mt.so.3 lrelease designer_fr.ts
cd $Z/tools/assistant
LD_PRELOAD=$Z/lib/libqt-mt.so.3 lrelease assistant_de.ts
LD_PRELOAD=$Z/lib/libqt-mt.so.3 lrelease assistant_fr.ts
cd $Z/tools/linguist/linguist
LD_PRELOAD=$Z/lib/libqt-mt.so.3 lrelease linguist_de.ts
LD_PRELOAD=$Z/lib/libqt-mt.so.3 lrelease linguist_fr.ts
cd $Z

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man{1,3},%{_examplesdir}/%{name}/lib} \
	$RPM_BUILD_ROOT%{_libdir}/qt/plugins-{m,s}t/network

export QTDIR=`/bin/pwd`

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT%{_libdir}/qt/plugins-mt/{network,qsa} \
	%{?with_single:$RPM_BUILD_ROOT%{_libdir}/qt/plugins-st/network} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}/lib \
	$RPM_BUILD_ROOT%{_mandir}/man{1,3} \

install bin/{findtr,qt20fix,qtrename140,qt32castcompat} \
	tools/{msg2qm/msg2qm,mergetr/mergetr} \
	$RPM_BUILD_ROOT%{_bindir}

%if %{with static}
install lib/libqt*.a		$RPM_BUILD_ROOT%{_libdir}
%endif

%if %{with single}
install lib/libqt.so.*.*.*	$RPM_BUILD_ROOT%{_libdir}
ln -sf libqt.so.%{version}	$RPM_BUILD_ROOT%{_libdir}/libqt.so
install lib/qt.pc		$RPM_BUILD_ROOT%{_pkgconfigdir}
cp -R plugins-st/*		$RPM_BUILD_ROOT%{_libdir}/qt/plugins-st
%endif

install doc/man/man1/*.1	$RPM_BUILD_ROOT%{_mandir}/man1
install doc/man/man3/*.3qt	$RPM_BUILD_ROOT%{_mandir}/man3

cp -dpR examples tutorial $RPM_BUILD_ROOT%{_examplesdir}/%{name}

mv $RPM_BUILD_ROOT{%{_libdir}/*.prl,%{_examplesdir}/%{name}/lib}

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

install -d $RPM_BUILD_ROOT%{_datadir}/locale/{ar,de,fr,ru,he}/LC_MESSAGES
install translations/qt_ar.qm $RPM_BUILD_ROOT%{_datadir}/locale/ar/LC_MESSAGES/qt.qm
install translations/qt_de.qm $RPM_BUILD_ROOT%{_datadir}/locale/de/LC_MESSAGES/qt.qm
install translations/qt_fr.qm $RPM_BUILD_ROOT%{_datadir}/locale/fr/LC_MESSAGES/qt.qm
install translations/qt_ru.qm $RPM_BUILD_ROOT%{_datadir}/locale/ru/LC_MESSAGES/qt.qm
install translations/qt_iw.qm $RPM_BUILD_ROOT%{_datadir}/locale/he/LC_MESSAGES/qt.qm

install tools/designer/designer/designer_de.qm $RPM_BUILD_ROOT%{_datadir}/locale/de/LC_MESSAGES/designer.qm
install tools/designer/designer/designer_fr.qm $RPM_BUILD_ROOT%{_datadir}/locale/fr/LC_MESSAGES/designer.qm

install tools/assistant/assistant_de.qm $RPM_BUILD_ROOT%{_datadir}/locale/de/LC_MESSAGES/assistant.qm
install tools/assistant/assistant_fr.qm $RPM_BUILD_ROOT%{_datadir}/locale/fr/LC_MESSAGES/assistant.qm

install tools/linguist/linguist/linguist_de.qm $RPM_BUILD_ROOT%{_datadir}/locale/de/LC_MESSAGES/linguist.qm
install tools/linguist/linguist/linguist_fr.qm $RPM_BUILD_ROOT%{_datadir}/locale/fr/LC_MESSAGES/linguist.qm

install tools/linguist/qm2ts/qm2ts.1 $RPM_BUILD_ROOT%{_mandir}/man1

install -d $RPM_BUILD_ROOT%{_sysconfdir}/qt
echo -e "\n" > $RPM_BUILD_ROOT%{_sysconfdir}/qt/doclist

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

cat << EOF

 *******************************************************
 *                                                     *
 *  NOTE:                                              *
 *  After qt 3.2.0 the single version was separated.   *
 *  Please install qt-st if you really require it.     *
 *  If you do not use qt-st explicitly, please ignore  *
 *  this, as you will not notice any changes. In most  *
 *  cases do not install qt-st, as it is obsoleted.    *
 *                                                     *
 *******************************************************

EOF

%postun -p /sbin/ldconfig
%post st -p /sbin/ldconfig
%postun	st -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc FAQ LICENSE.* README* changes*
%attr(755,root,root) %{_libdir}/libqassistantclient.so.*.*.*
%attr(755,root,root) %{_libdir}/libdesignercore.so.*.*.*
%attr(755,root,root) %{_libdir}/libeditor.so.*.*.*
%attr(755,root,root) %{_libdir}/libqui.so.*.*.*
%attr(755,root,root) %{_libdir}/libqt-mt.so.*.*.*
%dir %{_sysconfdir}/qt
%ghost %{_sysconfdir}/qt/doclist
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins-mt
%dir %{_libdir}/%{name}/plugins-mt/network
%dir %{_libdir}/%{name}/plugins-mt/qsa
%{?_withsql:%dir %{_libdir}/%{name}/plugins-mt/sqldrivers}
%dir %{_libdir}/%{name}/plugins-mt/imageformats
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/imageformats/*.so
%dir %{_libdir}/%{name}/plugins-mt/styles
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/styles/*.so
%dir %{_datadir}/qt
%lang(ar) %{_datadir}/locale/ar/LC_MESSAGES/qt.qm
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/qt.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/qt.qm
%lang(he) %{_datadir}/locale/he/LC_MESSAGES/qt.qm
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/qt.qm

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/[!adl]*
%attr(755,root,root) %{_bindir}/l[!i]*
%{_libdir}/libqassistantclient.so
%{_libdir}/libdesignercore.so
%{_libdir}/libeditor.so
%{_libdir}/libqui.so
%{_libdir}/libqt-mt.so
%{_includedir}
%{_datadir}/qt/[!d]*
%{_mandir}/man1/*
%{_pkgconfigdir}/qt-mt.pc

%if %{with static}
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

%if %{with static}
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
%endif

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/[ad]*
%attr(755,root,root) %{_bindir}/li*
%dir %{_libdir}/%{name}/plugins*/designer
%attr(755,root,root) %{_libdir}/%{name}/plugins-?t/designer/*.so
%{_datadir}/qt/designer
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/assistant.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/assistant.qm
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/designer.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/designer.qm
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/linguist.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/linguist.qm
