# TODO: use system sqlite
#
# Conditional build:
%bcond_with	dlopen_gl	# dlopen libGL.so and libXmu.so instead of direct linking (NOTE: should dlopen by soname, not *.so like it does now!)
%bcond_with	nas		# enable NAS audio support
%bcond_with	single		# enable single-threaded libraries
%bcond_without	static_libs	# don't build static libraries
%bcond_without	cups		# disable CUPS support
%bcond_without	mysql		# don't build MySQL plugin
%bcond_without	odbc		# don't build unixODBC plugin
%bcond_without	pgsql		# don't build PostgreSQL plugin
%bcond_without	designer	# don't build designer (it takes long)
%bcond_without	sqlite		# don't build SQLite plugin
%bcond_without	ibase		# don't build ibase (InterBase/Firebird) plugin
%bcond_without	pch		# don't enable pch in qmake
#
%ifnarch %{ix86} %{x8664} x32 sparc sparcv9 alpha ppc
%undefine	with_ibase
%endif
%define		with_sql	1
%{!?with_sqlite:%{!?with_ibase:%{!?with_mysql:%{!?with_pgsql:%{!?with_odbc:%undefine with_sql}}}}}

%define		ver		3.3.8.d

Summary:	The Qt3 GUI application framework
Summary(es.UTF-8):	Biblioteca para ejecutar aplicaciones GUI Qt
Summary(pl.UTF-8):	Biblioteka Qt3 do tworzenia GUI
Summary(pt_BR.UTF-8):	Estrutura para rodar aplicações GUI Qt
Name:		qt
Version:	%{ver}
Release:	11
Epoch:		6
License:	QPL v1, GPL v2 or GPL v3
Group:		X11/Libraries
Source0:	http://mirror.ets.kth.se/trinity/releases/3.5.13/dependencies/qt3-%{version}.tar.gz
# Source0-md5:	78dc675e84aed595375449818cbb589a
Source1:	%{name}config.desktop
Source2:	designer.desktop
Source3:	assistant.desktop
Source4:	linguist.desktop
Source5:	designer.png
Source6:	assistant.png
Source7:	linguist.png
# generated using notes from kdebase-SuSE/qtkdeintegration/README
Source8:	qtkdeintegration_x11.cpp
Source9:	qtkdeintegration_x11_p.h
Patch1:		%{name}-FHS.patch
Patch2:		%{name}-qmake-nostatic.patch
Patch3:		%{name}-disable_tutorials.patch
Patch4:		%{name}-locale.patch
Patch5:		%{name}-make_use_of_locale.patch
Patch6:		%{name}-qmake-opt.patch
Patch7:		%{name}-locale-charmap.patch
Patch8:		%{name}-gcc34.patch
Patch9:		%{name}-support-cflags-with-commas.patch
# for troll only
Patch10:	%{name}-antialias.patch
Patch11:	%{name}-x11-free-quiet.patch
Patch12:	%{name}-fvisibility.patch
Patch13:	qt-buildkey-fixed.patch
Patch14:	%{name}-odbc.patch
Patch15:	qt-3.3.8.d-libpng15-1.patch
Patch16:	qsql.patch
Patch17:	%{name}-psql.patch
URL:		http://www.trolltech.com/products/qt/
%{?with_ibase:BuildRequires:	Firebird-devel >= 1.5.0}
BuildRequires:	OpenGL-GLU-devel
%{?with_cups:BuildRequires:	cups-devel}
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.9
%{?with_pch:BuildRequires:	gcc >= 5:3.4.0}
BuildRequires:	giflib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel >= 1.0.0
BuildRequires:	libpng-devel >= 2:1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtirpc-devel
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	perl-base
%{?with_pgsql:BuildRequires:	postgresql-backend-devel}
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	sed >= 4.0
%{?with_sqlite:BuildRequires:	sqlite-devel}
%{?with_odbc:BuildRequires:	unixODBC-devel}
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	zlib-devel
Requires:	freetype >= 2.0.9
Requires:	libmng >= 1.0.0
Obsoletes:	qt-extensions < 1:3
Obsoletes:	qt-utils < 6:3.3.3
Conflicts:	kdelibs <= 8:3.2-0.030602.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		Werror_cflags	%{nil}

%define		specflags	-fno-strict-aliasing

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

%description -l es.UTF-8
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

%description -l pl.UTF-8
Qt oferuje kompletny system do tworzenia i rozwijania aplikacji w
języku C++, w którego skład wchodzi biblioteka z klasami oraz
wieloplatformowymi narzędziami do rozwijania i tłumaczenia aplikacji.
Z pomocą Qt jeden kod źródłowy może być natywnie uruchamiany na
różnych platformach (Windows, Unix/Linux, Mac OS X).

Qt ma bogaty zbiór standardowych elementów interfejsu graficznego, ale
pozwala również na pisanie własnych elementów. Łączy w sposób
niewidoczny dla programisty interfejsy programowania różnych systemów,
tworząc w ten sposób jeden interfejs dla obsługi plików, sieci,
procesów, wątków, baz danych itp. Umożliwia także łatwe przenoszenie
na Qt aplikacji korzystających z Motif oraz pisanie wtyczek z
wykorzystaniem Netscape LiveConnect.

