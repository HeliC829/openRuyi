# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name codspeed-divan-compat
%global full_version 4.4.1
%global pkgname codspeed-divan-compat-4.0

Name:           rust-codspeed-divan-compat-4.0
Version:        4.4.1
Release:        %autorelease
Summary:        Rust crate "codspeed-divan-compat"
License:        MIT OR Apache-2.0
URL:            https://codspeed.io
#!RemoteAsset:  sha256:89e4bf8c7793c170fd0fcf3be97b9032b2ae39c2b9e8818aba3cc10ca0f0c6c0
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(clap-4.0/env) >= 4.6.1
Requires:       crate(clap-4.0/std) >= 4.6.1
Requires:       crate(codspeed-4.0/default) >= 4.4.1
Requires:       crate(codspeed-divan-compat-macros-4.0/default) >= 4.4.1
Requires:       crate(codspeed-divan-compat-walltime-4.0/default) >= 4.4.1
Requires:       crate(regex-1.0/default) >= 1.12.3
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "codspeed-divan-compat"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
