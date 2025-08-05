# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname filelock

Name:           python-%{srcname}
Version:        3.16.1
Release:        %autorelease
License:        Unlicense
URL:            https://github.com/tox-dev/py-filelock
Summary:        Platform independent file lock
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildSystem:    pyproject
BuildOption(install): -l %{srcname} +auto
%description
@code{filelock} contains a single module implementing
a platform independent file lock in Python, which provides a simple way of
inter-process communication.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%{?autochangelog}
