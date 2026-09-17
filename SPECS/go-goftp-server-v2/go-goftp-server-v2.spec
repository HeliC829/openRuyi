# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           server
%define go_import_path  goftp.io/server/v2

Name:           go-goftp-server-v2
Version:        2.0.3
Release:        %autorelease
Summary:        Extensible FTP server framework for Go
License:        MIT
URL:            https://gitea.com/goftp/server
#!RemoteAsset:  sha256:e623afedc1b85320283300888e841f62795fbe552034648ff1dac4b375b13d6b
Source0:        https://gitea.com/goftp/server/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/jlaffaye/ftp)
BuildRequires:  go(github.com/minio/minio-go/v6)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(goftp.io/server/v2) = %{version}

Requires:       go(github.com/minio/minio-go/v6)

%description
FTP server framework with pluggable authentication, permissions and storage
drivers. Includes the filesystem and MinIO storage drivers.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
