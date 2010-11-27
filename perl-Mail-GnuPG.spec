%define upstream_name    Mail-GnuPG
%define upstream_version 0.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:	Process email with GPG
License:	GPL or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Mail/%{upstream_name}-%{upstream_version}.tar.gz
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
%setup -q -n %{upstream_name}-%{upstream_version}

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
