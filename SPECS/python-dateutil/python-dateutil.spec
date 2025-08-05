# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname dateutil

Name:           python-%{srcname}
Version:        2.9.0.post0
Release:        %autorelease
Summary:        Powerful extensions to the standard datetime module
License:        (Apache-2.0 AND BSD-3-Clause) OR BSD-3-Clause
URL:            https://github.com/dateutil/dateutil
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

# Otherwise will nothing provides python3dist(setuptools-scm) < 8~~
Patch0:         0001-relax-setuptools_scm-requires.patch
# Fix sphinx import path
Patch1:         0002-fix-sphinx-import.patch

BuildRequires:  python3-devel
BuildRequires:  python3-PyYAML
BuildRequires:  expat

%description
The dateutil module provides powerful extensions to the standard datetime
module available in Python.

%package     -n python3-%{srcname}
Summary:        Powerful extensions to the standard datetime module
Requires:       tzdata

%description -n python3-%{srcname}
The dateutil module provides powerful extensions to the standard datetime
module available in Python.

%prep
%autosetup -p1 -n %{name}-%{version}
# Convert NEWS file to UTF-8
iconv --from=ISO-8859-1 --to=UTF-8 NEWS > NEWS.new
mv NEWS.new NEWS

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
#make -C docs html

%install
%pyproject_install
%pyproject_save_files %{srcname} -l

%files -n python3-%{srcname} -f %{pyproject_files}
%doc NEWS README.rst
#doc docs/_build/html
%license LICENSE

%changelog
%{?autochangelog}
