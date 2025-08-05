# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname markdown

Name:           python-%{srcname}
Version:        3.8.2
Release:        %autorelease
Summary:        Markdown implementation in Python
License:        BSD-3-Clause
URL:            https://python-markdown.github.io/
# TODO: Use %%{pypi_source %%{srcname} %%{version}} in the future - 251
#       Otherwise https://files.pythonhosted.org/packages/source/a/abc/%%{srcname}-%%{version}.tar.gz
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-PyYAML
BuildRequires:  expat

%description
This is a Python implementation of John Gruberâ€™s Markdown. It is
almost completely compliant with the reference implementation, though
there are a few very minor differences.

%package     -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
This is a Python implementation of John Gruberâ€™s Markdown. It is
almost completely compliant with the reference implementation, though
there are a few very minor differences.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

# process license file
PYTHONPATH=%{buildroot}%{python3_sitelib} \
  %{buildroot}%{_bindir}/markdown_py \
  LICENSE.md > LICENSE.html

%files -n python3-%{srcname} -f %{pyproject_files}
# temporarily skip packaging docs - see also
# https://github.com/Python-Markdown/markdown/issues/621
#doc python3/build/docs/*
%license LICENSE.html LICENSE.md
%{_bindir}/markdown_py

%changelog
%{?autochangelog}
