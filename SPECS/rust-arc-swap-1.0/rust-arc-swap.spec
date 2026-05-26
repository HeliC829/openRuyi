# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arc-swap
%global full_version 1.9.1
%global pkgname arc-swap-1.0

Name:           rust-arc-swap-1.0
Version:        1.9.1
Release:        %autorelease
Summary:        Rust crate "arc-swap"
License:        MIT OR Apache-2.0
URL:            https://github.com/vorner/arc-swap
#!RemoteAsset:  sha256:6a3a1fd6f75306b68087b831f025c712524bcb19aad54e557b1129cfa0a2b207
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustversion-1.0/default) >= 1.0.22
Provides:       crate(arc-swap) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/experimental-strategies)
Provides:       crate(%{pkgname}/experimental-thread-local)
Provides:       crate(%{pkgname}/internal-test-strategies)
Provides:       crate(%{pkgname}/weak)

%description
Source code for takopackized Rust crate "arc-swap"

%package     -n %{name}+serde
Summary:        Atomically swappable Arc - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/rc) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust arc-swap crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