Ten pakiet zawiera współdzieloną, wielowątkową, linuksową wersję
biblioteki Qt, wtyczki ze stylami oraz pliki tłumaczeń Qt. Zainstaluj
qt-st jeśli potrzebujesz wersji jednowątkowej tej biblioteki (co
zwykle nie jest konieczne).

%description -l pt_BR.UTF-8
Contém as bibliotecas compartilhadas necessárias para rodar aplicações
Qt, bem como os arquivos README.

%package devel
Summary:	Development files for the Qt GUI toolkit
Summary(es.UTF-8):	Archivos de inclusión necesaria para compilar aplicaciones Qt
Summary(pl.UTF-8):	Pliki nagłówkowe, przykłady i dokumentacja do biblioteki
Summary(pt_BR.UTF-8):	Arquivos de inclusão necessária para compilar aplicações Qt
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%{!?with_dlopen_gl:Requires:	OpenGL-devel}
Requires:	freetype-devel >= 2.0.9
Requires:	libjpeg-devel
Requires:	libmng-devel >= 1.0.0
Requires:	libpng-devel
Requires:	libstdc++-devel
Requires:	xorg-lib-libSM-devel
Requires:	xorg-lib-libXcursor-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXft-devel
Requires:	xorg-lib-libXinerama-devel
Requires:	xorg-lib-libXmu-devel
Requires:	xorg-lib-libXrandr-devel
Requires:	xorg-lib-libXrender-devel
Requires:	zlib-devel
Conflicts:	qt2-devel

%description devel
This package contains the Qt development tools: the metaobjects
compiler (moc) and the user interface compiler (uic); Qt include
files, pkgconfig helpers and tools for preserving compatibility
between versions of Qt.

%description devel -l pl.UTF-8
Ten pakiet zawiera narzędzia programistyczne Qt: kompilator
metaobiektów (moc), kompilator interfejsu użytkownika (uic); pliki
nagłówkowe, wsparcie dla pkgconfig oraz narzędzia ułatwiające
zachowanie kompatybilności niezależnie od wersji Qt.

%package static
Summary:	Qt static library
Summary(pl.UTF-8):	Biblioteka statyczna Qt
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

%description static -l pl.UTF-8
Qt oferuje kompletny system do tworzenia i rozwijania aplikacji w
języku C++, w którego skład wchodzi biblioteka z klasami oraz
wieloplatformowymi narzędziami do rozwijania i tłumaczenia aplikacji.
Z pomocą Qt jeden kod źródłowy może być natywnie uruchamiany na
różnych platformach (Windows, Unix/Linux, Mac OS X).

Qt ma bogaty zbiór standardowych elementów interfejsu graficznego, ale
pozwala również na pisanie własnych elementów. Łączy w sposób
niewidoczny dla programisty interfejsy programowania różnych systemów,
tworząc w ten sposób jeden interfejs dla obsługi plików, sieci,
procesów, wątków, baz danych itp. Umożliwia także łatwe przenoszenie
na Qt aplikacji korzystających z Motif oraz pisanie wtyczek z
wykorzystaniem Netscape LiveConnect.

Ten pakiet zawiera statyczną, wielowątkową, linuksową wersję
biblioteki Qt.

%package doc
Summary:	Qt Documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja Qt w formacie HTML
Group:		X11/Development/Libraries
Obsoletes:	qt-doc-html < 6:3.2.1

%description doc
Qt documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja qt w formacie HTML.

%package man
Summary:	Qt man pages
Summary(pl.UTF-8):	Qt - strony man
Group:		X11/Development/Libraries
Obsoletes:	qt-doc-man < 6:3.1.2-5

%description man
Qt documentation in man pages format.

%description man -l pl.UTF-8
Dokumentacja Qt w formacie stron man.

%package examples
Summary:	Example programs bundled with Qt
Summary(pl.UTF-8):	Ćwiczenia i przykłady do Qt
Summary(pt_BR.UTF-8):	Programas exemplo desenvolvidos com o Qt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description examples
Example programs bundled with Qt version.

%description examples -l pl.UTF-8
Ćwiczenia/przykłady dołączone do Qt.

%description examples -l pt_BR.UTF-8
Programas exemplo para o Qt versão.

# <end main library desc>

# <start multithreaded plugins desc>

%package plugin-ibase
Summary:	Database plugin for InterBase/Firebird Qt support
Summary(pl.UTF-8):	Wtyczka InterBase/Firebird do Qt
Summary(pt_BR.UTF-8):	Plugin de suporte a InterBase/Firebird para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	Firebird-lib >= 1.5.0
Provides:	%{name}-plugin-sql = %{epoch}:%{version}-%{release}

%description plugin-ibase
This package contains a multi-thread enabled plugin for accessing
Interbase/Firebird database via the QSql classes.

