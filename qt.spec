Summary:     The Qt GUI application framework: Shared library
Summary(pl): Biblioteka Qt do tworzenia GUI
Name:        qt
Version:     1.40
Release:     3
Source0:     ftp://ftp.troll.no/qt/source/%{name}-%{version}.tar.gz
Patch0:      qt.patch
Copyright:   distributable
Group:       X11/Libraries
URL:         http://www.troll.no/
Buildroot:   /tmp/%{name}-%{version}-root

%description
Contains the shared library needed to run Qt applications, as well as
the README files for Qt.

%description -l pl
Zawiera bibliotekê Qt wymagan± przez aplikacje, które z niej korzystaj±.

%package devel
Summary:     Include files and documentation needed to compile
Summary(pl): Pliki nag³ówkowe, przyk³ady i dokumentacja do biblioteki 
Group:       X11/Libraries
Requires:    %{name} = %{version}

%description devel
Contains the files necessary to develop applications using Qt: header
files, the Qt meta object compiler, man pages, HTML documentation and
example programs.  See http://www.troll.no for more information about
Qt, or file:/usr/doc/%{name}-devel-%{version}/html/index.html for Qt
documentation in HTML.

%description -l pl devel
Pakiet tem zawiera pliki potrzebne do tworzenia i kompilacji aplikacji
korzystaj±cych z biblioteki Qt jak pliki nag³ówkowe, meta kompiler (moc),
dokumentacjê. Zobacz http://www.troll.no/ aby dowiedzieæ siê wiêcej o Qt.
Dokumentacjê do biblioteki znajdziesz tak¿e pod:
/usr/doc/%{name}-%{version}/html/index.html  

%prep
%setup -q
%patch -p1

%build
QTDIR=`/bin/pwd` export QTDIR
make linux-g++-shared
LD_LIBRARY_PATH=/usr/X11R6/lib \
make	SYSCONF_CFLAGS=$RPM_OPT_FLAGS \
	SYSCONF_CFLAGS_LIB="$RPM_OPT_FLAGS -fPIC" \
	SYSCONF_CFLAGS_SHOBJ="$RPM_OPT_FLAGS -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/{bin,include/X11/qt,lib,man/{man1,man3}}

install -s bin/moc $RPM_BUILD_ROOT/usr/X11R6/bin/moc
install -s lib/libqt.so.*.* $RPM_BUILD_ROOT/usr/X11R6/lib
ln -sf libqt.so.%{version} $RPM_BUILD_ROOT/usr/X11R6/lib/libqt.so
install man/man1/* $RPM_BUILD_ROOT/usr/X11R6/man/man1
install man/man3/* $RPM_BUILD_ROOT/usr/X11R6/man/man3
install include/* $RPM_BUILD_ROOT/usr/X11R6/include/X11/qt

for a in {tutorial,examples}/{Makefile,*/Makefile}; do
  sed 's-^SYSCONF_MOC.*-SYSCONF_MOC		= /usr/X11R6/bin/moc-' < $a > ${a}.2
  mv -v ${a}.2 $a
done

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc LICENSE README* FAQ
/usr/X11R6/lib/lib*.so.*.*

%files devel
%defattr(644, root, root, 755)
%doc html tutorial examples doc changes-* ANNOUNCE
%attr(755, root, root) /usr/X11R6/bin/*
%attr(644, root,  man) /usr/X11R6/man/man[13]/*
/usr/X11R6/include/X11/qt
%attr(  -, root, root) /usr/X11R6/lib/lib*.so

%changelog
* Tue Sep 15 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.40-3]
- added pl translation (based on translation maked by Jacek Konieczny
  <jajcus@zeus.polsl.gliwice.pl>),
- removed PORTING from %doc,
- ANNOUNCE and changes-* moved to devel %doc,
- changed install base directory to /usr/X11R6.

* Mon Aug  3 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.40-2]
- added -q %setup parameter and removed -n parameter,
- package rewrited for using Buildroot,
- added using %%{name} and %%{version} macros in Source,
- "rm -rf $RPM_BUILD_ROOT" moved from %prep to %install,
- spec file rewritten for using Buildroot,
- added %clean section,
- added URL,
- removed compiling tutorial and examples during building (qt.patch),
- fixed dependences for devel by adding "Requires: %%{name} = %%{version}",
- html, tutorial, examples and doc are marked as %doc in devel subpackage,
- header files moved to /usr/include/qt (to be consistent with FSSTND),
- replaced "mkdir -p" with "install -d" in %install,
- added striping binaries,
- /usr/lib/lib*.so moved to devel,
- fiew simplification in %files and %install,
- added using $RPM_OPT_FLAGS during compile,
- /sbin/ldconfig is now -p parameter in %post[un],
- added %defattr and %attr macros in %files (allows building package from
  non-root account).
