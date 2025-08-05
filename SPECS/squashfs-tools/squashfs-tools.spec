# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           squashfs-tools
Version:        4.7.2
Release:        %autorelease
Summary:        Utilities for the SquashFS read-only filesystem
License:        GPL-2.0-or-later
URL:            https://github.com/plougher/squashfs-tools
#!RemoteAsset
Source0:        https://github.com/plougher/squashfs-tools/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build): -C squashfs-tools LZMA_XZ_SUPPORT=1 XZ_SUPPORT=1 LZO_SUPPORT=1 LZ4_SUPPORT=1 ZSTD_SUPPORT=1
BuildOption(install): -C squashfs-tools INSTALL_DIR=%{buildroot}%{_bindir} INSTALL_MANPAGES_DIR=%{buildroot}%{_mandir}

BuildRequires:  lz4-devel
BuildRequires:  lzma-devel
BuildRequires:  lzo-devel
BuildRequires:  libzstd-devel
BuildRequires:  zlib-devel

Provides:       squashfs
Supplements:    filesystem(squashfs)

%description
This package contains the userland utilities (mksquashfs, unsquashfs)
to create and read SquashFS images. SquashFS is a highly compressed
read-only filesystem for Linux.

# No configure
%conf

%build -p
sed -i -e "s|-O2|%{optflags}|" squashfs-tools/Makefile

# no check target
%check

%files
%license COPYING
%{_bindir}/mksquashfs
%{_bindir}/unsquashfs
%{_bindir}/sqfstar
%{_bindir}/sqfscat
%{_mandir}/*.1.gz

%changelog
%{?autochangelog}
