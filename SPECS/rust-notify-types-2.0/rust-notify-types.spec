# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name notify-types
%global full_version 2.1.0
%global pkgname notify-types-2.0

Name:           rust-notify-types-2.0
Version:        2.1.0
Release:        %autorelease
Summary:        Rust crate "notify-types"
License:        MIT OR Apache-2.0
URL:            https://github.com/notify-rs/notify
#!RemoteAsset:  sha256:42b8cfee0e339a0337359f3c88165702ac6e600dc01c0cc9579a92d62b08477a
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.11.1
Provides:       crate(notify-types) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/serialization-compat-6)

%description
Source code for takopackized Rust crate "notify-types"

%package     -n %{name}+serde
Summary:        Types used by the notify crate - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(bitflags-2.0/serde) >= 2.11.1
Requires:       crate(serde-1.0/default) >= 1.0.89
Requires:       crate(serde-1.0/derive) >= 1.0.89
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust notify-types crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+web-time
Summary:        Types used by the notify crate - feature "web-time"
Requires:       crate(%{pkgname})
Requires:       crate(web-time-1.0/default) >= 1.1.0
Provides:       crate(%{pkgname}/web-time)

%description -n %{name}+web-time
This metapackage enables feature "web-time" for the Rust notify-types crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
