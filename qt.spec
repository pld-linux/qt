#
# Conditional build:
# _with_nas		- enable nas audio support
# _without_cups		- disable cups support
# _without_examples	- don't build and include samples
# _without_mysql	- without mysql support
# _without_odbc		- without unixODBC support
# _without_pgsql	- without PostgreSQL support
# _with_static		- build static library
# _with_single		- build single threaded library

%define 	_snap	030405

%define 	_withsql	1

%{?_without_mysql:%{?_without_pgsql:%{?_without_odbc:%define _withsql 0}}}

Summary:	The Qt3 GUI application framework
Summary(es):	Biblioteca para ejecutar aplicaciones GUI Qt
Summary(pl):	Biblioteka Qt3 do tworzenia GUI
Summary(pt_BR):	Estrutura para rodar aplicações GUI Qt
Name:		qt
Version:	3.2
Release:	0.%{_snap}.2
Epoch:		6
License:	GPL / QPL
Group:		X11/Libraries
#Source0:	ftp://ftp.trolltech.com/qt/source/%{name}-x11-free-%{version}.tar.bz2
Source0:	%{name}-copy-%{_snap}.tar.bz2
Patch0:		%{name}-tools.patch
Patch1:		%{name}-postgresql_7_2.patch
Patch2:		%{name}-mysql_includes.patch
Patch3:		%{name}-FHS.patch
Patch4:		%{name}-qmake-opt.patch
Patch5:		%{name}-cursors.patch
Patch6:         %{name}-qmake-nostatic.patch
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
Requires:	OpenGL
Requires:	XFree86-libs >= 4.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	qt-extensions

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_includedir	%{_prefix}/include/qt
%define         _qt_sl		%{version}

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
usando Qt: archivos de inclusión, compilador de metaobjetos Qt,
páginas de manual, documentación HTML y programas ejemplo. Mira
http://www.troll.no para más información sobre el Qt, o el
archivo file:/usr/share/doc/%{name}-%{version}/html/index.html en la
documentación en HTML.

%description devel -l pl
Pakiet tem zawiera pliki potrzebne do tworzenia i kompilacji aplikacji
korzystaj±cych z biblioteki Qt, jak pliki nag³ówkowe, meta kompiler
(moc), dokumentacjê. Zobacz http://www.troll.no/ aby dowiedzieæ siê
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
Summary(pl):	Æwiczenia i przyk³ady do Qt
Summary(pt_BR):	Programas exemplo desenvolvidos com o Qt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description examples
Example programs made with Qt version %{version}.

%description examples -l pl
Æwiczenia/przyk³ady do Qt.

%description examples -l pt_BR
Programas exemplo para o Qt versão %{version}.

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

%package utils
Summary:	QT Utils
Summary(pl):	Narzêdzia QT
Group:		X11/Development/Tools
Requires:	%{name}-devel = %{version}

%description utils
QT Development Utilities.

%description utils -l pl
Narzedzia programistyczne QT.

%prep
%setup -q -n %{name}-copy
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

rm -rf `find . -name CVS`

# There is no file pointed by this sym-link and there is cp -L in %%install
rm -f include/qt_windows.h

%build
QTDIR=`/bin/pwd`; export QTDIR
LD_LIBRARY_PATH="$QTDIR/lib" ; export LD_LIBRARY_PATH
PATH="$QTDIR/bin:$PATH"

# change QMAKE_CFLAGS_RELEASE to build properly optimized libs
perl -pi -e "
	s|-O2|%{rpmcflags}|;
	" mkspecs/linux-g++/qmake.conf

DEFAULTOPT="-prefix %{_prefix} -docdir %{_docdir}/%{name}-doc-%{version} \
	    -datadir %{_datadir}/qt -headerdir %{_includedir}\
	    -qt-gif -system-zlib -no-g++-exceptions -stl \
	    -no-exceptions \
	    -system-libpng -system-libjpeg -system-libmng -sm -xinerama \
	    -xrender -xft -xkb -enable-opengl"
%{?_with_nas:DEFAULTOPT="$DEFAULTOPT -system-nas-sound"}
%{?_without_cups:DEFAULTOPT="$DEFAULTOPT -no-cups"}
%{?debug:DEFAULTOPT="$DEFAULTOPT -debug"}
%{!?debug:DEFAULTOPT="$DEFAULTOPT -release"}
	
STYLESLIST="cde compact motif motifplus platinum sgi windows"
%{__make} -f Makefile.cvs
########################################################################
# STATIC SINGLE-THREAD
########################################################################
%if %{?_with_static:%{?_with_single:1}}0
DEFAULTSTYLES=""
for i in $STYLESLIST; do
	DEFAULTSTYLES="$DEFAULTSTYLES -qt-style-$i"
