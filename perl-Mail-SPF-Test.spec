%define modname	Mail-SPF-Test
%define modver	1.001

Summary:	SPF test-suite class
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	5
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Mail/%{modname}-v%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(NetAddr::IP)
BuildRequires:	perl(Net::DNS)
BuildRequires:	perl(YAML)

%description
Mail::SPF::Test is a class for reading and manipulating SPF test-suite data.

%prep
%setup -qn %{modname}-v%{modver} 

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc CHANGES LICENSE README TODO
%{perl_vendorlib}/Mail/SPF/*.pm
%{perl_vendorlib}/Mail/SPF/Test/*.pm
%{_mandir}/man3/*

