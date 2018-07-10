#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Sys
%define		pnam	MemInfo
%include	/usr/lib/rpm/macros.perl
Summary:	Sys::MemInfo - query the total free and used physical memory
Name:		perl-Sys-MemInfo
Version:	0.99
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sys/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	88f0632691d7de91cbed95ba1ff29025
URL:		https://metacpan.org/release/Sys-MemInfo/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sys::MemInfo return the total amount of free and used physical memory in bytes in totalmem and freemem variables.

Total amount of free and user swap memory are alse returned in totalswap and freeswap variables.

This module has been tested on Linux 3.13.0, UnixWare 7.1.2, AIX5, OpenBSD 3.8, 
NetBSD 2.0.2, FreBSD 5.4, HPUX11, Solaris 9, Tru64 5.1, Irix 6.5, Mac OS X 10.2 darwin and Windows XP.

It should work on FreeBSD 4 and Windows 9X/ME/NT/200X/Vista.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Sys/MemInfo.pm
%dir %{perl_vendorarch}/auto/Sys/MemInfo
%attr(755,root,root) %{perl_vendorarch}/auto/Sys/MemInfo/MemInfo.so
%{_mandir}/man3/Sys::MemInfo.3pm*
