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
%bcond_without	ibase		# build ibase (InterBase/Firebird) plugin
%bcond_with	pch		# enable pch in qmake
#
%ifnarch %{ix86} amd64 sparc sparcv9 alpha ppc
%undefine	with_ibase
%endif
%define		_withsql	1
%{!?with_sqlite:%{!?with_ibase:%{!?with_mysql:%{!?with_pgsql:%{!?with_odbc:%undefine _withsql}}}}}

%define		_ver		3.3.3

Summary:	The Qt3 GUI application framework
Summary(es):	Biblioteca para ejecutar aplicaciones GUI Qt
Summary(pl):	Biblioteka Qt3 do tworzenia GUI
Summary(pt_BR):	Estrutura para rodar aplicações GUI Qt
Name:		qt
#Version:	%{_ver}.%{_snap}
Version:	%{_ver}
Release:	4
Epoch:		6
License:	GPL/QPL
Group:		X11/Libraries
#Source0:	http://ep09.pld-linux.org/~%{_packager}/kde/%{name}-copy-%{_snap}.tar.bz2
Source0:	ftp://ftp.trolltech.com/qt/source/%{name}-x11-free-%{version}.tar.bz2
# Source0-md5:	3e0a0c8429b0a974b39b5f535ddff01c
Source1:	http://ftp.pld-linux.org/software/kde/%{name}-copy-patches-040819.tar.bz2
# Source1-md5:	f35f461463d89f7b035530d8d1f02ad6
Source2:	%{name}config.desktop
Source3:	designer.desktop
Source4:	assistant.desktop
Source5:	linguist.desktop
Source6:	%{name}-apply_patches.sh
Patch0:		%{name}-tools.patch
Patch1:		%{name}-FHS.patch
Patch2:		%{name}-qmake-nostatic.patch
Patch3:		%{name}-disable_tutorials.patch
Patch4:		%{name}-locale.patch
Patch5:		%{name}-make_use_of_locale.patch
Patch6:		%{name}-qmake-opt.patch
Patch7:		%{name}-locale-charmap.patch
Patch8:		%{name}-gcc34.patch
# for troll only
Patch10:	%{name}-antialias.patch
#
Patch12:	%{name}-x11-free-quiet.patch
Patch13:	%{name}-x11-mono.patch
Patch14:	%{name}-x11-qfontdatabase_x11.patch
URL:		http://www.trolltech.com/products/qt/
Icon:		qt.xpm
%{?with_ibase:BuildRequires:	Firebird-devel >= 1.5.0}
BuildRequires:	OpenGL-devel
%{?with_nvidia:BuildRequires:	X11-driver-nvidia-devel >= 1.0.6111-2}
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
#Requires:	xft
#Requires:	xcursor
#Requires:	xrender
Requires:	freetype >= 2.0.0
#Requires:	libjpeg
Requires:	libmng >= 1.0.0
#Requires:	libpng
Requires:	OpenGL
Obsoletes:	qt-extensions
Obsoletes:	qt-utils
Conflicts:	kdelibs <= 8:3.2-0.030602.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

# <begin main library description>

%description
Qt is a complete C++ application development framework, which includes
a class library and tools for multiplatform development and
internationalization. Using Qt, a single source code tree can build
applications that run natively on different platforms (Windows,
Unix/Linux, Mac OS X, embedded Linux).

Qt has a rich set of standard widgets, and lets you write custom
controls. It encapsulates four different platform-specific APIs, and
the APIs for file-handling, networking, process-handling, threading,
database access, etc. Qt now also has Motif migration support and
Netscape LiveConnect plugin.

