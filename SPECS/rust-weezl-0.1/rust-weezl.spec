# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name weezl
%global full_version 0.1.12
%global pkgname weezl-0.1

Name:           rust-weezl-0.1
Version:        0.1.12
Release:        %autorelease
Summary:        Rust crate "weezl"
License:        MIT OR Apache-2.0
URL:            https://github.com/image-rs/weezl
#!RemoteAsset:  sha256:a28ac98ddc8b9274cb41bb4d9d4d5c425b6020c50c46f25559911905610b4a88
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(weezl) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "weezl"

%package     -n %{name}+async
Summary:        Fast LZW compression and decompression - feature "async"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/async)

%description -n %{name}+async
This metapackage enables feature "async" for the Rust weezl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Fast LZW compression and decompression - feature "futures"
Requires:       crate(%{pkgname})
Requires:       crate(futures-0.3/std) >= 0.3.12
Provides:       crate(%{pkgname}/futures)

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust weezl crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