%description plugin-ibase -l pl.UTF-8
Ten pakiet zawiera wielowątkową wersję wtyczki do Qt umożliwiającej
korzystanie z baz danych Interbase/Firebird poprzez klasy QSql.

%description plugin-ibase -l pt_BR.UTF-8
Plugin de suporte a InterBase/Firebird para Qt.

%package plugin-mysql
Summary:	Database plugin for MySQL Qt support
Summary(pl.UTF-8):	Wtyczka MySQL do Qt
Summary(pt_BR.UTF-8):	Plugin de suporte a MySQL para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-plugin-sql = %{epoch}:%{version}-%{release}
Obsoletes:	qt-plugins-mysql < 6:3.2.1

%description plugin-mysql
This package contains a multi-thread enabled plugin for accessing
MySQL database via the QSql classes.

%description plugin-mysql -l pl.UTF-8
Ten pakiet zawiera wielowątkową wersję wtyczki do Qt umożliwiającej
korzystanie z baz danych MySQL poprzez klasy QSql.

%description plugin-mysql -l pt_BR.UTF-8
Plugin de suporte a MySQL para Qt.

%package plugin-odbc
Summary:	Database plugin for ODBC Qt support
Summary(pl.UTF-8):	Wtyczka ODBC do Qt
Summary(pt_BR.UTF-8):	Plugin de suporte a ODBC para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-plugin-sql = %{epoch}:%{version}-%{release}
Obsoletes:	qt-plugins-odbc < 6:3.2.1

%description plugin-odbc
This package contains a multi-thread enabled plugin for accessing
unixODBC services via the QSql classes.

%description plugin-odbc -l pl.UTF-8
Ten pakiet zawiera wielowątkową wersję wtyczki do Qt umożliwiającej
korzystanie z usług unixODBC poprzez klasy QSql.

%description plugin-odbc -l pt_BR.UTF-8
Plugin de suporte a ODBC para Qt.

%package plugin-psql
Summary:	Database plugin for PostgreSQL Qt support
Summary(pl.UTF-8):	Wtyczka PostgreSQL do Qt
Summary(pt_BR.UTF-8):	Plugin de suporte a PostgreSQL para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-plugin-sql = %{epoch}:%{version}-%{release}
Obsoletes:	qt-plugins-psql < 6:3.2.1

%description plugin-psql
This package contains a multi-thread enabled plugin for accessing
PostgreSQL database via the QSql classes.

%description plugin-psql -l es.UTF-8
Plugin de suporte a PostgreSQL para Qt.

%description plugin-psql -l pl.UTF-8
Ten pakiet zawiera wielowątkową wersję wtyczki do Qt umożliwiającej
korzystanie z baz danych PostgreSQL poprzez klasy QSql.

%package plugin-sqlite
Summary:	Database plugin for SQLite Qt support
Summary(pl.UTF-8):	Wtyczka SQLite do Qt
Summary(pt_BR.UTF-8):	Plugin de suporte a SQLite para Qt
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	%{name}-plugin-sql = %{epoch}:%{version}-%{release}

%description plugin-sqlite
This package contains a multi-thread enabled plugin for using the
SQLite library (which allows to acces virtually any SQL database) via
the QSql classes.

%description plugin-sqlite -l pl.UTF-8
Ten pakiet zawiera wielowątkową wersję wtyczki do Qt umożliwiającej
korzystanie z baz danych PostgreSQL poprzez klasy QSql.

%description plugin-sqlite -l pt_BR.UTF-8
Plugin de suporte a SQLite para Qt.

# <end multithreaded plugins desc>

# <begin single threaded desc>

%package st
Summary:	Single-threaded Qt library
Summary(pl.UTF-8):	Jednowątkowa wersja biblioteki Qt
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

%description st -l pl.UTF-8
Qt oferuje kompletny system do tworzenia i rozwijania aplikacji w
języku C++, w którego skład wchodzi biblioteka z klasami oraz
wieloplatformowymi narzędziami do rozwijania i tłumaczenia aplikacji.
Z pomocą Qt jeden kod źródłowy może być natywnie uruchamiany na
różnych platformach (Windows, Unix/Linux, Mac OS X).

Qt ma bogaty zbiór standardowych elementów interfejsu graficznego, ale
pozwala również na pisanie własnych elementów. Łączy w sposób
niewidoczny dla programisty interfejsy programowania różnych systemów,
tworząc w ten sposób jeden interfejs dla obsługi plików, sieci,
procesów, wątków, baz danych itp. Umożliwia także łatwe przenoszenie
na Qt aplikacji korzystających z Motif oraz pisanie wtyczek z
wykorzystaniem Netscape LiveConnect.

Ten pakiet zawiera współdzieloną, jednowątkową, linuksową wersję
biblioteki Qt oraz jednowątkowe wtyczki ze stylami. Ta wersja nie jest
już wspierana i nie zaleca się jej instalowania bez wyraźnej potrzeby.

