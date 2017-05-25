#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ed
Version  : 1.14.2
Release  : 14
URL      : https://mirrors.kernel.org/gnu/ed/ed-1.14.2.tar.lz
Source0  : https://mirrors.kernel.org/gnu/ed/ed-1.14.2.tar.lz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0+
Requires: ed-bin
Requires: ed-doc
BuildRequires : lzip

%description
Description
GNU ed is a line-oriented text editor. It is used to create, display,
modify and otherwise manipulate text files, both interactively and via
shell scripts. A restricted version of ed, red, can only edit files in
the current directory and cannot execute shell commands. Ed is the
"standard" text editor in the sense that it is the original editor for
Unix, and thus widely available. For most purposes, however, it is
superseded by full-screen editors such as GNU Emacs or GNU Moe.

%package bin
Summary: bin components for the ed package.
Group: Binaries

%description bin
bin components for the ed package.


%package doc
Summary: doc components for the ed package.
Group: Documentation

%description doc
doc components for the ed package.


%prep
%setup -q -n ed-1.14.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1495720677
%configure --disable-static
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1495720677
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ed
/usr/bin/red

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
