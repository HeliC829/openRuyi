# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name colored
%global full_version 3.1.1
%global pkgname colored-3.0

Name:           rust-colored-3.0
Version:        3.1.1
Release:        %autorelease
Summary:        Rust crate "colored"
License:        MPL-2.0
URL:            https://github.com/mackwic/colored
#!RemoteAsset:  sha256:faf9468729b8cbcea668e36183cb69d317348c2e08e994829fb56ebfdfbaac34
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(windows-sys-0.59/default) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-foundation) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-console) >= 0.59.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/no-color)

%description
Source code for takopackized Rust crate "colored"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
