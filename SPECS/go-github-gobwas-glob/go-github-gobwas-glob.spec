# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           glob
%define go_import_path  github.com/gobwas/glob

Name:           go-github-gobwas-glob
Version:        1.0.0
Release:        %autorelease
Summary:        Go glob
License:        MIT
URL:            https://github.com/gobwas/glob
#!RemoteAsset:  sha256:c9a0c70b666b19250f5a5b8294b3915148801f2678588c7c0eb17b5d699fb224
Source0:        https://github.com/gobwas/glob/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Go 1.25 vet rejects non-constant fmt.Fprintf format strings. - HNO3Miracle
Patch2000:      2000-fix-non-constant-fprintf-format.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/gobwas/glob) = %{version}

%description
glob provides glob pattern matching for Go.

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