This package contains the shared, multi-threaded, Linux version of the
Qt library, the style plugins and translation files for Qt. Please
install qt-st if you need the single-threaded version of this library
(which isn't usually necessary).

%description -l es
Qt es un completo framework de desarrollo de aplicaciones en C++, el
que incluye una biblioteca de clases y unas herramientas para el
desarrollo multiplataforma e internacionalizado. Usando Qt, un
genérico árbol de código fuente se puede usar para construir
aplicaciones que puedan ejecutarse nativamente en varias plataformas
(Windows, Unix/Linux, Mac OS X, Linux embebido).

Qt provee un rico conjunto de componentes estándares y le permite
escribir unos propios. Encapsula cuatro APIs diferentes dependientes
de la plataforma y también APIs para el manejo de ficheros, la red, el
manejo de los procesos e hilos, acceso a bases de datos, etc. También
está incluido soporte de migración de Motif y un plugin para Netscape
LiveConnect.

Este paquete contiene la versión compartida multi-hilvanada de la
biblioteca Qt, los plugin de estilo y ficheros de traducción para Qt.
Instálese qt-st si necesita la versión mono-hilvanada de esta
biblioteca (lo cual normalmente no es necesario).

%description -l pl
Qt oferuje kompletny system do tworzenia i rozwijania aplikacji w
jêzyku C++, w którego sk³ad wchodzi biblioteka z klasami oraz
wieloplatformowymi narzêdziami do rozwijania i t³umaczenia aplikacji.
Z pomoc± Qt jeden kod ¼ród³owy mo¿e byæ natywnie uruchamiany na
ró¿nych platformach (Windows, Unix/Linux, Mac OS X).

Qt ma bogaty zbiór standardowych elementów interfejsu graficznego, ale
pozwala równie¿ na pisanie w³asnych elementów. £±czy w sposób
niewidoczny dla programisty interfejsy programowania ró¿nych systemów,
tworz±c w ten sposób jeden interfejs dla obs³ugi plików, sieci,
procesów, w±tków, baz danych itp. Umo¿liwia tak¿e ³atwe przenoszenie
na Qt aplikacji korzystaj±cych z Motif oraz pisanie wtyczek z
wykorzystaniem Netscape LiveConnect.

Ten pakiet zawiera wspó³dzielon±, wielow±tkow±, linuksow± wersjê
biblioteki Qt, wtyczki ze stylami oraz pliki t³umaczeñ Qt. Zainstaluj
qt-st je¶li potrzebujesz wersji jednow±tkowej tej biblioteki (co
zwykle nie jest konieczne).

%description -l pt_BR
Contém as bibliotecas compartilhadas necessárias para rodar aplicações
Qt, bem como os arquivos README.

%package devel
Summary:	Development files for the Qt GUI toolkit
Summary(es):	Archivos de inclusión necesaria para compilar aplicaciones Qt
Summary(pl):	Pliki nag³ówkowe, przyk³ady i dokumentacja do biblioteki
Summary(pt_BR):	Arquivos de inclusão necessária para compilar aplicações Qt
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	OpenGL-devel
Requires:	freetype-devel >= 2.0.0
Requires:	libjpeg-devel
Requires:	libmng-devel >= 1.0.0
Requires:	libpng-devel
Requires:	libstdc++-devel
Requires:	xcursor-devel
Requires:	xft-devel
Requires:	xrender-devel
Conflicts:	qt2-devel

%description devel
This package contains the Qt development tools: the metaobjects
compiler (moc) and the user interface compiler (uic); Qt include
files, pkgconfig helpers and tools for preserving compatibility
between versions of Qt.

%description devel -l pl
Ten pakiet zawiera narzêdzia programistyczne Qt: kompilator
metaobiektów (moc), kompilator interfejsu u¿ytkownika (uic); pliki
nag³ówkowe, wsparcie dla pkgconfig oraz narzêdzia u³atwiaj±ce
zachowanie kompatybilno¶ci niezale¿nie od wersji Qt.

%package static
Summary:	Qt static library
Summary(pl):	Biblioteka statyczna Qt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Qt is a complete C++ application development framework, which includes
a class library and tools for multiplatform development and
internationalization. Using Qt, a single source code tree can build
applications that run natively on different platforms (Windows,
Unix/Linux, Mac OS X, embedded Linux).

Qt has a rich set of standard widgets, and lets you write custom
controls. It encapsulates four different platform-specific APIs, and
the APIs for file-handling, networking, process-handling, threading,
database access, etc. Qt now also has Motif migration oraz Netscape
LiveConnect plugin.

This package contains the static, multi-threaded, linux version of the
Qt library.

%description static -l pl
Qt oferuje kompletny system do tworzenia i rozwijania aplikacji w
jêzyku C++, w którego sk³ad wchodzi biblioteka z klasami oraz
wieloplatformowymi narzêdziami do rozwijania i t³umaczenia aplikacji.
Z pomoc± Qt jeden kod ¼ród³owy mo¿e byæ natywnie uruchamiany na
ró¿nych platformach (Windows, Unix/Linux, Mac OS X).

Qt ma bogaty zbiór standardowych elementów interfejsu graficznego, ale
pozwala równie¿ na pisanie w³asnych elementów. £±czy w sposób
niewidoczny dla programisty interfejsy programowania ró¿nych systemów,
tworz±c w ten sposób jeden interfejs dla obs³ugi plików, sieci,
procesów, w±tków, baz danych itp. Umo¿liwia tak¿e ³atwe przenoszenie
na Qt aplikacji korzystaj±cych z Motif oraz pisanie wtyczek z
wykorzystaniem Netscape LiveConnect.

Ten pakiet zawiera statyczn±, wielow±tkow±, linuksow± wersjê
biblioteki Qt.

%package doc
Summary:	Qt Documentation in HTML format
Summary(pl):	Dokumentacja Qt w formacie HTML
Group:		X11/Development/Libraries
Obsoletes:	qt-doc-html

%description doc
Qt documentation in HTML format.

%description doc -l pl
Dokumentacja qt w formacie HTML.

%package man
Summary:	Qt man pages
Summary(pl):	Qt - strony man
Group:		X11/Development/Libraries
Obsoletes:	qt-doc-man

%description man
Qt documentation in man pages format.

%description man -l pl
Dokumentacja Qt w formacie stron man.

%package examples
Summary:	Example programs bundled with Qt
Summary(pl):	Æwiczenia i przyk³ady do Qt
Summary(pt_BR):	Programas exemplo desenvolvidos com o Qt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description examples
Example programs bundled with Qt version.

%description examples -l pl
Æwiczenia/przyk³ady do³±czone do Qt.

%description examples -l pt_BR
Programas exemplo para o Qt versão.

# <end main library desc>

# <start multithreaded plugins desc>

%package plugin-ibase
Summary:	Database plugin for InterBase/Firebird Qt support
Summary(pl):	Wtyczka InterBase/Firebird do Qt
Summary(pt_BR):	Plugin de suporte a InterBase/Firebird para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	Firebird-lib >= 1.5.0
Provides:	%{name}-plugin-sql = %{epoch}:%{version}-%{release}

%description plugin-ibase
This package contains a multi-thread enabled plugin for accessing
Interbase/Firebird database via the QSql classes.

%description plugin-ibase -l pl
Ten pakiet zawiera wielow±tkow± wersjê wtyczki do Qt umo¿liwiaj±cej
korzystanie z baz danych Interbase/Firebird poprzez klasy QSql.

%description plugin-ibase -l pt_BR
Plugin de suporte a InterBase/Firebird para Qt.

%package plugin-mysql
Summary:	Database plugin for MySQL Qt support
Summary(pl):	Wtyczka MySQL do Qt
Summary(pt_BR):	Plugin de suporte a MySQL para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
#Requires:	mysql-libs
Provides:	%{name}-plugin-sql = %{epoch}:%{version}-%{release}
Obsoletes:	qt-plugins-mysql

%description plugin-mysql
This package contains a multi-thread enabled plugin for accessing
MySQL database via the QSql classes.

%description plugin-mysql -l pl
Ten pakiet zawiera wielow±tkow± wersjê wtyczki do Qt umo¿liwiaj±cej
korzystanie z baz danych MySQL poprzez klasy QSql.

%description plugin-mysql -l pt_BR
Plugin de suporte a MySQL para Qt.

%package plugin-odbc
Summary:	Database plugin for ODBC Qt support
Summary(pl):	Wtyczka ODBC do Qt
Summary(pt_BR):	Plugin de suporte a ODBC para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
#Requires:	unixODBC
Provides:	%{name}-plugin-sql = %{epoch}:%{version}-%{release}
Obsoletes:	qt-plugins-odbc

%description plugin-odbc
This package contains a multi-thread enabled plugin for accessing
unixODBC services via the QSql classes.

%description plugin-odbc -l pl
Ten pakiet zawiera wielow±tkow± wersjê wtyczki do Qt umo¿liwiaj±cej
korzystanie z us³ug unixODBC poprzez klasy QSql.

%description plugin-odbc -l pt_BR
Plugin de suporte a ODBC para Qt.

%package plugin-psql
Summary:	Database plugin for PostgreSQL Qt support
Summary(pl):	Wtyczka PostgreSQL do Qt
Summary(pt_BR):	Plugin de suporte a PostgreSQL para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
#Requires:	postgresql-libs
Provides:	%{name}-plugin-sql = %{epoch}:%{version}-%{release}
Obsoletes:	qt-plugins-psql

%description plugin-psql
This package contains a multi-thread enabled plugin for accessing
PostgreSQL database via the QSql classes.

%description plugin-psql -l es
Plugin de suporte a PostgreSQL para Qt.

%description plugin-psql -l pl
Ten pakiet zawiera wielow±tkow± wersjê wtyczki do Qt umo¿liwiaj±cej
korzystanie z baz danych PostgreSQL poprzez klasy QSql.

%package plugin-sqlite
Summary:	Database plugin for SQLite Qt support
Summary(pl):	Wtyczka SQLite do Qt
Summary(pt_BR):	Plugin de suporte a SQLite para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
#Requires:	sqlite
Provides:	%{name}-plugin-sql = %{epoch}:%{version}-%{release}

%description plugin-sqlite
This package contains a multi-thread enabled plugin for using the
SQLite library (which allows to acces virtually any SQL database) via
the QSql classes.

%description plugin-sqlite -l pl
Ten pakiet zawiera wielow±tkow± wersjê wtyczki do Qt umo¿liwiaj±cej
korzystanie z baz danych PostgreSQL poprzez klasy QSql.

%description plugin-sqlite -l pt_BR
Plugin de suporte a SQLite para Qt.

# <end multithreaded plugins desc>

# <begin single threaded desc>

%package st
Summary:	Single-threaded Qt library
Summary(pl):	Jednow±tkowa wersja biblioteki Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description st
Qt is a complete C++ application development framework, which includes
a class library and tools for multiplatform development and
internationalization. Using Qt, a single source code tree can build
applications that run natively on different platforms (Windows,
Unix/Linux, Mac OS X, embedded Linux).

Qt has a rich set of standard widgets, and lets you write custom
controls. It encapsulates four different platform-specific APIs, and
the APIs for file-handling, networking, process-handling, threading,
database access, etc. Qt now also has Motif migration oraz Netscape
LiveConnect plugin.

This package contains the shared, single-threaded, linux version of
the Qt library and single-threaded styles for Qt. This version is
deprecated, please do not install it unless you explicitly need to.

%description st -l pl
Qt oferuje kompletny system do tworzenia i rozwijania aplikacji w
jêzyku C++, w którego sk³ad wchodzi biblioteka z klasami oraz
wieloplatformowymi narzêdziami do rozwijania i t³umaczenia aplikacji.
Z pomoc± Qt jeden kod ¼ród³owy mo¿e byæ natywnie uruchamiany na
ró¿nych platformach (Windows, Unix/Linux, Mac OS X).

Qt ma bogaty zbiór standardowych elementów interfejsu graficznego, ale
pozwala równie¿ na pisanie w³asnych elementów. £±czy w sposób
niewidoczny dla programisty interfejsy programowania ró¿nych systemów,
tworz±c w ten sposób jeden interfejs dla obs³ugi plików, sieci,
procesów, w±tków, baz danych itp. Umo¿liwia tak¿e ³atwe przenoszenie
na Qt aplikacji korzystaj±cych z Motif oraz pisanie wtyczek z
wykorzystaniem Netscape LiveConnect.

Ten pakiet zawiera wspó³dzielon±, jednow±tkow±, linuksow± wersjê
biblioteki Qt oraz jednow±tkowe wtyczki ze stylami. Ta wersja nie jest
ju¿ wspierana i nie zaleca siê jej instalowania bez wyra¼nej potrzeby.

%package st-devel
Summary:	Development files for single-threaded Qt library
Summary(pl):	Pliki programistyczne dla jednow±tkowej biblioteki Qt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-st = %{epoch}:%{version}-%{release}

%description st-devel
This package contains the single threaded

%description st-devel -l pl
Pliki programistyczne dla jednow±tkowej biblioteki Qt.

%package st-static
Summary:	Single-threaded Qt static libraries
Summary(pl):	Jednow±tkowa statyczna biblioteka Qt
Group:		X11/Development/Libraries
Requires:	%{name}-st-devel = %{epoch}:%{version}-%{release}

%description st-static
Qt is a complete C++ application development framework, which includes
a class library and tools for multiplatform development and
internationalization. Using Qt, a single source code tree can build
applications that run natively on different platforms (Windows,
Unix/Linux, Mac OS X, embedded Linux).

Qt has a rich set of standard widgets, and lets you write custom
controls. It encapsulates four different platform-specific APIs, and
the APIs for file-handling, networking, process-handling, threading,
database access, etc. Qt now also has Motif migration oraz Netscape
LiveConnect plugin.

This package contains the static, single-threaded, linux version of
the Qt library and single-threaded styles for Qt. This version is
deprecated, please do not install it unless you explicitly need to.

%description st-static -l pl
Qt oferuje kompletny system do tworzenia i rozwijania aplikacji w
jêzyku C++, w którego sk³ad wchodzi biblioteka z klasami oraz
wieloplatformowymi narzêdziami do rozwijania i t³umaczenia aplikacji.
Z pomoc± Qt jeden kod ¼ród³owy mo¿e byæ natywnie uruchamiany na
ró¿nych platformach (Windows, Unix/Linux, Mac OS X).

Qt ma bogaty zbiór standardowych elementów interfejsu graficznego, ale
pozwala równie¿ na pisanie w³asnych elementów. £±czy w sposób
niewidoczny dla programisty interfejsy programowania ró¿nych systemów,
tworz±c w ten sposób jeden interfejs dla obs³ugi plików, sieci,
procesów, w±tków, baz danych itp. Umo¿liwia tak¿e ³atwe przenoszenie
na Qt aplikacji korzystaj±cych z Motif oraz pisanie wtyczek z
wykorzystaniem Netscape LiveConnect.

Ten pakiet zawiera wspó³dzielon±, jednow±tkow±, linuksow± wersjê
biblioteki Qt oraz jednow±tkowe wtyczki ze stylami. Ta wersja nie jest
ju¿ wspierana i nie zaleca siê jej instalowania bez wyra¼nej potrzeby.

%package st-plugin-ibase
Summary:	Database plugin for InterBase/Firebird support in single-threaded Qt
Summary(pl):	Wtyczka InterBase/Firebird do jednow±tkowej wersji Qt
Group:		X11/Libraries
Requires:	%{name}-st = %{epoch}:%{version}-%{release}
Requires:	Firebird-lib >= 1.5.0
Provides:	%{name}-st-plugin-sql = %{epoch}:%{version}-%{release}

%description st-plugin-ibase
This package contains a single-thread plugin for accessing
InterBase/Firebird database via the QSql classes.

%description st-plugin-ibase -l pl
Ten pakiet zawiera jednow±tkow± wersjê wtyczki do Qt umo¿liwiaj±cej
korzystanie z baz danych InterBase/Firebird poprzez klasy QSql.

%package st-plugin-mysql
Summary:	Database plugin for MySQL support in single-threaded Qt
Summary(pl):	Wtyczka MySQL do jednow±tkowej wersji Qt
Group:		X11/Libraries
Requires:	%{name}-st = %{epoch}:%{version}-%{release}
#Requires:	mysql-libs
Provides:	%{name}-st-plugin-sql = %{epoch}:%{version}-%{release}

%description st-plugin-mysql
This package contains a single-thread plugin for accessing MySQL
database via the QSql classes.

%description st-plugin-mysql -l pl
Ten pakiet zawiera jednow±tkow± wersjê wtyczki do Qt umo¿liwiaj±cej
korzystanie z baz danych MySQL poprzez klasy QSql.

%package st-plugin-odbc
Summary:	Database plugin for ODBC support in single-threaded Qt
Summary(pl):	Wtyczka ODBC do jednow±tkowej wersji Qt
Group:		X11/Libraries
Requires:	%{name}-st = %{epoch}:%{version}-%{release}
#Requires:	unixODBC
Provides:	%{name}-st-plugin-sql = %{epoch}:%{version}-%{release}

%description st-plugin-odbc
This package contains a single-thread enabled plugin for accessing
unixODBC services via the QSql classes.

%description st-plugin-odbc -l pl
Ten pakiet zawiera jednow±tkow± wersjê wtyczki do Qt umo¿liwiaj±cej
korzystanie z us³ug unixODBC poprzez klasy QSql.

%package st-plugin-psql
Summary:	Database plugin for PostgreSQL support in single-threaded Qt
Summary(pl):	Wtyczka PostgreSQL do jednow±tkowej wersji Qt
Summary(pt_BR):	Plugin de suporte a PostgreSQL para Qt
Group:		X11/Libraries
Requires:	%{name}-st = %{epoch}:%{version}-%{release}
#Requires:	postgresql-libs
Provides:	%{name}-st-plugin-sql = %{epoch}:%{version}-%{release}

%description st-plugin-psql
This package contains a single-thread plugin for accessing PostgreSQL
database via the QSql classes.

%description st-plugin-psql -l pl
Ten pakiet zawiera jednow±tkow± wersjê wtyczki do Qt umo¿liwiaj±cej
korzystanie z baz danych PostgreSQL poprzez klasy QSql.

%package st-plugin-sqlite
Summary:	Database plugin for SQLite support in single-threaded Qt
Summary(pl):	Wtyczka SQLite do jednow±tkowej wersji Qt
Group:		X11/Libraries
Requires:	%{name}-st = %{epoch}:%{version}-%{release}
#Requires:	sqlite
Provides:	%{name}-st-plugin-sql = %{epoch}:%{version}-%{release}

%description st-plugin-sqlite
This package contains a single-thread plugin for using the SQLite
library (which allows to acces virtually any SQL database)

%description st-plugin-sqlite -l pl
Ten pakiet zawiera jednow±tkow± wersjê wtyczki do Qt umo¿liwiaj±cej
korzystanie z baz danych PostgreSQL poprzez klasy QSql.

%package linguist
Summary:	Translation helper for Qt
Summary(pl):	Aplikacja u³atwiaj±ca t³umaczenie aplikacji oparty o Qt
Group:		X11/Development/Tools
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	qt-devel < 6:3.3.2-3

%description linguist
This program provides an interface that shortens and helps systematize
the process of translating GUIs. Qt Linguist takes all of the text of
a UI that will be shown to the user, and presents it to a human
translator in a simple window. When one UI text is translated, the
program automatically progresses to the next, until they are all
completed.

%description linguist -l pl
Ten program oferuje interfejs znacznie przy¶pieszaj±cy proces
t³umaczenia interfejsu u¿ytkownika. Zbiera wszystkie teksty
przeznaczone do t³umaczenia i przedstawia w ³atwym w obs³udze oknie.
Gdy jeden z nich jest ju¿ przet³umaczony, automatycznie przechodzi do
nastêpnego, a¿ wszystkie bêd± przet³umaczone.

%package assistant
Summary:	Qt documentation browser
Summary(pl):	Przegl±darka dokumentacji Qt
Group:		X11/Development/Tools
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-doc
Conflicts:	qt-devel < 6:3.3.2-3

%description assistant
Qt Assistant is a tool for browsing on-line documentation with
indexing, bookmarks and full-text search.

%description assistant -l pl
Qt Assistant to narzêdzie do przegl±dania dokumentacji z mo¿liwo¶ci±
indeksowania, dodawania zak³adek i pe³notekstowego wyszukiwania.

%package -n qmake
Summary:	Qt makefile generator
Summary(pl):	Generator plików makefile dla aplikacji Qt
Group:		X11/Development/Tools
Conflicts:	qt-devel < 6:3.3.2-3

%description -n qmake
A powerful makefile generator. It can create makefiles on any platform
from a simple .pro definitions file.

%description -n qmake -l pl
Rozbudowany generator plików makefile. Potrafi tworzyæ pliki makefile
na ka¿dej platformi na podstawie ³atwego w przygotowaniu pliku .pro.

%package -n qtconfig
Summary:	Qt widgets configuration tool
Summary(pl):	Narzêdzie do konfigurowania widgetów Qt
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n qtconfig
A tool for configuring look and behavior of Qt widgets.

%description -n qtconfig -l pl
Narzêdie do konfiguracji wygl±du i zachowania widgetów Qt.

%package designer
Summary:	IDE used for GUI designing with Qt library
Summary(pl):	IDE s³u¿±ce do projektowania GUI za pomoc± biblioteki Qt
Group:		X11/Applications
Requires:	%{name}-designer-libs = %{epoch}:%{version}-%{release}

%description designer
An advanced tool used for GUI designing with Qt library.

%description designer -l pl
Zaawansowane narzêdzie s³u¿±ce do projektowania interfejsu graficznego
za pomoc± biblioteki Qt.

%package designer-libs
Summary:	Libraries IDE used for GUI designing with Qt library
Summary(pl):	Biblioteki do IDE s³u¿±cego do projektowania GUI za pomoc± biblioteki Qt
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description designer-libs
Libraries used by the Qt GUI Designer.

%description designer-libs -l pl
Biblioteki wykorzystywane przez narzêdzie projektowania interfejsu
graficznego - Qt Designer.

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
%patch10 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

install %{SOURCE6} ./apply_patches
chmod +x ./apply_patches
./apply_patches

# change QMAKE_CFLAGS_RELEASE to build
# properly optimized libs
plik="mkspecs/linux-g++/qmake.conf"

perl -pi -e "
	s|QMAKE_CC.*=.*gcc|QMAKE_CC = %{__cc}|;
	s|QMAKE_CXX.*=.*g\+\+|QMAKE_CXX = %{__cxx}|;
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
	%{?with_pch:-pch} \
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
cd $QTDIR/translations/
for i in *.ts ;
do
	LD_PRELOAD=$QTDIR/%{_lib}/libqt-mt.so.3 lrelease ${i}
done
cd -

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

install %{SOURCE4} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}

