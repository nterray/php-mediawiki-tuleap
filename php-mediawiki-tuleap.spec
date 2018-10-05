Name:            php-mediawiki-tuleap-123
Version:         1.23.9
Release:         5%{?dist}
Summary:         A wiki engine

Group:           Development/Tools
License:         GPLv2+
URL:             http://www.mediawiki.org
Source0:         mediawiki-%{version}.tar.gz
Patch2:          pdfbook-command-injection.patch
Patch3:          pdfbook-images-private-wiki.patch
Patch4:          Bump-to-GeSHI-v1.0.9.0.patch

BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:       noarch
AutoReqProv:     no

Requires:        ImageMagick, htmldoc

%description
php-mediawiki-tuleap is a mediawiki instance for Tuleap use. It aims to provide
mediawiki integration within Tuleap's hosted projects.

%prep
%setup -qn mediawiki-%{version}
cd extensions

cd %{_builddir}/mediawiki-%{version}

%patch2
%patch3
%patch4

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/mediawiki-tuleap-123
%{__cp} -pr * $RPM_BUILD_ROOT%{_datadir}/mediawiki-tuleap-123
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/mediawiki-tuleap-123/tests

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/mediawiki-tuleap-123
%doc docs