done

OPTFLAGS="%{rpmcflags}" \
./configure \
	$DEFAULTOPT \
	-no-thread \
	-fast \
	-static \
	-qt-imgfmt-png \
	-qt-imgfmt-jpeg \
	-qt-imgfmt-mng \
	%{!?_without_mysql:-qt-sql-mysql} \
	%{!?_without_odbc:-qt-sql-odbc} \
	%{!?_without_pgsql:-qt-sql-psql} \
	$DEFAULTSTYLES \
	-no-style-windowsxp \
	<<_EOF_
yes
_EOF_

# Build libraries and everything needed to do this. Do not build examples and
# such. They will be built with shared, sigle-thread libraries.
%{__make} symlinks src-qmake src-moc sub-src
%{__make} clean
%endif # _with_single_static
########################################################################
# STATIC MULTI-THREAD
########################################################################
%if %{?_with_static:1}0

# This will not remove previously compiled libraries.

OPTFLAGS="%{rpmcflags}" \
./configure \
	$DEFAULTOPT \
	-thread \
	-static \
	-fast\
	-qt-imgfmt-png \
	-qt-imgfmt-jpeg \
	-qt-imgfmt-mng \
	%{!?_without_mysql:-qt-sql-mysql} \
	%{!?_without_odbc:-qt-sql-odbc} \
	%{!?_without_pgsql:-qt-sql-psql} \
	$DEFAULTSTYLES \
	-no-style-windowsxp \
	<<_EOF_
yes
_EOF_

# Build libraries and everything needed to do this. Do not build examples and
# such. They will be built with shared, sigle-thread libraries.
%{__make} symlinks src-qmake src-moc sub-src
%endif #_with_static

########################################################################
# SHARED SINGLE-THREAD
########################################################################
%if %{?_with_single:1}0
DEFAULTSTYLES=""
for i in $STYLESLIST; do
	DEFAULTSTYLES="$DEFAULTSTYLES -plugin-style-$i"
done


# This will not remove previously compiled libraries.
%{?_with_static:%{__make} clean}

# workaround for some nasty bug to avoid linking plugins statically with -lqt-mt
rm -f lib/libqt-mt.prl

OPTFLAGS="%{rpmcflags}" \
./configure \
	$DEFAULTOPT \
	-fast \
	-no-thread \
	-shared \
	-plugindir %{_libdir}/qt/plugins-st \
	-plugin-imgfmt-png \
	-plugin-imgfmt-jpeg \
	-plugin-imgfmt-mng \
	%{!?_without_mysql:-plugin-sql-mysql} \
	%{!?_without_odbc:-plugin-sql-odbc} \
	%{!?_without_pgsql:-plugin-sql-psql} \
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
rm -rf plugins-st
mkdir plugins-st
cp -R plugins/{imageformats,styles} plugins-st
%{?_withsql:cp -R plugins/sqldrivers plugins-st}

%{__make} clean
%endif # without single
OPTFLAGS="%{rpmcflags}" \
./configure \
	$DEFAULTOPT \
	-thread \
	-shared \
	-plugindir %{_libdir}/qt/plugins-mt \
	-plugin-imgfmt-png \
	-plugin-imgfmt-jpeg \
	-plugin-imgfmt-mng \
	%{!?_without_mysql:-plugin-sql-mysql} \
	%{!?_without_odbc:-plugin-sql-odbc} \
	%{!?_without_pgsql:-plugin-sql-psql} \
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

rm -rf `find $RPM_BUILD_ROOT -name CVS`

install -d $RPM_BUILD_ROOT{%{_mandir}/man{1,3},%{_examplesdir}/%{name}/lib} \
	$RPM_BUILD_ROOT%{_libdir}/qt/plugins-{m,s}t/network
install bin/{findtr,qt20fix,qtrename140} \
	tools/msg2qm/msg2qm tools/mergetr/mergetr \
	$RPM_BUILD_ROOT%{_bindir}

