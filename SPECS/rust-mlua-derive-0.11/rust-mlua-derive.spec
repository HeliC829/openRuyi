# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mlua_derive
%global full_version 0.11.0
%global pkgname mlua-derive-0.11

Name:           rust-mlua-derive-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "mlua_derive"
License:        MIT
URL:            https://github.com/mlua-rs/mlua
#!RemoteAsset:  sha256:465bddde514c4eb3b50b543250e97c1d4b284fa3ef7dc0ba2992c77545dbceb2
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(proc-macro2-1.0/span-locations) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Provides:       crate(mlua-derive) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "mlua_derive"

%package     -n %{name}+itertools
Summary:        Procedural macros for the mlua crate - feature "itertools"
Requires:       crate(%{pkgname})
Requires:       crate(itertools-0.14/default) >= 0.14.0
Provides:       crate(%{pkgname}/itertools)

%description -n %{name}+itertools
This metapackage enables feature "itertools" for the Rust mlua_derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        Procedural macros for the mlua crate - feature "macros"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/itertools)
Requires:       crate(%{pkgname}/once-cell)
Requires:       crate(%{pkgname}/proc-macro-error2)
Requires:       crate(%{pkgname}/regex)
Provides:       crate(%{pkgname}/macros)

%description -n %{name}+macros
This metapackage enables feature "macros" for the Rust mlua_derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Procedural macros for the mlua crate - feature "once_cell"
Requires:       crate(%{pkgname})
Requires:       crate(once-cell-1.0/default) >= 1.21.4
Provides:       crate(%{pkgname}/once-cell)

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust mlua_derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc-macro-error2
Summary:        Procedural macros for the mlua crate - feature "proc-macro-error2"
Requires:       crate(%{pkgname})
Requires:       crate(proc-macro-error2-2.0/default) >= 2.0.1
Provides:       crate(%{pkgname}/proc-macro-error2)

%description -n %{name}+proc-macro-error2
This metapackage enables feature "proc-macro-error2" for the Rust mlua_derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Procedural macros for the mlua crate - feature "regex"
Requires:       crate(%{pkgname})
Requires:       crate(regex-1.0/default) >= 1.12.3
Provides:       crate(%{pkgname}/regex)

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust mlua_derive crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