%package st-devel
Summary:	Development files for single-threaded Qt library
Summary(pl.UTF-8):	Pliki programistyczne dla jednowątkowej biblioteki Qt
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-st = %{epoch}:%{version}-%{release}

%description st-devel
This package contains the single threaded

%description st-devel -l pl.UTF-8
Pliki programistyczne dla jednowątkowej biblioteki Qt.

%package st-static
Summary:	Single-threaded Qt static libraries
Summary(pl.UTF-8):	Jednowątkowa statyczna biblioteka Qt
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

%description st-static -l pl.UTF-8
Qt oferuje kompletny system do tworzenia i rozwijania aplikacji w
języku C++, w którego skład wchodzi biblioteka z klasami oraz
wieloplatformowymi narzędziami do rozwijania i tłumaczenia aplikacji.
Z pomocą Qt jeden kod źródłowy może być natywnie uruchamiany na
różnych platformach (Windows, Unix/Linux, Mac OS X).

Qt ma bogaty zbiór standardowych elementów interfejsu graficznego, ale
pozwala również na pisanie własnych elementów. Łączy w sposób
niewidoczny dla programisty interfejsy programowania różnych systemów,
tworząc w ten sposób jeden interfejs dla obsługi plików, sieci,
procesów, wątków, baz danych itp. Umożliwia także łatwe przenoszenie
na Qt aplikacji korzystających z Motif oraz pisanie wtyczek z
wykorzystaniem Netscape LiveConnect.

Ten pakiet zawiera współdzieloną, jednowątkową, linuksową wersję
biblioteki Qt oraz jednowątkowe wtyczki ze stylami. Ta wersja nie jest
już wspierana i nie zaleca się jej instalowania bez wyraźnej potrzeby.

%package st-plugin-ibase
Summary:	Database plugin for InterBase/Firebird support in single-threaded Qt
Summary(pl.UTF-8):	Wtyczka InterBase/Firebird do jednowątkowej wersji Qt
Group:		X11/Libraries
Requires:	%{name}-st = %{epoch}:%{version}-%{release}
Requires:	Firebird-lib >= 1.5.0
Provides:	%{name}-st-plugin-sql = %{epoch}:%{version}-%{release}

%description st-plugin-ibase
This package contains a single-thread plugin for accessing
InterBase/Firebird database via the QSql classes.

%description st-plugin-ibase -l pl.UTF-8
Ten pakiet zawiera jednowątkową wersję wtyczki do Qt umożliwiającej
korzystanie z baz danych InterBase/Firebird poprzez klasy QSql.

%package st-plugin-mysql
Summary:	Database plugin for MySQL support in single-threaded Qt
Summary(pl.UTF-8):	Wtyczka MySQL do jednowątkowej wersji Qt
Group:		X11/Libraries
Requires:	%{name}-st = %{epoch}:%{version}-%{release}
Provides:	%{name}-st-plugin-sql = %{epoch}:%{version}-%{release}

%description st-plugin-mysql
This package contains a single-thread plugin for accessing MySQL
database via the QSql classes.

%description st-plugin-mysql -l pl.UTF-8
Ten pakiet zawiera jednowątkową wersję wtyczki do Qt umożliwiającej
korzystanie z baz danych MySQL poprzez klasy QSql.

%package st-plugin-odbc
Summary:	Database plugin for ODBC support in single-threaded Qt
Summary(pl.UTF-8):	Wtyczka ODBC do jednowątkowej wersji Qt
Group:		X11/Libraries
Requires:	%{name}-st = %{epoch}:%{version}-%{release}
Provides:	%{name}-st-plugin-sql = %{epoch}:%{version}-%{release}

%description st-plugin-odbc
This package contains a single-thread enabled plugin for accessing
unixODBC services via the QSql classes.

%description st-plugin-odbc -l pl.UTF-8
Ten pakiet zawiera jednowątkową wersję wtyczki do Qt umożliwiającej
korzystanie z usług unixODBC poprzez klasy QSql.

%package st-plugin-psql
Summary:	Database plugin for PostgreSQL support in single-threaded Qt
Summary(pl.UTF-8):	Wtyczka PostgreSQL do jednowątkowej wersji Qt
Summary(pt_BR.UTF-8):	Plugin de suporte a PostgreSQL para Qt
Group:		X11/Libraries
Requires:	%{name}-st = %{epoch}:%{version}-%{release}
Provides:	%{name}-st-plugin-sql = %{epoch}:%{version}-%{release}

%description st-plugin-psql
This package contains a single-thread plugin for accessing PostgreSQL
database via the QSql classes.

%description st-plugin-psql -l pl.UTF-8
Ten pakiet zawiera jednowątkową wersję wtyczki do Qt umożliwiającej
korzystanie z baz danych PostgreSQL poprzez klasy QSql.

%package st-plugin-sqlite
Summary:	Database plugin for SQLite support in single-threaded Qt
Summary(pl.UTF-8):	Wtyczka SQLite do jednowątkowej wersji Qt
Group:		X11/Libraries
Requires:	%{name}-st = %{epoch}:%{version}-%{release}
Provides:	%{name}-st-plugin-sql = %{epoch}:%{version}-%{release}

