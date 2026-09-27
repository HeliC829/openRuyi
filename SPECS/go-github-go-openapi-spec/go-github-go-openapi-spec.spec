# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           spec
%define go_import_path  github.com/go-openapi/spec

Name:           go-github-go-openapi-spec
Version:        1.0.1
Release:        %autorelease
Summary:        openapi specification object model
License:        Apache-2.0
URL:            https://github.com/go-openapi/spec
#!RemoteAsset:  sha256:04e3fa445aaedb76f6a6545243823eaa9f4112f5433e877982476c58dcbefcba
Source0:        https://github.com/go-openapi/spec/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-openapi/jsonpointer)
BuildRequires:  go(github.com/go-openapi/jsonreference)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/go-openapi/testify)
BuildRequires:  go(go.yaml.in/yaml/v3)

Provides:       go(github.com/go-openapi/spec) = %{version}

Requires:       go(github.com/go-openapi/jsonpointer)
Requires:       go(github.com/go-openapi/jsonreference)
Requires:       go(github.com/go-openapi/swag)
Requires:       go(github.com/go-openapi/testify)
Requires:       go(go.yaml.in/yaml/v3)

%description
The object model for OpenAPI v2 specification documents.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
