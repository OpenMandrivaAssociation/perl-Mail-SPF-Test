%define modname	Mail-SPF-Test
%define modver	v1.001

Summary:	SPF test-suite class
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Mail-SPF-Test
Source0:	https://cpan.metacpan.org/authors/id/J/JM/JMEHNLE/mail-spf-test/Mail-SPF-Test-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(NetAddr::IP)
BuildRequires:	perl(Net::DNS)
BuildRequires:	perl(YAML)

%description
Mail::SPF::Test is a class for reading and manipulating SPF test-suite data.

%prep
%autosetup -p1 -n %{modname}-v%{modver} 

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc CHANGES LICENSE README TODO
%{perl_vendorlib}/Mail/SPF/*.pm
%{perl_vendorlib}/Mail/SPF/Test/*.pm
%doc %{_mandir}/man3/*

