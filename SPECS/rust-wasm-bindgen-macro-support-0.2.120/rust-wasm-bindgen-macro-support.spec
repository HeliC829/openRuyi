# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-bindgen-macro-support
%global full_version 0.2.120
%global pkgname wasm-bindgen-macro-support-0.2.120

Name:           rust-wasm-bindgen-macro-support-0.2.120
Version:        0.2.120
Release:        %autorelease
Summary:        Rust crate "wasm-bindgen-macro-support"
License:        MIT OR Apache-2.0
URL:            https://wasm-bindgen.github.io/wasm-bindgen/
#!RemoteAsset:  sha256:9dcd0ff20416988a18ac686d4d4d0f6aae9ebf08a389ff5d29012b05af2a1b41
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bumpalo-3.0/default) >= 3.20.2
Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Requires:       crate(syn-2.0/visit) >= 2.0.117
Requires:       crate(syn-2.0/visit-mut) >= 2.0.117
Requires:       crate(wasm-bindgen-shared-0.2.120/default) >= 0.2.120
Provides:       crate(wasm-bindgen-macro-support) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/strict-macro)

%description
Source code for takopackized Rust crate "wasm-bindgen-macro-support"

%package     -n %{name}+extra-traits
Summary:        Implementation APIs for the `#[wasm_bindgen]` attribute - feature "extra-traits"
Requires:       crate(%{pkgname})
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Requires:       crate(syn-2.0/visit) >= 2.0.117
Requires:       crate(syn-2.0/visit-mut) >= 2.0.117
Provides:       crate(%{pkgname}/extra-traits)

%description -n %{name}+extra-traits
This metapackage enables feature "extra-traits" for the Rust wasm-bindgen-macro-support crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
