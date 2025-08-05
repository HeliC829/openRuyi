# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           rdfind
Version:        1.7.0
Release:        %autorelease
Summary:        Find duplicate files utility
License:        GPL-2.0-or-later
URL:            https://rdfind.pauldreik.se/
#!RemoteAsset
Source0:        https://rdfind.pauldreik.se/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://rdfind.pauldreik.se/%{name}-%{version}.tar.gz.asc

BuildSystem:    autotools

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  nettle-devel

%description
Rdfind is a program that finds duplicate files. It is useful for compressing
backup directories or just finding duplicate files. It compares files based on
their content, NOT on their file names.

%files
%license COPYING LICENSE
%doc AUTHORS ChangeLog
%{_bindir}/rdfind
%{_mandir}/man1/rdfind.1*

%changelog
%{?autochangelog}
