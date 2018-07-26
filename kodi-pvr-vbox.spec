%global commit 57f31984008bac8047b6d74d338980b6dd9ebd28
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20180205

%global kodi_addon pvr.vbox
%global kodi_version 18.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
Version:        4.3.1
Release:        2%{?dist}
Summary:        VBox Home TV Gateway PVR client for Kodi

License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{shortcommit}/%{kodi_addon}-%{shortcommit}.tar.gz
# Use external tinyxml2 library
Patch0:         %{name}-4.3.1-use_external_tinyxml2.patch
# Fix build with tinyxml2 >= 6.0.0
Patch1:         %{name}-4.3.1-tinyxml2_6.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  pkgconfig(tinyxml2)
BuildRequires:  platform-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64

%description
%{summary}.


%prep
%autosetup -n %{kodi_addon}-%{commit} -p0

# Drop bundled tinyxml2 library
rm -r lib/tinyxml2/


%build
%cmake .
%make_build


%install
%make_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.3.1-1
- Update to latest stable release for Kodi 18

* Mon Mar 12 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.6.12-3
- Patch for new tinyxml2

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 3.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.6.12-1
- Update to 3.6.12

* Fri Apr 28 2017 Mohamed El Morabity <melmorabity@fedorapeople.org> - 3.6.10-1
- Update to latest stable release for Kodi 17

* Sat Jul 23 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.13-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.3.8-1
- Initial RPM release
