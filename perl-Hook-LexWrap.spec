%define modname	Hook-LexWrap
%define modver 0.26

Summary:	Lexically scoped subroutine wrappers
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/karenetheridge/Hook-LexWrap
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/Hook-LexWrap-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
Hook::LexWrap allows you to install a pre- or post-wrapper (or both)
around an existing subroutine. Unlike other modules that provide this
capacity (e.g. Hook::PreAndPost and Hook::WrapSub), Hook::LexWrap
implements wrappers in such a way that the standard `caller' function
works correctly within the wrapped subroutine.

%prep
%setup -qn %{modname}-%{modver}

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
%{_mandir}/man3/*
