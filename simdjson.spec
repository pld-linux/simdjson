Summary:	Parsing gigabytes of JSON per second
Summary(pl.UTF-8):	Analiza gigabajtów danych JSON na sekundę
Name:		simdjson
Version:	4.3.1
Release:	1
License:	Apache v2.0 or MIT
Group:		Libraries
#Source0Download: https://github.com/simdjson/simdjson/releases
Source0:	https://github.com/simdjson/simdjson/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c1da512aecfc85dbfe62951537ef5747
URL:		https://simdjson.org/
BuildRequires:	cmake >= 3.14
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	rpmbuild(macros) >= 1.605
ExclusiveArch:	%{ix86} %{x8664} %{arm} aarch64 loongarch64 ppc ppc64 riscv64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON documents are everywhere on the Internet. Servers spend a lot of
time parsing these documents. simdjson aims to accelerate the parsing
of JSON per se using commonly available SIMD instructions as much as
possible while doing full validation (including character encoding).

%description -l pl.UTF-8
Dokumenty JSON są wszędzie w Internecie. Serwery zużywają mnóstwo
czasu na ich analizę. Biblioteka simdjson jest próbą przyspieszenia
samej analizy JSON poprzez użycie możliwie jak największej liczby
powszechnie dostępnych instrukcji SIMD, jednocześnie wykonując pełne
sprawdzanie poprawności (wraz z kodowaniem znaków).

%package devel
Summary:	Header files for simdjson library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki simdjson
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:5

%description devel
Header files for simdjson library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki simdjson.

%prep
%setup -q

%build
%cmake -B build

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
%doc AUTHORS CONTRIBUTING.md CONTRIBUTORS HACKING.md LICENSE-MIT README.md
%attr(755,root,root) %{_libdir}/libsimdjson.so.*.*.*
%ghost %{_libdir}/libsimdjson.so.30

%files devel
%defattr(644,root,root,755)
%{_libdir}/libsimdjson.so
%{_includedir}/simdjson.h
%{_libdir}/cmake/simdjson
%{_pkgconfigdir}/simdjson.pc
