%define real_name Mail-SPF-Test

Summary:	SPF test-suite class
Name:		perl-%{real_name}
Version:	1.001
Release:	%mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JM/JMEHNLE/mail-spf-test/%{real_name}-v%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Module-Build
BuildRequires:	perl-NetAddr-IP
BuildRequires:	perl-Net-DNS
BuildRequires:	perl-YAML
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Mail::SPF::Test is a class for reading and manipulating SPF test-suite data.

%prep

%setup -q -n %{real_name}-v%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES LICENSE README TODO
%{perl_vendorlib}/Mail/SPF/*.pm
%{perl_vendorlib}/Mail/SPF/Test/*.pm
%{_mandir}/*/*
