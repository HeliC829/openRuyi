# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           rust-rpm-macros
Version:        0.1
Release:        %autorelease
Summary:        Rust macros for openRuyi packaging
License:        MIT
# TODO: Update the URL when there is a proper project page
URL:            https://git.openruyi.cn/openRuyi/rust-rpm-macros
#!RemoteAsset:  sha256:cb488b3b6aaf219948a0695b94423118801ab77c8eb3ae2ecb95d8081cb4b770
Source0:        https://git.openruyi.cn/openRuyi/rust-rpm-macros/archive/%{version}.tar.gz
BuildArch:      noarch

%description
This package provides RPM macros for packaging Rust software in openRuyi.

%prep
%autosetup -n %{name}

# No build needed
%build

%install
install -D -m644 macros.buildsystem.rustcrates %{buildroot}%{_rpmmacrodir}/macros.buildsystem.rustcrates

# No check needed
%check

%files
%license LICENSE
%{_rpmmacrodir}/macros.buildsystem.rustcrates

%changelog
%{?autochangelog}
