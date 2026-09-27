# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           log
%define go_import_path  github.com/containerd/log

Name:           go-github-containerd-log
Version:        0.2.0
Release:        %autorelease
Summary:        Context-aware logging package for containerd
License:        Apache-2.0
URL:            https://github.com/containerd/log
#!RemoteAsset:  sha256:cf5bc961b0f85429560058ce3ea416d61ed7808a4e741fb905f8e50fc48a692c
Source0:        https://github.com/containerd/log/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/containerd/log) = %{version}

Requires:       go(github.com/sirupsen/logrus)
Requires:       go(golang.org/x/sys)

%description
Package log provides context-aware logging helpers used by containerd.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