install doc/man/man1/*		$RPM_BUILD_ROOT%{_mandir}/man1
install doc/man/man3/*		$RPM_BUILD_ROOT%{_mandir}/man3

%if %{?_with_static:1}0
install lib/libqt.a		$RPM_BUILD_ROOT%{_libdir}
install lib/libqt-mt.a		$RPM_BUILD_ROOT%{_libdir}
%endif

install lib/libqt.so.*.*.*	$RPM_BUILD_ROOT%{_libdir}
ln -sf libqt.so.%{_qt_sl} $RPM_BUILD_ROOT%{_libdir}/libqt.so

cp -R plugins-st/* $RPM_BUILD_ROOT%{_libdir}/qt/plugins-st/

cp -dpR .qmake.cache examples tutorial \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}
	
mv $RPM_BUILD_ROOT{%{_libdir}/*.prl,%{_examplesdir}/%{name}/lib}
mkdir $RPM_BUILD_ROOT%{_datadir}/qt/mkspecs/features

# Fix Makefiles for tutorial and examples. How people who made so cool
# library could screw build process so badly?
find $RPM_BUILD_ROOT%{_examplesdir}/%{name} -regex '.*/\(examples\|tutorial\).*/Makefile$' -exec \
	perl -pi -e '
		print "QTDIR    = %{_prefix}\n" if $. == 1;
		s|(-I\$\(QTDIR\)/include)|$1/qt|g;
		s|(\$\(QTDIR\))(/mkspecs)|$1/share/qt$2|g;
		s|'$QTDIR'|%{_prefix}|g;
	' {} \;

perl -pi -e "
	s|(QMAKE_INCDIR_QT\\s*=\\s*\\\$\\(QTDIR\\)/include)|\$1/qt|
	" $RPM_BUILD_ROOT/%{_datadir}/qt/mkspecs/linux-g++/qmake.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc FAQ LICENSE.* README* changes*
%attr(755,root,root) %{_libdir}/libdesigner.so.*
%attr(755,root,root) %{_libdir}/libeditor.so.*
%attr(755,root,root) %{_libdir}/libqassistantclient.so.*
%if %{?_with_single:1}0
%attr(755,root,root) %{_libdir}/libqt.so.*
%dir %{_libdir}/%{name}/plugins-st
%dir %{_libdir}/%{name}/plugins-st/imageformats
%dir %{_libdir}/%{name}/plugins-st/network
%dir %{_libdir}/%{name}/plugins-st/styles
%{?_withsql:%dir %{_libdir}/%{name}/plugins-st/sqldrivers}
%attr(755,root,root) %{_libdir}/%{name}/plugins-st/imageformats/*.so
%attr(755,root,root) %{_libdir}/%{name}/plugins-st/styles/*.so
%endif
%attr(755,root,root) %{_libdir}/libqt-mt.so.*
%attr(755,root,root) %{_libdir}/libqui.so.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins-mt
%dir %{_libdir}/%{name}/plugins-mt/imageformats
%dir %{_libdir}/%{name}/plugins-mt/network
%dir %{_libdir}/%{name}/plugins-mt/styles
%if %{_withsql}
%dir %{_libdir}/%{name}/plugins-mt/sqldrivers
%endif
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/imageformats/*.so
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/styles/*.so
%dir %{_datadir}/qt

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/[!adl]*
%attr(755,root,root) %{_bindir}/l[!i]*
%{_libdir}/libdesigner.so
%{_libdir}/libeditor.so
%{_libdir}/libqassistantclient.so
%if %{?_with_single:1}0
%{_libdir}/libqt.so
%endif
%{_libdir}/libqt-mt.so
%{_libdir}/libqui.so
%{_includedir}
%{_datadir}/qt/[!d]*
%{_mandir}/man1/*

%if %{!?_without_static:1}%{?_without_static:0}
%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%endif

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-doc-%{version}

%files man
%defattr(644,root,root,755)
%{_mandir}/man3/*

%if %{!?_without_examples:1}%{?_without_examples:0}
%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
%endif

%if %{!?_without_mysql:1}%{?_without_mysql:0}
%files plugins-mysql
%defattr(644,root,root,755)
%{?_with_single:%attr(755,root,root) %{_libdir}/%{name}/plugins-st/sqldrivers/lib*mysql.so}
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/sqldrivers/lib*mysql.so
%endif

%if %{!?_without_pgsql:1}%{?_without_pgsql:0}
%files plugins-psql
%defattr(644,root,root,755)
%{?_with_single:%attr(755,root,root) %{_libdir}/%{name}/plugins-st/sqldrivers/lib*psql.so}
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/sqldrivers/lib*psql.so
%endif

%if %{!?_without_odbc:1}%{?_without_odbc:0}
%files plugins-odbc
%defattr(644,root,root,755)
%{?_with_single:%attr(755,root,root) %{_libdir}/%{name}/plugins-st/sqldrivers/lib*odbc.so}
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/sqldrivers/lib*odbc.so
%endif

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/[ad]*
%attr(755,root,root) %{_bindir}/li*
%dir %{_libdir}/%{name}/plugins*/designer
%attr(755,root,root) %{_libdir}/%{name}/plugins*/designer/*.so
%{_datadir}/qt/designer
