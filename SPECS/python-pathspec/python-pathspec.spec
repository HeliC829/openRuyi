# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pathspec

Name:           python-%{srcname}
Version:        0.12.1
Release:        %autorelease
Summary:        Utility library for gitignore style pattern matching of file paths
License:        MIT
URL:            https://github.com/cpburnz/python-path-specification
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  pathspec

BuildRequires:  python3-devel
BuildRequires:  python3-packaging
BuildRequires:  python3-pip
BuildRequires:  python3-flit-core
BuildRequires:  expat

%generate_buildrequires
%pyproject_buildrequires

%description
Path Specification (pathspec) is a utility library for pattern matching of file
paths. So far this only includes Git's wildmatch pattern matching which itself
is derived from Rsync's wildmatch. Git uses wildmatch for its gitignore files.

%package     -n python3-pathspec
Summary:        %{summary}

%description -n python3-pathspec
Path Specification (pathspec) is a utility library for pattern matching of file
paths. So far this only includes Git's wildmatch pattern matching which itself
is derived from Rsync's wildmatch. Git uses wildmatch for its gitignore files.

%files -n python3-pathspec -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%{?autochangelog}
