%global debug_package %{nil}

Name:           tty-copy
Version:        0.2.2
Release:        1%{?dist}
Summary:        Copy content to system clipboard via TTY and terminal using ANSI OSC52 sequence

License:        MIT
URL:            https://github.com/jirutka/tty-copy
Source0:        https://github.com/jirutka/tty-copy/archive/v%{version}.tar.gz

BuildRequires:  gcc make rubygem-asciidoctor

%description
tty-copy is a utility for copying content to the system clipboard from
anywhere via a TTY and terminal using the ANSI OSC52 sequence. It works in any
terminal session, whether local, remote (e.g. SSH), or even nested therein.

%prep
%autosetup

%build
make

%check
# smoke test
%{buildroot}%{_bindir}/tty-copy -V

%install
# bin
make PREFIX=%{_prefix} DESTDIR=%{buildroot} install

%files
%license LICENSE
%doc README.adoc
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Aug 09 2022 cyqsimon - 0.2.2-1
- Release 0.2.2
