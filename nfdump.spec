Summary:	Netflow processing tools
Summary(pl.UTF-8):	Narzędzia do przetwarzania ruchu sieciowego
Name:		nfdump
Version:	1.5.8
Release:	1
License:	BSD
Group:		Applications
Source0:	http://dl.sourceforge.net/nfdump/%{name}-%{version}.tar.gz
# Source0-md5:	f314513652df18259f8303c542918cbb
Source1:	http://www.ripe.net/ripe/meetings/ripe-50/presentations/ripe50-plenary-tue-nfsen-%{name}.pdf
# Source1-md5:	6240259f9e54bc78894e99ea1deef776
URL:		http://nfdump.sourceforge.net/
BuildRequires:	bison
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The nfdump tools collect and process netflow data on the command line.
They are part of the NfSen project.

%description -l pl.UTF-8
Narzędzia nfdump zbierają i przetwarzają dane z ruchu sieciowego
(netflow) z linii poleceń. Są częścią projektu NfSen.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install *.1 $RPM_BUILD_ROOT%{_mandir}/man1
install nfcapd nfdump nfexpire nfgen nfreplay nftest $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README ToDo
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
