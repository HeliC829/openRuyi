# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name imperative
%global full_version 1.0.7
%global pkgname imperative-1.0

Name:           rust-imperative-1.0
Version:        1.0.7
Release:        %autorelease
Summary:        Rust crate "imperative"
License:        MIT OR Apache-2.0
URL:            https://github.com/crate-ci/imperative
#!RemoteAsset:  sha256:35e1d0bd9c575c52e59aad8e122a11786e852a154678d0c86e9e243d55273970
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(phf-0.13/default) >= 0.13.1
Requires:       crate(rust-stemmers-1.0/default) >= 1.2.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "imperative"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
