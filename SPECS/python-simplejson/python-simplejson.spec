# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: laokz <zhangkai@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname simplejson

Name:           python-%{srcname}
Version:        3.17.6
Release:        %autorelease
Summary:        Json library for Python
License:        (LicenseRef-Callaway-MIT OR LicenseRef-Callaway-AFL) AND (LicenseRef-Callaway-MIT OR GPL-2.0-only)
URL:            https://simplejson.readthedocs.io/en/latest
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

BuildRequires:  python3-devel
BuildSystem:    pyproject
BuildOption(install):  -l %{srcname}

%description
JSON (JavaScript Object Notation) is a subset of JavaScript
syntax (ECMA-262 3rd edition) used as a lightweight data interchange
format.

%package -n python3-%{srcname}
Summary:        Json library for Python

%description -n python3-%{srcname}
JSON (JavaScript Object Notation) is a subset of JavaScript
syntax (ECMA-262 3rd edition) used as a lightweight data interchange
format.

Simplejson exposes an API familiar to users of the standard library marshal
and pickle modules.  It is the externally maintained version of the json
library contained in Python 2.6, but maintains compatibility with Python 2.5
and (currently) has significant performance advantages, even without using
the optional C extension for speedups.  Simplejson is also supported on
Python 3.3+.

%generate_buildrequires
%pyproject_buildrequires

%files -n python3-%{srcname}  -f %{pyproject_files}
%license LICENSE*
%doc README*

%changelog
%{?autochangelog}
