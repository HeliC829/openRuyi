# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname decorator

Name:           python-%{srcname}
Version:        5.2.1
Release:        %autorelease
License:        BSD-2-Clause
URL:            https://pypi.org/project/decorator/
Summary:        Python module to simplify usage of decorators
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildSystem:    pyproject
BuildOption(install): -l %{srcname} +auto
%description
The aim of the decorator module is to simplify the usage of decorators
for the average programmer, and to popularize decorators usage giving examples
of useful decorators, such as memoize, tracing, redirecting_stdout, locked,
etc.  The core of this module is a decorator factory.

%generate_buildrequires
%pyproject_buildrequires

%check -a
%{py3_test_envvars} %{python3} -m unittest tests/test.py

%files -f %{pyproject_files}
%doc README.rst CHANGES.md
%license LICENSE.txt

%changelog
%{?autochangelog}
