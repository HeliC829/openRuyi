# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sharutils
Version:        4.15.2
Release:        %autorelease
Summary:        The GNU shar utilities for creating shell archives
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/sharutils/
#!RemoteAsset
Source0:        https://ftp.gnu.org/gnu/sharutils/sharutils-%{version}.tar.xz
BuildSystem:    autotools
Patch:          0001-backport-Fix-building-with-GCC-10.patch

BuildRequires:  autoconf automake libtool
BuildRequires:  gcc make
BuildRequires:  gettext-devel
BuildRequires:  texinfo

%description
This is the set of GNU shar utilities. shar makes shell archives out of many
files, preparing them for transmission by electronic mail services. Use unshar
to unpack shell archives after reception. uuencode and uudecode are also included.

%conf -p
# note: 'false' is a keyword with '-std=c23' onwards
export CFLAGS="%{optflags} -std=gnu99"
autoreconf -fiv

%install -a
rm -f %{buildroot}%{_infodir}/dir

%find_lang %{name} --generate-subpackages

%files
%license COPYING AUTHORS
%doc README ChangeLog NEWS THANKS TODO
%{_bindir}/*
%{_infodir}/*info*
%{_mandir}/man?/*

%changelog
%{?autochangelog}
