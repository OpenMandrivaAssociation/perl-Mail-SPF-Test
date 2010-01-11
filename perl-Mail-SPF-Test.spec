%define upstream_name Mail-SPF-Test
%define upstream_version 1.001

Summary:	SPF test-suite class
Name:		perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Mail/%{upstream_name}-v%{upstream_version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Module-Build
BuildRequires:	perl-NetAddr-IP
BuildRequires:	perl-Net-DNS
BuildRequires:	perl-YAML
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Mail::SPF::Test is a class for reading and manipulating SPF test-suite data.

%prep
%setup -q -n %{upstream_name}-v%{upstream_version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES LICENSE README TODO
%{perl_vendorlib}/Mail/SPF/*.pm
%{perl_vendorlib}/Mail/SPF/Test/*.pm
%{_mandir}/*/*
