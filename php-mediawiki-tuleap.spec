Name:            php-mediawiki-tuleap
Version:         1.20.3
Release:         6%{?dist}
Summary:         A wiki engine

Group:           Development/Tools
License:         GPLv2+
URL:             http://www.mediawiki.org
Source0:         mediawiki-%{version}.tar.gz
Source1:         https://extdist.wmflabs.org/dist/SyntaxHighlight_GeSHi-REL1_20-8c017a6.tar.gz
Source2:         https://extdist.wmflabs.org/dist/PdfBook-REL1_23-17d1dfd.tar.gz
Source3:	 https://extdist.wmflabs.org/dist/extensions/LabeledSectionTransclusion-REL1_20-634472d.tar.gz
Source4:	 https://extdist.wmflabs.org/dist/extensions/CategoryTree-REL1_20-f5d36e1.tar.gz
Source5:	 https://extdist.wmflabs.org/dist/extensions/Cite-REL1_20-aa635f0.tar.gz
Source6:	 https://extdist.wmflabs.org/dist/extensions/ImageMap-REL1_20-50d05ff.tar.gz
Source7:	 https://extdist.wmflabs.org/dist/extensions/InputBox-REL1_20-118f3c6.tar.gz
Patch0:          php-mediawiki-tuleap.only_current_page_should_be_converted.patch

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
%{__tar} -xzf %{_sourcedir}/SyntaxHighlight_GeSHi-REL1_20-8c017a6.tar.gz
%{__tar} -xzf %{_sourcedir}/PdfBook-REL1_23-17d1dfd.tar.gz
%{__tar} -xzf %{_sourcedir}/LabeledSectionTransclusion-REL1_20-634472d.tar.gz
%{__tar} -xzf %{_sourcedir}/CategoryTree-REL1_20-f5d36e1.tar.gz
%{__tar} -xzf %{_sourcedir}/Cite-REL1_20-aa635f0.tar.gz
%{__tar} -xzf %{_sourcedir}/ImageMap-REL1_20-50d05ff.tar.gz
%{__tar} -xzf %{_sourcedir}/InputBox-REL1_20-118f3c6.tar.gz
cd %{_builddir}/mediawiki-%{version}

%patch0

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/mediawiki-tuleap
%{__cp} -pr * $RPM_BUILD_ROOT%{_datadir}/mediawiki-tuleap
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/mediawiki-tuleap/extensions/SyntaxHighlight_GeSHi/.git
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/mediawiki-tuleap/extensions/PdfBook/.git
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/mediawiki-tuleap/tests

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/mediawiki-tuleap
%doc docs

%changelog
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
