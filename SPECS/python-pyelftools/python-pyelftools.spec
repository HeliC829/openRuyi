# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyelftools

Name:           python-%{srcname}
Version:        0.32
Release:        %autorelease
License:        Public-Domain
URL:            https://github.com/eliben/pyelftools
Summary:        Analyze binary and library file information
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildSystem:    pyproject
BuildOption(install): -l elftools +auto
%description
This Python library provides interfaces for parsing and analyzing two
binary and library file formats ; the Executable and Linking Format (ELF), and
debugging information in the Debugging With Attributed Record
Format (DWARF).

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README*

%changelog
%{?autochangelog}
