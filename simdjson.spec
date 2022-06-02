Summary:	Parsing gigabytes of JSON per second
Name:		simdjson
Version:	2.0.2
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/simdjson/simdjson/releases
Source0:	https://github.com/simdjson/simdjson/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d645745db224e2a2dea3584180e57c1f
URL:		https://simdjson.org
BuildRequires:	cmake >= 3.9
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	rpmbuild(macros) >= 1.605
ExclusiveArch:	%{x8664} aarch64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON documents are everywhere on the Internet. Servers spend a lot of
time parsing these documents. simdjson aims to accelerate the parsing
of JSON per se using commonly available SIMD instructions as much as
possible while doing full validation (including character encoding).

%package devel
Summary:	Header files for simdjson library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for simdjson library.

%prep
%setup -q

%build
%cmake -B build \
	-DSIMDJSON_JUST_LIBRARY=ON
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTING.md CONTRIBUTORS HACKING.md README.md RELEASES.md
%attr(755,root,root) %{_libdir}/libsimdjson.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsimdjson.so.11

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsimdjson.so
%{_libdir}/cmake/simdjson
%{_includedir}/simdjson.h
