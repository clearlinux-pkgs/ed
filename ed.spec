Name     : ed
Version  : 1.19
Release  : 23
URL      : https://mirrors.kernel.org/gnu/ed/ed-1.19.tar.lz
Source0  : https://mirrors.kernel.org/gnu/ed/ed-1.19.tar.lz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: ed-bin = %{version}-%{release}
Requires: ed-info = %{version}-%{release}
Requires: ed-license = %{version}-%{release}
Requires: ed-man = %{version}-%{release}
BuildRequires : plzip

%description
Description
GNU ed is a line-oriented text editor. It is used to create, display,
modify and otherwise manipulate text files, both interactively and via
shell scripts. A restricted version of ed, red, can only edit files in
the current directory and cannot execute shell commands. Ed is the
'standard' text editor in the sense that it is the original editor for
Unix, and thus widely available. For most purposes, however, it is
superseded by full-screen editors such as GNU Emacs or GNU Moe.

%package bin
Summary: bin components for the ed package.
Group: Binaries
Requires: ed-license = %{version}-%{release}

%description bin
bin components for the ed package.


%package info
Summary: info components for the ed package.
Group: Default

%description info
info components for the ed package.


%package license
Summary: license components for the ed package.
Group: Default

%description license
license components for the ed package.


%package man
Summary: man components for the ed package.
Group: Default

%description man
man components for the ed package.


%prep
%setup -q

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573777459
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static CFLAGS="$CFLAGS"
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1573777459
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ed
cp %{_builddir}/ed-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ed/aeb23ef9343dcd5bfaf91ec1088f508e646f5370
%make_install

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ed
/usr/bin/red

%files info
%defattr(0644,root,root,0755)
/usr/share/info/ed.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ed/aeb23ef9343dcd5bfaf91ec1088f508e646f5370

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ed.1
/usr/share/man/man1/red.1
