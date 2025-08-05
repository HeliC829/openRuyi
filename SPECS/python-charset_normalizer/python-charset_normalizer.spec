# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname charset_normalizer

Name:           python-%{srcname}
Version:        3.4.3
Release:        %autorelease
License:        MIT
URL:            https://github.com/ousret/charset_normalizer
Summary:        Universal Charset Detector, alternative to Chardet
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pytest
BuildRequires:  python3-devel
BuildSystem:    pyproject
BuildOption(install): -l %{srcname} +auto
%description
A library that helps you read text from an unknown charset encoding.
Motivated by chardet, trying to resolve the issue by taking
a new approach. All IANA character set names for which the Python core
library provides codecs are supported.

%prep -a
# Drop mypy from build dependencies
sed -i 's/"mypy.*"//' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -r

%check
%pytest

%files -f %{pyproject_files}
%doc README*
%{_bindir}/normalizer

%changelog
%{?autochangelog}
