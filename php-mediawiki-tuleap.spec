Name:            php-mediawiki-tuleap-123
Version:         1.23.9
Release:         5%{?dist}
Summary:         A wiki engine

Group:           Development/Tools
License:         GPLv2+
URL:             http://www.mediawiki.org
Source0:         mediawiki-%{version}.tar.gz
Source3:	 https://extdist.wmflabs.org/dist/extensions/LabeledSectionTransclusion-REL1_23-98e6ab8.tar.gz
Source4:	 https://extdist.wmflabs.org/dist/extensions/CategoryTree-REL1_23-c7333ea.tar.gz
Source5:	 https://extdist.wmflabs.org/dist/extensions/Cite-REL1_23-2342915.tar.gz
Source6:	 https://extdist.wmflabs.org/dist/extensions/ImageMap-REL1_23-1f17b01.tar.gz
Patch0:          php-mediawiki-tuleap.only_current_page_should_be_converted.patch
Patch1:          php-mediawiki-tuleap.add-Forge-to-database-types.patch
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
%{__tar} -xzf %{_sourcedir}/LabeledSectionTransclusion-REL1_23-98e6ab8.tar.gz
%{__tar} -xzf %{_sourcedir}/CategoryTree-REL1_23-c7333ea.tar.gz
%{__tar} -xzf %{_sourcedir}/Cite-REL1_23-2342915.tar.gz
%{__tar} -xzf %{_sourcedir}/ImageMap-REL1_23-1f17b01.tar.gz
cd %{_builddir}/mediawiki-%{version}

%patch0
%patch1 -p1
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
