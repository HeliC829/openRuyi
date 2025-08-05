# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lshw
Version:        B.02.20
Release:        %autorelease
Summary:        Hardware lister
License:        GPL-2.0-only
URL:            https://ezix.org/project/wiki/HardwareLiSter
#!RemoteAsset
Source:         https://www.ezix.org/software/files/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  gettext-devel

# Define common arguments for make
%global make_args PREFIX="%{_prefix}" SBINDIR="%{_sbindir}" MANDIR="%{_mandir}" DATADIR="%{_datadir}" VERSION="%{version}"

# Pass these arguments to the build and install steps
BuildOption(build):   %{make_args}
BuildOption(install): %{make_args}

%description
lshw (Hardware Lister) is a small tool to provide detailed information
on the hardware configuration of the machine. It can report exact memory
configuration, firmware version, mainboard configuration, CPU version
and speed, cache configuration, bus speed, etc.
This package provides the command-line interface only.

# No configure
%conf

# No tests
%check
:

%install -a
%find_lang %{name} --generate-subpackages

%files
%license COPYING
%doc README.md
%{_sbindir}/lshw
%{_datadir}/lshw/
%{_mandir}/man1/lshw.1*

%changelog
%{?autochangelog}
