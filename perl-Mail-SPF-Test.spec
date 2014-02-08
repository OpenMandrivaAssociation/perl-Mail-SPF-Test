%define upstream_name Mail-SPF-Test
%define upstream_version 1.001

Summary:	SPF test-suite class
Name:		perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	6
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Mail/%{upstream_name}-v%{upstream_version}.tar.bz2
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(NetAddr::IP)
BuildRequires:	perl(Net::DNS)
BuildRequires:	perl(YAML)
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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-4mdv2012.0
+ Revision: 765458
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2
+ Revision: 667253
- mass rebuild

* Mon Jan 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 489722
- use Module::Build
- use %%perl_version macro
- spec cleanup

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.001-4mdv2010.0
+ Revision: 426522
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.001-3mdv2009.0
+ Revision: 223814
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.001-2mdv2008.1
+ Revision: 180464
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 02 2007 Oden Eriksson <oeriksson@mandriva.com> 1.001-1mdv2008.0
+ Revision: 47039
- Import perl-Mail-SPF-Test



* Mon Jul 02 2007 Oden Eriksson <oeriksson@mandriva.com> 1.001-1mdv2008.0
- initial Mandriva package 
