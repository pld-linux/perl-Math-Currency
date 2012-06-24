#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Currency
Summary:	Math::Currency - exact currency math with formatting and rounding
Summary(pl):	Math::Currency - dok�adne obliczenia na walutach z formatowaniem i zaokr�glaniem
Name:		perl-Math-Currency
Version:	0.39
Release:	1
License:	GPL v1+ or Artistic except commercial distribution on CD-ROM etc.
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f53c41ec41be1bd576def284845e0b16
Patch0:		%{name}-perl_paths.patch
BuildRequires:	perl-Math-BigInt
BuildRequires:	perl(Math::BigFloat) >= 1.27
%if %{with tests}
BuildRequires:	perl-Test-Simple
BuildRequires:	perl(Test::More) >= 0.02
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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

%description -l pl
Obliczenia na walutach s� w�a�ciwie bli�sze obliczeniom na liczbach
ca�kowitych ni� zmiennoprzecinkowych. B��dy zaokr�gle� przy dodawaniu
i odejmowaniu nie s� dozwolone, a dzielenie czy mno�enie nie powinno
da� wi�kszej dok�adno�ci ni� oryginalne warto�ci. Wszystkie warto�ci
monetarne powinny by� zaokr�glane do najbli�szego centa czy
czegokolwiek b�d�cego jego lokalnym odpowiednikiem.

Wszystkie zwyk�e operacje matematyczne s� przeci��one, wi�c po
zainicjalizowaniu zmiennej monetarnej mo�na j� traktowa� jak ka�d�
liczb�, a modu� zrobi to co trzeba. Ten modu� jest cienk� warstw�
osadzon� na Math::BigFloat, kt�ry z kolei jest warstw� na
Math::BigInt.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/Currency.pm
%{_mandir}/man3/*
