Name:            php-mediawiki-tuleap-123
Version:         1.23.9
Release:         4%{?dist}
Summary:         A wiki engine

Group:           Development/Tools
License:         GPLv2+
URL:             http://www.mediawiki.org
Source0:         mediawiki-%{version}.tar.gz
Source1:         https://extdist.wmflabs.org/dist/extensions/SyntaxHighlight_GeSHi-REL1_23-4959271.tar.gz
Source2:         https://extdist.wmflabs.org/dist/PdfBook-REL1_23-17d1dfd.tar.gz
Source3:	 https://extdist.wmflabs.org/dist/extensions/LabeledSectionTransclusion-REL1_23-98e6ab8.tar.gz
Source4:	 https://extdist.wmflabs.org/dist/extensions/CategoryTree-REL1_23-c7333ea.tar.gz
Source5:	 https://extdist.wmflabs.org/dist/extensions/Cite-REL1_23-2342915.tar.gz
Source6:	 https://extdist.wmflabs.org/dist/extensions/ImageMap-REL1_23-1f17b01.tar.gz
Patch0:          php-mediawiki-tuleap.only_current_page_should_be_converted.patch
Patch1:          php-mediawiki-tuleap.add-Forge-to-database-types.patch
Patch2:          pdfbook-command-injection.patch
Patch3:          pdfbook-images-private-wiki.patch

BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:       noarch
AutoReqProv:     no

Requires:        php(language) >= 5.3
Requires:        ImageMagick, htmldoc

%description
php-mediawiki-tuleap is a mediawiki instance for Tuleap use. It aims to provide
mediawiki integration within Tuleap's hosted projects.

%prep
%setup -qn mediawiki-%{version}
cd extensions
%{__tar} -xzf %{_sourcedir}/SyntaxHighlight_GeSHi-REL1_23-4959271.tar.gz
%{__tar} -xzf %{_sourcedir}/PdfBook-REL1_23-17d1dfd.tar.gz
%{__tar} -xzf %{_sourcedir}/LabeledSectionTransclusion-REL1_23-98e6ab8.tar.gz
%{__tar} -xzf %{_sourcedir}/CategoryTree-REL1_23-c7333ea.tar.gz
%{__tar} -xzf %{_sourcedir}/Cite-REL1_23-2342915.tar.gz
%{__tar} -xzf %{_sourcedir}/ImageMap-REL1_23-1f17b01.tar.gz
cd %{_builddir}/mediawiki-%{version}

%patch0
%patch1 -p1
%patch2
%patch3

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/mediawiki-tuleap-123
%{__cp} -pr * $RPM_BUILD_ROOT%{_datadir}/mediawiki-tuleap-123
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/mediawiki-tuleap-123/extensions/SyntaxHighlight_GeSHi/.git
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/mediawiki-tuleap-123/extensions/PdfBook/.git
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/mediawiki-tuleap-123/tests

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/mediawiki-tuleap-123
%doc docs

%changelog
* Wed Sep 20 2017 Thomas Gerbet <thomas.gerbet@enalean.com> - 1.23.9-4
- request #10642: Images of non public Mediawiki are not exported when using the "print as pdf" feature

* Mon Sep 11 2017 Thomas Gerbet <thomas.gerbet@enalean.com> - 1.23.9-3
- request #10637: OS command injection through the print as PDF feature in Mediawiki

* Tue Apr 08 2015 Martin GOYOT <martin.goyot@enalean.com> - 1.23.9-2
- Add patch that add 'forge' database type

* Tue Apr 07 2015 Manuel VACELET <manuel.vacelet@enalean.com> - 1.23.9-1
- Bump version

* Fri Feb 06 2015 Yannis ROSSETTO <yannis.rossetto@enalean.com> - 1.20.3-6
- Add LabeledSectionTransclusion extension
- Add CategoryTree extension
- Add Cite extension
- Add ImageMap extension
- Add InputBox extension

* Wed Oct 29 2014 Manuel VACELET <manuel.vacelet@enalean.com> - 1.20.3-5
- Repackage with separation between upstream and added extensions
- Add patch for http://www.mediawiki.org/wiki/Extension_talk:PdfBook#Problem_in_pdfbook_if_only_current_page_should_be_converted

* Tue Apr 16 2013 Manuel VACELET <manuel.vacelet@enalean.com> - 1.20.3-3
- Move to centos6

* Tue Apr 2 2013 Manuel VACELET <manuel.vacelet@enalean.com> - 1.20.3-2
- Thumbnail generator requires ImageMagick

* Thu Mar 21 2013 Martin GOYOT <martin.goyot@enalean.com> - 1.20.3-1
- initial build <3
