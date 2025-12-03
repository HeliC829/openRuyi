# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond x11 0

Name:           vulkan-validation-layers
Version:        1.4.335.0
Release:        %autorelease
Summary:        Vulkan validation layers
License:        Apache-2.0
URL:            https://github.com/KhronosGroup/Vulkan-ValidationLayers
#!RemoteAsset
Source0:        https://github.com/KhronosGroup/Vulkan-ValidationLayers/archive/refs/tags/vulkan-sdk-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_WERROR=OFF
BuildOption(conf):  -DGLSLANG_INSTALL_DIR=%{_prefix}
BuildOption(conf):  -DBUILD_LAYER_SUPPORT_FILES:BOOL=ON
BuildOption(conf):  -DUSE_ROBIN_HOOD_HASHING:BOOL=OFF
BuildOption(conf):  -DSPIRV_HEADERS_INSTALL_DIR=%{_prefix}
BuildOption(conf):  -DVULKAN_HEADERS_INSTALL_DIR=%{_prefix}
BuildOption(conf):  -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}
BuildOption(conf):  -DBUILD_WSI_WAYLAND_SUPPORT=ON

%if %{with x11}
BuildOption(conf):  -DBUILD_WSI_XCB_SUPPORT=ON
BuildOption(conf):  -DBUILD_WSI_XLIB_SUPPORT=ON
%else
BuildOption(conf):  -DBUILD_WSI_XCB_SUPPORT=OFF
BuildOption(conf):  -DBUILD_WSI_XLIB_SUPPORT=OFF
%endif

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig(python3)
BuildRequires:  vulkan-headers
BuildRequires:  vulkan-loader-devel
BuildRequires:  vulkan-utility-libraries-devel
BuildRequires:  spirv-tools-devel
BuildRequires:  spirv-headers-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)

%if %{with x11}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xcb)
%endif

%description
Vulkan validation layers.

%files
%license LICENSE.txt
%doc README.md CONTRIBUTING.md
%{_datadir}/vulkan/explicit_layer.d/*.json
%{_libdir}/libVkLayer_*.so

%changelog
%{?autochangelog}
