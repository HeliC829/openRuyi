# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-sqlite3
%define go_import_path  github.com/mattn/go-sqlite3

Name:           go-github-mattn-go-sqlite3
Version:        1.14.52
Release:        %autorelease
Summary:        SQLite3 driver for Go
License:        MIT
URL:            https://github.com/mattn/go-sqlite3
#!RemoteAsset:  sha256:2f775dc697c4e3b53fad106a6db17c585a801d0c4db61c9b62a684a886b367bf
Source0:        https://github.com/mattn/go-sqlite3/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Fix go vet: Errorf format %q has an argument of wrong type int64.
Patch2000:      2000-tests-format-integer-results.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
# Timezone tests fail with unknown time zone US/Central and Asia/Tokyo.
BuildRequires:  tzdata

Provides:       go(github.com/mattn/go-sqlite3) = %{version}

%description
SQLite3 driver implementing the Go database/sql interface using cgo.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
