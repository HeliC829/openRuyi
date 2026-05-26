# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name futures-executor
%global full_version 0.3.32
%global pkgname futures-executor-0.3

Name:           rust-futures-executor-0.3
Version:        0.3.32
Release:        %autorelease
Summary:        Rust crate "futures-executor"
License:        MIT OR Apache-2.0
URL:            https://rust-lang.github.io/futures-rs
#!RemoteAsset:  sha256:baf29c38818342a3b26b5b923639e7b1f4a61fc5e76102d4b1981c6dc7a7579d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-core-0.3) >= 0.3.32
Requires:       crate(futures-task-0.3) >= 0.3.32
Requires:       crate(futures-util-0.3) >= 0.3.32
Provides:       crate(futures-executor) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "futures-executor"

%package     -n %{name}+std
Summary:        Executors for asynchronous tasks based on the futures-rs library - feature "std" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(futures-core-0.3/std) >= 0.3.32
Requires:       crate(futures-task-0.3/std) >= 0.3.32
Requires:       crate(futures-util-0.3/std) >= 0.3.32
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/thread-pool)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust futures-executor crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "thread-pool" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
