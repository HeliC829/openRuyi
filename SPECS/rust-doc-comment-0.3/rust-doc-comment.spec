# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name doc-comment
%global full_version 0.3.3
%global pkgname doc-comment-0.3

Name:           rust-doc-comment-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "doc-comment"
License:        MIT
URL:            https://github.com/GuillaumeGomez/doc-comment
#!RemoteAsset:  sha256:fea41bba32d969b513997752735605054bc0dfa92b4c56bf1189f2e174be7a10
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/no-core)
Provides:       crate(%{pkgname}/old-macros)

%description
Source code for takopackized Rust crate "doc-comment"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
