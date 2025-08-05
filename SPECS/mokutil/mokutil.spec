# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:        mokutil
Version:     0.7.2
Release:     %autorelease
Summary:     Tools for manipulating machine owner keys
License:     GPLv3+
URL:         https://github.com/lcp/mokutil
#!RemoteAsset
Source0:     https://github.com/lcp/mokutil/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem: autotools

BuildRequires: gcc autoconf automake libtool
BuildRequires: openssl-devel keyutils-devel efivar-devel
BuildRequires: pkgconfig

%description
The utility to manipulate machine owner keys which are managed by shim.

%conf -p
autoreconf -fiv

%files
%license COPYING
%doc README
%{_bindir}/mokutil
%{_datadir}/bash-completion/completions/mokutil
%{_mandir}/man1/*

%changelog
%{?autochangelog}
