#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	Currency
Summary:	Math::Currency - exact currency math with formatting and rounding
Summary(pl.UTF-8):	Math::Currency - dokładne obliczenia na walutach z formatowaniem i zaokrąglaniem
Name:		perl-Math-Currency
Version:	0.47
Release:	1
License:	GPL v1+ or Artistic except commercial distribution on CD-ROM etc.
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	545e37f755c50385df2dec5b8d55239b
URL:		http://search.cpan.org/dist/Math-Currency/
BuildRequires:	perl(Math::BigFloat) >= 1.27
BuildRequires:	perl-Math-BigInt
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::More) >= 0.02
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Currency math is actually more closely related to integer math than it
is to floating point math. Rounding errors on addition and subtraction
are not allowed and division/multiplication should never create more
accuracy than the original values. All currency values should round to
the closest cent or whatever the local equivalent should happen to be.

All common mathematical operations are overloaded, so once you
initialize a currency variable, you can treat it like any number and
the module will do the right thing. This module is a thin layer over
Math::BigFloat which is itself a layer over Math::BigInt.

%description -l pl.UTF-8
Obliczenia na walutach są właściwie bliższe obliczeniom na liczbach
całkowitych niż zmiennoprzecinkowych. Błędy zaokrągleń przy dodawaniu
i odejmowaniu nie są dozwolone, a dzielenie czy mnożenie nie powinno
dać większej dokładności niż oryginalne wartości. Wszystkie wartości
monetarne powinny być zaokrąglane do najbliższego centa czy
czegokolwiek będącego jego lokalnym odpowiednikiem.

Wszystkie zwykłe operacje matematyczne są przeciążone, więc po
zainicjalizowaniu zmiennej monetarnej można ją traktować jak każdą
liczbę, a moduł zrobi to co trzeba. Ten moduł jest cienką warstwą
osadzoną na Math::BigFloat, który z kolei jest warstwą na
Math::BigInt.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
%{__perl} Build

%{?with_tests:%{__perl} Build test}

%install
rm -rf $RPM_BUILD_ROOT

%{__perl} Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/Currency.pm
%dir %{perl_vendorlib}/Math/Currency
%{perl_vendorlib}/Math/Currency/*.pm
%{_mandir}/man3/*
