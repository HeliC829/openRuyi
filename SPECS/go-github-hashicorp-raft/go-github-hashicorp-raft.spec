# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           raft
%define go_import_path  github.com/hashicorp/raft

Name:           go-github-hashicorp-raft
Version:        1.8.0
Release:        %autorelease
Summary:        Raft consensus library for Go
License:        MPL-2.0
URL:            https://github.com/hashicorp/raft
#!RemoteAsset:  sha256:3db7490c6d8376355792c5b37a792784847153d39b8792441425c3392e9b1ac5
Source0:        https://github.com/hashicorp/raft/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Partial backport: https://github.com/hashicorp/raft/pull/647
Patch1000:      1000-fix-format-strings.patch
# Partial backport: https://github.com/hashicorp/raft/pull/551
Patch1001:      1001-check-structured-snapshot-progress.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/armon/go-metrics)
BuildRequires:  go(github.com/hashicorp/go-hclog)
BuildRequires:  go(github.com/hashicorp/go-msgpack)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/hashicorp/raft) = %{version}

Requires:       go(github.com/armon/go-metrics)
Requires:       go(github.com/hashicorp/go-hclog)
Requires:       go(github.com/hashicorp/go-msgpack)

%description
Raft consensus implementation for replicated logs and finite state
machines, including network transports and snapshot management.

%prep -a
# fuzzy is an independently managed fuzz-test harness (fuzzy/go.mod),
# not part of the public Raft module. Keep the root module tests.
rm -rf fuzzy

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
