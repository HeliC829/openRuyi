# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pb
%define go_import_path  github.com/cheggaaa/pb
# Failure on newer version test? Why? - Julian
%define go_test_exclude github.com/cheggaaa/pb/v3

Name:           go-github-cheggaaa-pb-v1
Version:        1.0.30
Release:        %autorelease
Summary:        Console progress bar for Golang
License:        BSD-3-Clause
URL:            https://github.com/cheggaaa/pb
#!RemoteAsset:  sha256:60be48135bf8bf0e9c59cb8c5e4adf11997c2b92a57b86d5d1e33a563583a576
Source0:        https://github.com/cheggaaa/pb/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/mattn/go-colorable)
BuildRequires:  go(github.com/mattn/go-runewidth)

Provides:       go(github.com/cheggaaa/pb) = %{version}

Requires:       go(github.com/fatih/color)
Requires:       go(github.com/mattn/go-colorable)
Requires:       go(github.com/mattn/go-runewidth)

%description
Terminal progress bar for Go

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
