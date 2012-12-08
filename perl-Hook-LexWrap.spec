%define upstream_name    Hook-LexWrap
%define upstream_version 0.24

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Lexically scoped subroutine wrappers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Hook/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Hook::LexWrap allows you to install a pre- or post-wrapper (or both)
around an existing subroutine. Unlike other modules that provide this
capacity (e.g. Hook::PreAndPost and Hook::WrapSub), Hook::LexWrap
implements wrappers in such a way that the standard `caller' function
works correctly within the wrapped subroutine.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Hook
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.240.0-4mdv2012.0
+ Revision: 765300
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.240.0-3
+ Revision: 763841
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.240.0-2
+ Revision: 676844
- rebuild

* Fri Nov 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.240.0-1mdv2011.0
+ Revision: 596534
- update to new version 0.24

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2011.0
+ Revision: 561575
- update to 0.23

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.22-2mdv2011.0
+ Revision: 440579
- rebuild

* Thu Feb 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2009.1
+ Revision: 345119
- update to new version 0.22

* Sun Nov 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-1mdv2009.1
+ Revision: 306009
- new version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.20-4mdv2009.0
+ Revision: 241444
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-2mdv2008.0
+ Revision: 86470
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.20-1mdv2007.0
- rebuild

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 0.20-1mdk
- initial Mandriva package

