%global kodi_addon pvr.vbox
%global kodi_version 21
%global kodi_codename Omega

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
Version:        21.1.5
Release:        3%{?dist}
Summary:        VBox Home TV Gateway PVR client for Kodi

License:        GPL-2.0-or-later
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        %{url}/archive/%{version}-%{kodi_codename}/%{kodi_addon}-%{version}.tar.gz
Source1:        %{name}.metainfo.xml

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(tinyxml2)
Requires:       kodi >= %{kodi_version}
ExcludeArch:    %{power64}

%description
%{summary}.


%prep
%autosetup -n %{kodi_addon}-%{version}-%{kodi_codename} -p0


%build
%cmake
%cmake_build


%install
%cmake_install
# Install AppData file
install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_metainfodir}/%{name}.metainfo.xml


%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/%{name}.metainfo.xml


%files
%doc README.md %{kodi_addon}/changelog.txt
%license LICENSE.md
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/
%{_metainfodir}/%{name}.metainfo.xml


%changelog
* Sun Aug 24 2025 Leigh Scott <leigh123linux@gmail.com> - 21.1.5-3
- Rebuild for new libtinyxml2

* Sun Jul 27 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 21.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Mar 29 2025 Leigh Scott <leigh123linux@gmail.com> - 21.1.5-1
- Update to 21.1.5

* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 21.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 21.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 14 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 21.1.2-1
- Update to 21.1.2

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 20.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 20.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 27 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 20.4.2-1
- Update to 20.4.2

* Sun Feb 12 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.4.0-1
- Update to 20.4.0

* Sun Jan 29 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 20.3.0-1
- Update to 20.3.0
- Add AppStream metadata
- Switch to SPDX license identifiers

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 8.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 8.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 8.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 8.1.2-1
- Update to 8.1.2

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 8.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 29 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 8.1.0-1
- Update to 8.1.0

* Mon Nov 16 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 8.0.0-1
- Update to 8.0.0

* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 7.0.0-1
- Update to 7.0.0 (switch to Matrix branch)

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.7.0-1
- Update to 4.7.0

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.4.5-2
- Enable arm build

* Sat Sep 01 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 4.4.5-1
- Update to 4.4.5
- Enable aarch64 build

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
