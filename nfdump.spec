Summary:	Netflow processing tools
Name:		nfdump
Version:	1.5.1
Release:	1
License:	BSD
Group:		Applications
Source0:	http://dl.sourceforge.net/nfdump/%{name}-%{version}.tar.gz
# Source0-md5:	76325d91d5061341ffcc2b43c9f2c400
Source1:	http://www.ripe.net/ripe/meetings/ripe-50/presentations/ripe50-plenary-tue-nfsen-%{name}.pdf
# Source1-md5:	76325d91d5061341ffcc2b43c9f2c400
URL:		http://nfdump.sourceforge.net/
BuildRequires:	bison
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The nfdump tools collect and process netflow data on the command line.
They are part of the NfSen project.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install *.1 $RPM_BUILD_ROOT%{_mandir}/man1
install nfcapd nfdump nfgen nfprofile nfreplay nftest $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README ToDo
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
