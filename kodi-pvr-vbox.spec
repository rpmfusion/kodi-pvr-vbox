%global commit 35dd90995f22dc3cb854380a659384bcffb0c59c
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20170704

%global kodi_addon pvr.vbox
%global kodi_version 17.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
Version:        3.6.12
Release:        1%{?dist}
Summary:        Kodi VBox TV Gateway PVR addon

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{short_commit}/%{name}-%{short_commit}.tar.gz
# Use external tinyxml2 library
Patch0:         %{name}-3.6.10-use_external_tinyxml2.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  pkgconfig(tinyxml2)
BuildRequires:  platform-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64

%description
This is a PVR addon for interfacing with VBox Communications' XTi TV
Gateways. It supports all the basic functionality you would expect, such as
watching, recording and timeshifting. Additionally, it supports augmenting the
over-the-air guide data with external XMLTV data.


%prep
%autosetup -n %{kodi_addon}-%{commit} -p0

# Drop bundled tinyxml2 library
rm -r lib/tinyxml2/


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}/kodi/ .
%make_build


%install
%make_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%license LICENSE.md
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Tue Oct 03 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.6.12-1
- Update to 3.6.12

* Fri Apr 28 2017 Mohamed El Morabity <melmorabity@fedorapeople.org> - 3.6.10-1
- Update to latest stable release for Kodi 17

* Sat Jul 23 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.13-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.3.8-1
- Initial RPM release
