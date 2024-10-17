%define upstream_name    Mail-GnuPG
%define upstream_version 0.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.19
Release:	3
Summary:	Process email with GPG
License:	GPL or Artistic
Group:		Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Mail/Mail-GnuPG-0.19.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(GnuPG::Interface)
BuildRequires:	perl(Class::MethodMaker)
BuildRequires:	perl(MIME::Tools)
BuildRequires:	perl(Module::Build)
BuildArch:	noarch

%description
Use GnuPG::Interface to process or create PGP signed or encrypted email.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
export LC_ALL=C
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes README
%{perl_vendorlib}/Mail
%{_mandir}/*/*


%changelog
* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 622946
- new version
- normalize perl version

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.15-5mdv2011.0
+ Revision: 440609
- rebuild

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-4mdv2009.1
+ Revision: 324509
- update to new version 0.15

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.10-1mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 08 2007 Funda Wang <fwang@mandriva.org> 0.10-1mdv2008.0
+ Revision: 60480
- New version 0.10


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-6mdv2007.0
- Rebuild

* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.08-5mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL

* Mon Oct 17 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.08-4mdk
- Fix BuildRequires

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.08-3mdk
- fix BuildRequires

* Fri Aug 26 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-2mdk
- spec cleanup  
- better url
- make test in %%check

* Wed Aug 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.08-1mdk 
- first mdk release


