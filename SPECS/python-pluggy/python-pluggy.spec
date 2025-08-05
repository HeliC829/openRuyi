# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pluggy

Name:           python-%{srcname}
Version:        1.6.0
Release:        %autorelease
Summary:        The plugin manager stripped of pytest specific details
License:        MIT
URL:            https://github.com/pytest-dev/pluggy
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  pluggy

BuildRequires:  python3-devel
BuildRequires:  python3-packaging
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-setuptools_scm+toml
BuildRequires:  expat

%description
The plugin manager stripped of pytest specific details.

%package     -n python3-pluggy
Summary:        %{summary}

%description -n python3-pluggy
The plugin manager stripped of pytest specific details.

%files -n python3-pluggy -f %{pyproject_files}
%doc README.rst

%changelog
%{?autochangelog}