%description st-plugin-sqlite
This package contains a single-thread plugin for using the SQLite
library (which allows to acces virtually any SQL database)

%description st-plugin-sqlite -l pl.UTF-8
Ten pakiet zawiera jednowątkową wersję wtyczki do Qt umożliwiającej
korzystanie z baz danych PostgreSQL poprzez klasy QSql.

%package linguist
Summary:	Translation helper for Qt
Summary(pl.UTF-8):	Aplikacja ułatwiająca tłumaczenie aplikacji oparty o Qt
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

%description linguist -l pl.UTF-8
Ten program oferuje interfejs znacznie przyśpieszający proces
tłumaczenia interfejsu użytkownika. Zbiera wszystkie teksty
przeznaczone do tłumaczenia i przedstawia w łatwym w obsłudze oknie.
Gdy jeden z nich jest już przetłumaczony, automatycznie przechodzi do
następnego, aż wszystkie będą przetłumaczone.

%package assistant
Summary:	Qt documentation browser
Summary(pl.UTF-8):	Przeglądarka dokumentacji Qt
Group:		X11/Development/Tools
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-doc
Conflicts:	qt-devel < 6:3.3.2-3

%description assistant
Qt Assistant is a tool for browsing on-line documentation with
indexing, bookmarks and full-text search.

%description assistant -l pl.UTF-8
Qt Assistant to narzędzie do przeglądania dokumentacji z możliwością
indeksowania, dodawania zakładek i pełnotekstowego wyszukiwania.

%package -n qmake
Summary:	Qt makefile generator
Summary(pl.UTF-8):	Generator plików makefile dla aplikacji Qt
Group:		X11/Development/Tools
Conflicts:	qt-devel < 6:3.3.2-3

%description -n qmake
A powerful makefile generator. It can create makefiles on any platform
from a simple .pro definitions file.

%description -n qmake -l pl.UTF-8
Rozbudowany generator plików makefile. Potrafi tworzyć pliki makefile
na każdej platformie na podstawie łatwego w przygotowaniu pliku .pro.

%package -n qtconfig
Summary:	Qt widgets configuration tool
Summary(pl.UTF-8):	Narzędzie do konfigurowania widgetów Qt
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n qtconfig
A tool for configuring look and behavior of Qt widgets.

%description -n qtconfig -l pl.UTF-8
Narzędie do konfiguracji wyglądu i zachowania widgetów Qt.

%package designer
Summary:	IDE used for GUI designing with Qt library
Summary(pl.UTF-8):	IDE służące do projektowania GUI za pomocą biblioteki Qt
Group:		X11/Applications
Requires:	%{name}-designer-libs = %{epoch}:%{version}-%{release}

%description designer
An advanced tool used for GUI designing with Qt library.

%description designer -l pl.UTF-8
Zaawansowane narzędzie służące do projektowania interfejsu graficznego
za pomocą biblioteki Qt.

%package designer-libs
Summary:	Libraries IDE used for GUI designing with Qt library
Summary(pl.UTF-8):	Biblioteki do IDE służącego do projektowania GUI za pomocą biblioteki Qt
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description designer-libs
Libraries used by the Qt GUI Designer.

%description designer-libs -l pl.UTF-8
Biblioteki wykorzystywane przez narzędzie projektowania interfejsu
graficznego - Qt Designer.

%prep
%setup -q -n qt3
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p0
%patch -P13 -p1
%patch -P14 -p1
%patch -P15 -p1
%patch -P16 -p1
%patch -P17 -p1

# copy qt kde integration files
cp %{SOURCE8} %{SOURCE9} src/kernel
cp %{SOURCE9} include/private

