%bcond_without	extra		# build extra utilities used by nfsen
				# (nfprofile and nftrack)

Summary:	Netflow processing tools
Summary(pl.UTF-8):	Narzędzia do przetwarzania ruchu sieciowego
Name:		nfdump
Version:	1.7.7
Release:	1
License:	BSD
Group:		Applications
Source0:	https://github.com/phaag/nfdump/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9a11af046f10519c6f65772fead19d1e
Source1:	http://www.ripe.net/ripe/meetings/ripe-50/presentations/ripe50-plenary-tue-nfsen-%{name}.pdf
# Source1-md5:	6240259f9e54bc78894e99ea1deef776
URL:		https://github.com/phaag/nfdump
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
%if %{with extra}
BuildRequires:	rrdtool-devel
%endif
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

%description libs
Libraries for nfdump

%description libs -l pl.UTF-8
Biblioteki dla nfdump

%package static
Summary:	Static libraries for nfdump
Summary(pl.UTF-8):	Statyczne biblioteki dla nfdump
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for nfdump

%description static -l pl.UTF-8
Statyczne biblioteki dla nfdump

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
./autogen.sh
%configure \
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
%doc AUTHORS ChangeLog README
%{_sysconfdir}/nfdump.conf
%attr(755,root,root) %{_bindir}/nfanon
%attr(755,root,root) %{_bindir}/nfcapd
%attr(755,root,root) %{_bindir}/nfdump
%attr(755,root,root) %{_bindir}/nfexpire
%attr(755,root,root) %{_bindir}/nfpcapd
%attr(755,root,root) %{_bindir}/nfreplay
%attr(755,root,root) %{_bindir}/sfcapd
%{_mandir}/man1/nfanon.*
%{_mandir}/man1/nfcapd.*
%{_mandir}/man1/nfdump.*
%{_mandir}/man1/nfexpire.*
%{_mandir}/man1/nfpcapd.*
%{_mandir}/man1/nfreplay.*
%{_mandir}/man1/sfcapd.*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnfdump-%{version}.so
%attr(755,root,root) %{_libdir}/libnffile-%{version}.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libnfdump.a
%{_libdir}/libnffile.a

%if %{with extra}
%files extra
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nfprofile
%attr(755,root,root) %{_bindir}/nftrack
%{_mandir}/man1/nfprofile.*
%endif
