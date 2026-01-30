#
# Conditional build:
%bcond_without	extra		# nfprofile, nftrack utilities (used by nfsen)

Summary:	Netflow processing tools
Summary(pl.UTF-8):	Narzędzia do przetwarzania ruchu sieciowego
Name:		nfdump
Version:	1.7.7
Release:	2
License:	BSD
Group:		Applications
Source0:	https://github.com/phaag/nfdump/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9a11af046f10519c6f65772fead19d1e
Source1:	http://www.ripe.net/ripe/meetings/ripe-50/presentations/ripe50-plenary-tue-nfsen-%{name}.pdf
# Source1-md5:	6240259f9e54bc78894e99ea1deef776
URL:		https://github.com/phaag/nfdump
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	bzip2-devel
BuildRequires:	flex
# c17
BuildRequires:	gcc >= 6:7
BuildRequires:	libpcap-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	lz4-devel
%if %{with extra}
BuildRequires:	rrdtool-devel
%endif
BuildRequires:	zlib-devel >= 1.0.2
BuildRequires:	zstd-devel
Requires:	zlib >= 1.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The nfdump tools collect and process netflow data on the command line.
They are part of the NfSen project.

%description -l pl.UTF-8
Narzędzia nfdump zbierają i przetwarzają dane z ruchu sieciowego
(netflow) z linii poleceń. Są częścią projektu NfSen.

%package libs
Summary:	Libraries for nfdump
Summary(pl.UTF-8):	Biblioteki dla nfdump
Group:		Libraries
Obsoletes:	nfdump-static < 1.7.7-2

%description libs
Libraries for nfdump

%description libs -l pl.UTF-8
Biblioteki dla nfdump

%package extra
Summary:	Extra utilities for nfdump
Summary(pl.UTF-8):	Dodatkowe narzędzia dla nfdump
Group:		Networking/Utilities

%description extra
Extra utilities for nfdump used by nfsen

%description extra -l pl.UTF-8
Dodatkowe narzędzia dla nfdump używane przez nfsen

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
%if %{with extra}
	--enable-nfprofile \
	--enable-nftrack \
%endif
	--enable-sflow \
	--enable-readpcap \
	--enable-nfpcapd
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libnf{dump,file}.{la,so}
%{__mv} $RPM_BUILD_ROOT%{_sysconfdir}/nfdump.conf{.dist,}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README
%attr(755,root,root) %{_bindir}/nfanon
%attr(755,root,root) %{_bindir}/nfcapd
%attr(755,root,root) %{_bindir}/nfdump
%attr(755,root,root) %{_bindir}/nfexpire
%attr(755,root,root) %{_bindir}/nfpcapd
%attr(755,root,root) %{_bindir}/nfreplay
%attr(755,root,root) %{_bindir}/sfcapd
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nfdump.conf
%{_mandir}/man1/nfanon.1*
%{_mandir}/man1/nfcapd.1*
%{_mandir}/man1/nfdump.1*
%{_mandir}/man1/nfexpire.1*
%{_mandir}/man1/nfpcapd.1*
%{_mandir}/man1/nfreplay.1*
%{_mandir}/man1/sfcapd.1*

%files libs
%defattr(644,root,root,755)
%{_libdir}/libnfdump-%{version}.so
%{_libdir}/libnffile-%{version}.so

%if %{with extra}
%files extra
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nfprofile
%attr(755,root,root) %{_bindir}/nftrack
%{_mandir}/man1/nfprofile.1*
%endif