# change QMAKE_CFLAGS_RELEASE to build
# properly optimized libs
cp mkspecs/linux-g++/qmake.conf{,.orig}
%{__sed} -i -e '
	s|/usr/lib|%{_libdir}|;
	s|/usr/X11R6/lib|/usr/%{_lib}|;
	s|/usr/X11R6/include|/usr/include|;
	s|(QTDIR)/lib|(QTDIR)/%{_lib}|;
	s|QMAKE_RPATH\s*=.*|QMAKE_RPATH =|
	s|QMAKE_STRIP\s*=.*|QMAKE_STRIP =|
	s|QMAKE_STRIPFLAGS_LIB\s*+=.*|QMAKE_STRIPFLAGS_LIB =|
	s|QMAKE_LINK\s*=.*g++|QMAKE_LINK = %{__cxx}|
	s|QMAKE_LINK_SHLIB\s*=.*g++|QMAKE_LINK_SHLIB = %{__cxx}|
	s|QMAKE_CC\s*=.*gcc|QMAKE_CC = %{__cc}|
	s|QMAKE_CXX\s*=.*g++|QMAKE_CXX = %{__cxx}|
	s|QMAKE_CFLAGS\s*=.*-pipe|QMAKE_CFLAGS\t=\t%{rpmcflags} -pipe -I/usr/include/tirpc|
	s|QMAKE_CFLAGS_RELEASE\s*=.*|QMAKE_CFLAGS_RELEASE\t=\t%{rpmcflags} -I/usr/include/tirpc|
	s|QMAKE_CFLAGS_DEBUG\s*=.*|QMAKE_CFLAGS_DEBUG\t=\t%{debugcflags} -I/usr/include/tirpc|
	s|QMAKE_CXXFLAGS_RELEASE\s*=.*|QMAKE_CXXFLAGS_RELEASE\t=\t%{rpmcxxflags} -I/usr/include/tirpc|
	s|QMAKE_CXXFLAGS_DEBUG\s*=.*|QMAKE_CXXFLAGS_DEBUG\t=\t%{debugcflags} -I/usr/include/tirpc|
	s|QMAKE_LFLAGS_RELEASE\s*=.*|QMAKE_LFLAGS_RELEASE\t=\t%{rpmldflags} -ltirpc|
	s|QMAKE_LFLAGS_DEBUG\s*=.*|QMAKE_LFLAGS_DEBUG\t=\t%{rpmldflags} -ltirpc|
	' mkspecs/linux-g++/qmake.conf

# default ODBC headers are used (from unixODBC), not iodbc ones; so link with unixODBC not libiodbc
%{__sed} -i -e 's/-liodbc/-lodbc/' src/sql/qt_sql.pri
%{__sed} -i -e 's/-liodbc/-lodbc/' plugins/src/sqldrivers/odbc/odbc.pro

%build
export QTDIR=$(pwd)
export PATH=$QTDIR/bin:$PATH
export LD_LIBRARY_PATH=$QTDIR/%{_lib}${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}

%if "%{_lib}" != "lib"
	ln -sf lib "%{_lib}"
%endif

# pass OPTFLAGS to build qmake itself with optimization
export OPTFLAGS="%{rpmcxxflags}"

##################################
# DEFAULT OPTIONS FOR ALL BUILDS #
##################################

DEFAULTOPT=" \
%if "%{_lib}" != "lib"
	-DUSE_LIB64_PATHES \
%endif
	-DQT_CLEAN_NAMESPACE \
	-release \
	-buildkey pld-linux \
	-verbose \
	-prefix %{_prefix} \
	-libdir %{_libdir} \
	-L%{_libdir} \
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
	%{!?with_cups:-no}-cups \
	%{?with_nas:-system-nas-sound} \
	%{?with_dlopen_gl:-dlopen-opengl} \
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
	%{?with_ibase:-qt-sql-ibase} \
	%{?with_mysql:-qt-sql-mysql} \
	%{?with_odbc:-qt-sql-odbc} \
	%{?with_pgsql:-qt-sql-psql} \
	%{?with_sqlite:-qt-sql-sqlite} \
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
#	  SHARED SINGLE-THREAD	  #
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
%{?with_sql:cp -R plugins/sqldrivers plugins-st}
%{__make} clean
%endif

##################################
#	  SHARED MULTI-THREAD	   #
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
# with __make -jN we can got (making qmake_image_collection.o):
#	cc1plus: error: designercore: No such file or directory
#	cc1plus: error: one or more PCH files were found, but they were invalid
#	cc1plus: error: use -Winvalid-pch for more information
%{__make} -j1 sub-tools \
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
for i in *.ts; do
	LD_PRELOAD=$QTDIR/%{_lib}/libqt-mt.so.3 lrelease ${i}
done
cd -

##make -C extensions/nsplugin/src

%install
rm -rf $RPM_BUILD_ROOT

export QTDIR=$(pwd)

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT%{_sysconfdir}/qt \
	$RPM_BUILD_ROOT%{_libdir}/qt/plugins-mt/{crypto,network} \
	%{?with_single:$RPM_BUILD_ROOT%{_libdir}/qt/plugins-st/network} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}/lib \
	$RPM_BUILD_ROOT%{_mandir}/man{1,3} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install -p bin/{findtr,qt20fix,qtrename140} \
	tools/{msg2qm/msg2qm,mergetr/mergetr} \
	$RPM_BUILD_ROOT%{_bindir}

%if %{with static_libs}
cp -a %{_lib}/libqt*.a		$RPM_BUILD_ROOT%{_libdir}
%endif

