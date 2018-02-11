Summary:	Netflow processing tools
Summary(pl.UTF-8):	Narzędzia do przetwarzania ruchu sieciowego
Name:		nfdump
Version:	1.6.16
Release:	1
License:	BSD
Group:		Applications
Source0:	https://github.com/phaag/nfdump/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9f768d380e8fcf88f56e14009a509e74
Source1:	http://www.ripe.net/ripe/meetings/ripe-50/presentations/ripe50-plenary-tue-nfsen-%{name}.pdf
# Source1-md5:	6240259f9e54bc78894e99ea1deef776
URL:		https://github.com/phaag/nfdump
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	rrdtool-devel
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
%configure \
	--enable-nfprofile \
	--enable-sflow
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/nf*
%attr(755,root,root) %{_bindir}/sfcapd
%attr(755,root,root) %{_libdir}/libnfdump-1.6.15.so
%{_mandir}/man1/*
