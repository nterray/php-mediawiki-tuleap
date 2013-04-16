Name:            php-mediawiki-tuleap
Version:         1.20.3
Release:         3%{?dist}
Summary:         A wiki engine

Group:           Development/Tools
License:         GPLv2+
URL:             http://www.mediawiki.org
Source0:         mediawiki-%{version}.tar.gz
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:       noarch
AutoReqProv:     no

Requires:        php, ImageMagick

%description
php-mediawiki-tuleap is a mediawiki instance for Tuleap use. It aims to provide
mediawiki integration within Tuleap's hosted projects.

%prep
%setup -qn mediawiki-%{version}

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/mediawiki-tuleap
%{__cp} -pr * $RPM_BUILD_ROOT%{_datadir}/mediawiki-tuleap

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/mediawiki-tuleap
%doc docs

%changelog
* Tue Apr 16 2013 Manuel VACELET <manuel.vacelet@enalean.com> - 1.20.3-3
- Move to centos6

* Tue Apr 2 2013 Manuel VACELET <manuel.vacelet@enalean.com> - 1.20.3-2
- Thumbnail generator requires ImageMagick

* Thu Mar 21 2013 Martin GOYOT <martin.goyot@enalean.com> - 1.20.3-1
- initial build <3