%if %{without designer}
install bin/uic $RPM_BUILD_ROOT%{_bindir}
%endif

# Because trolltech fails to think.
rm -rf $RPM_BUILD_ROOT%{_bindir}/qmake
install qmake/qmake $RPM_BUILD_ROOT%{_bindir}/qmake
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


cd $RPM_BUILD_ROOT%{_examplesdir}/%{name}/examples
for i in `find ./ -name Makefile`;
do

%{__sed} -i -e "s,$RPM_BUILD_DIR,/usr,g" $i
%{__sed} -i -e "s,examples,src/examples/qt/examples,g" $i

done

cd $RPM_BUILD_ROOT%{_examplesdir}/%{name}/tutorial
for i in `find ./ -name Makefile`;
do

%{__sed} -i -e "s,$RPM_BUILD_DIR,/usr,g" $i
%{__sed} -i -e "s,examples,src/examples/qt/tutorial,g" $i

done


%clean
rm -rf $RPM_BUILD_ROOT

%post		-p /sbin/ldconfig
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
%attr(755,root,root) %{_bindir}/moc
%attr(755,root,root) %{_bindir}/qt20fix
#%attr(755,root,root) %{_bindir}/qt32castcompat
%attr(755,root,root) %{_bindir}/qtrename140
%attr(755,root,root) %{_bindir}/uic
%{_includedir}/qt
%{_libdir}/libqassistantclient.so
%{_libdir}/libqt-mt.la
%{_libdir}/libqt-mt.so
%{_mandir}/man1/moc*
%{_mandir}/man1/uic*
%{_pkgconfigdir}/qt-mt.pc

%files -n qmake
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qmake
%{_datadir}/qt/mkspecs

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

%files assistant
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/assistant
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/assistant.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/assistant.qm
%{_desktopdir}/assistant.desktop

%files linguist
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/linguist
%attr(755,root,root) %{_bindir}/findtr
%attr(755,root,root) %{_bindir}/lrelease
%attr(755,root,root) %{_bindir}/lupdate
%attr(755,root,root) %{_bindir}/mergetr
%attr(755,root,root) %{_bindir}/qm2ts
%attr(755,root,root) %{_bindir}/msg2qm
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/linguist.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/linguist.qm
%{_desktopdir}/linguist.desktop
%{_datadir}/qt/phrasebooks
%{_mandir}/man1/l*
%{_mandir}/man1/*qm*

%files -n qtconfig
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtconfig
%{_desktopdir}/qtconfig.desktop
%{_pixmapsdir}/qtconfig.png