%if %{with single}
install -p %{_lib}/libqt.so.*.*.*	$RPM_BUILD_ROOT%{_libdir}
ln -sf libqt.so.%{ver}		$RPM_BUILD_ROOT%{_libdir}/libqt.so
cp -a %{_lib}/qt.pc		$RPM_BUILD_ROOT%{_pkgconfigdir}
cp -R plugins-st/*		$RPM_BUILD_ROOT%{_libdir}/qt/plugins-st
%endif

cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%if %{with designer}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/designer.desktop
install %{SOURCE5} $RPM_BUILD_ROOT%{_pixmapsdir}
%endif

install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_desktopdir}

install %{SOURCE6} %{SOURCE7} $RPM_BUILD_ROOT%{_pixmapsdir}

cp -a tools/qtconfig/images/appicon.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/qtconfig.png

%if %{without designer}
install -p bin/uic $RPM_BUILD_ROOT%{_bindir}
%endif

# Because trolltech fails to think.
rm -rf $RPM_BUILD_ROOT%{_bindir}/qmake
install -p qmake/qmake $RPM_BUILD_ROOT%{_bindir}/qmake

cp -a doc/man/man1/*.1	$RPM_BUILD_ROOT%{_mandir}/man1
cp -a doc/man/man3/*.3qt	$RPM_BUILD_ROOT%{_mandir}/man3

cp -dpR examples tutorial $RPM_BUILD_ROOT%{_examplesdir}/%{name}

mv $RPM_BUILD_ROOT{%{_libdir}/*.prl,%{_examplesdir}/%{name}/lib}

%{__sed} -i -e '
	# From now QMAKE_INCDIR_QT becomes %{_includedir}/qt
	s|\(QMAKE_INCDIR_QT\s*=\s*\$(QTDIR)/include\)|\1/qt|
	# Remove ccache if any
	/QMAKE_\(CC\|CXX\|LINK\)/s|ccache ||;
' $RPM_BUILD_ROOT%{_datadir}/qt/mkspecs/linux-g++/qmake.conf
rm $RPM_BUILD_ROOT%{_datadir}/qt/mkspecs/linux-g++/qmake.conf.orig

# We provide qt style classes as plugins,
# so make corresponding changes to the qconfig.h.
chmod u+w $RPM_BUILD_ROOT%{_includedir}/qt/qconfig.h

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

install -d $RPM_BUILD_ROOT%{_datadir}/locale/{ar,ca,cs,de,es,fr,he,it,ja,nb,pt,pt_BR,ru,sk,zh_CN,zh_TW}/LC_MESSAGES
mv $RPM_BUILD_ROOT%{_datadir}/locale/{qt_ar.qm,ar/LC_MESSAGES/qt.qm}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{qt_ca.qm,ca/LC_MESSAGES/qt.qm}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{qt_cs.qm,cs/LC_MESSAGES/qt.qm}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{qt_de.qm,de/LC_MESSAGES/qt.qm}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{qt_es.qm,es/LC_MESSAGES/qt.qm}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{qt_fr.qm,fr/LC_MESSAGES/qt.qm}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{qt_he.qm,he/LC_MESSAGES/qt.qm}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{qt_it.qm,it/LC_MESSAGES/qt.qm}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{qt_ja.qm,ja/LC_MESSAGES/qt.qm}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{qt_nb.qm,nb/LC_MESSAGES/qt.qm}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{qt_pt-br.qm,pt_BR/LC_MESSAGES/qt.qm}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{qt_ru.qm,ru/LC_MESSAGES/qt.qm}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{qt_sk.qm,sk/LC_MESSAGES/qt.qm}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{qt_zh-cn.qm,zh_CN/LC_MESSAGES/qt.qm}
mv $RPM_BUILD_ROOT%{_datadir}/locale/{qt_zh-tw.qm,zh_TW/LC_MESSAGES/qt.qm}

%if %{with designer}
cp -a tools/designer/designer/designer_de.qm $RPM_BUILD_ROOT%{_datadir}/locale/de/LC_MESSAGES/designer.qm
cp -a tools/designer/designer/designer_fr.qm $RPM_BUILD_ROOT%{_datadir}/locale/fr/LC_MESSAGES/designer.qm
%endif

mv $RPM_BUILD_ROOT%{_datadir}/locale/{assistant_de.qm,de/LC_MESSAGES/assistant.qm}
cp -a tools/assistant/assistant_fr.qm $RPM_BUILD_ROOT%{_datadir}/locale/fr/LC_MESSAGES/assistant.qm

cp -a tools/linguist/linguist/linguist_de.qm $RPM_BUILD_ROOT%{_datadir}/locale/de/LC_MESSAGES/linguist.qm
cp -a tools/linguist/linguist/linguist_fr.qm $RPM_BUILD_ROOT%{_datadir}/locale/fr/LC_MESSAGES/linguist.qm

cp -a tools/linguist/qm2ts/qm2ts.1 $RPM_BUILD_ROOT%{_mandir}/man1

find $RPM_BUILD_ROOT -name CVS | xargs rm -rf

cd $RPM_BUILD_ROOT%{_examplesdir}/%{name}/examples
for i in $(find -name Makefile); do
	%{__sed} -i -e "s,$RPM_BUILD_DIR,/usr,g" $i
	%{__sed} -i -e "s,examples,src/examples/qt/examples,g" $i
done

cd $RPM_BUILD_ROOT%{_examplesdir}/%{name}/tutorial
for i in $(find -name Makefile); do
	%{__sed} -i -e "s,$RPM_BUILD_DIR,/usr,g" $i
	%{__sed} -i -e "s,examples,src/examples/qt/tutorial,g" $i
done

# drop some bad symlink
rm -f $RPM_BUILD_ROOT%{_datadir}/qt/mkspecs/linux-g++/linux-g++

# unwanted symlinks
rm $RPM_BUILD_ROOT%{_libdir}/libdesignercore.so.1.0
rm $RPM_BUILD_ROOT%{_libdir}/libeditor.so.1.0
rm $RPM_BUILD_ROOT%{_libdir}/libqassistantclient.so.1.0
rm $RPM_BUILD_ROOT%{_libdir}/libqt-mt.so.3.3
rm $RPM_BUILD_ROOT%{_libdir}/libqui.so.1.0

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
%attr(755,root,root) %ghost %{_libdir}/libqassistantclient.so.1
%attr(755,root,root) %{_libdir}/libqt-mt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqt-mt.so.3
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins-mt
%dir %{_libdir}/%{name}/plugins-mt/crypto
%dir %{_libdir}/%{name}/plugins-mt/imageformats
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/imageformats/*.so
%dir %{_libdir}/%{name}/plugins-mt/inputmethods
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/inputmethods/libqimsw-multi.so
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/inputmethods/libqimsw-none.so
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/inputmethods/libqsimple.so
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/inputmethods/libqxim.so
%dir %{_libdir}/%{name}/plugins-mt/network
%{?with_sql:%dir %{_libdir}/%{name}/plugins-mt/sqldrivers}
%dir %{_libdir}/%{name}/plugins-mt/styles
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/styles/*.so
%dir %{_datadir}/qt
%lang(ar) %{_datadir}/locale/ar/LC_MESSAGES/qt.qm
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/qt.qm
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/qt.qm
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/qt.qm
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/qt.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/qt.qm
%lang(he) %{_datadir}/locale/he/LC_MESSAGES/qt.qm
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/qt.qm
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/qt.qm
%lang(nb) %{_datadir}/locale/nb/LC_MESSAGES/qt.qm
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/qt.qm
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/qt.qm
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/qt.qm
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/qt.qm
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/qt.qm

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/makeqpf
%attr(755,root,root) %{_bindir}/moc
%attr(755,root,root) %{_bindir}/qembed
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
%{_mandir}/man3/Q*.3qt*
%{_mandir}/man3/q*.3qt*

%if %{with mysql}
%files plugin-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/sqldrivers/libqsqlmysql.so
%endif

%if %{with pgsql}
%files plugin-psql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/sqldrivers/libqsqlpsql.so
%endif

%if %{with odbc}
%files plugin-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/sqldrivers/libqsqlodbc.so
%endif

%if %{with sqlite}
%files plugin-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/sqldrivers/libqsqlite.so
%endif

%if %{with ibase}
%files plugin-ibase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-mt/sqldrivers/libqsqlibase.so
%endif

%if %{with single}
%files st
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqt.so.*.*.*
%dir %{_libdir}/%{name}/plugins-st
%dir %{_libdir}/%{name}/plugins-st/network
%{?with_sql:%dir %{_libdir}/%{name}/plugins-st/sqldrivers}
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
%attr(755,root,root) %{_libdir}/%{name}/plugins-st/sqldrivers/libqsqlmysql.so
%endif

%if %{with pgsql}
%files st-plugin-psql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-st/sqldrivers/libqsqlpsql.so
%endif

%if %{with odbc}
%files st-plugin-odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-st/sqldrivers/libqsqlodbc.so
%endif

%if %{with sqlite}
%files st-plugin-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-st/sqldrivers/libqsqlite.so
%endif

%if %{with ibase}
%files st-plugin-ibase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins-st/sqldrivers/libqsqlibase.so
%endif
%endif

%if %{with designer}
%files designer-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdesignercore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdesignercore.so.1
%attr(755,root,root) %{_libdir}/libeditor.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeditor.so.1
%attr(755,root,root) %{_libdir}/libqui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqui.so.1
%attr(755,root,root) %{_libdir}/libdesignercore.so
%attr(755,root,root) %{_libdir}/libeditor.so
%attr(755,root,root) %{_libdir}/libqui.so

%files designer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/createcw
%attr(755,root,root) %{_bindir}/designer
%attr(755,root,root) %{_libdir}/%{name}/plugins-?t/designer/*.so
%dir %{_libdir}/%{name}/plugins-?t/designer
%{_datadir}/qt/designer
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/designer.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/designer.qm
%{_desktopdir}/designer.desktop
%{_pixmapsdir}/designer.png
%endif

%files assistant
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/assistant
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/assistant.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/assistant.qm
%{_desktopdir}/assistant.desktop
%{_pixmapsdir}/assistant.png

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
%{_datadir}/qt/phrasebooks
%{_desktopdir}/linguist.desktop
%{_pixmapsdir}/linguist.png
%{_mandir}/man1/l*
%{_mandir}/man1/*qm*

%files -n qtconfig
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtconfig
%{_desktopdir}/qtconfig.desktop
%{_pixmapsdir}/qtconfig.png
