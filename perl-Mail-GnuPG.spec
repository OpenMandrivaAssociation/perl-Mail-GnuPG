%define module	Mail-GnuPG
%define name	perl-%{module}
%define version	0.10
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Process email with GPG
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Mail/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(GnuPG::Interface)
BuildRequires:  perl(Class::MethodMaker)
BuildRequires:  perl-MIME-tools
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Use GnuPG::Interface to process or create PGP signed or encrypted email.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Mail
%{_mandir}/*/*
