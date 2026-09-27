# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           stats
%define go_import_path  github.com/montanaflynn/stats

Name:           go-github-montanaflynn-stats
Version:        0.12.7
Release:        %autorelease
Summary:        Statistical functions for Go
License:        MIT
URL:            https://github.com/montanaflynn/stats
#!RemoteAsset:  sha256:da38706603fce9345062d156e1d2ac6b1598108675d305cf2220bd12af4bd413
Source0:        https://github.com/montanaflynn/stats/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Backport: https://github.com/montanaflynn/stats/pull/136
Patch1000:      1000-fix-non-constant-format-strings.patch
# Backport: https://github.com/montanaflynn/stats/pull/97
Patch1001:      1001-use-math-round.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/montanaflynn/stats) = %{version}

%description
Statistical functions for Go, including descriptive statistics,
distributions, regression and hypothesis testing.

%prep -a
# Standalone examples each define main and cannot form a single Go package.
rm -rf examples

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
