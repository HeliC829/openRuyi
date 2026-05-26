# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vergen-lib
%global full_version 9.1.0
%global pkgname vergen-lib-9.0

Name:           rust-vergen-lib-9.0
Version:        9.1.0
Release:        %autorelease
Summary:        Rust crate "vergen-lib"
License:        MIT OR Apache-2.0
URL:            https://github.com/rustyhorde/vergen
#!RemoteAsset:  sha256:b34a29ba7e9c59e62f229ae1932fb1b8fb8a6fdcc99215a641913f5f5a59a569
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1.0/default) >= 1.0.102
Requires:       crate(derive-builder-0.20/default) >= 0.20.2
Requires:       crate(rustversion-1.0/default) >= 1.0.22
Provides:       crate(vergen-lib) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/build)
Provides:       crate(%{pkgname}/cargo)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/emit-and-set)
Provides:       crate(%{pkgname}/git)
Provides:       crate(%{pkgname}/rustc)
Provides:       crate(%{pkgname}/si)
Provides:       crate(%{pkgname}/unstable)

%description
Source code for takopackized Rust crate "vergen-lib"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
