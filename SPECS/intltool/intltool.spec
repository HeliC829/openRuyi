# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           intltool
Version:        0.51.0
Release:        %autorelease
Summary:        Utility scripts for internationalizing XML
License:        GPL-2.0-or-later
URL:            https://launchpad.net/intltool
#!RemoteAsset
Source:         https://launchpad.net/intltool/trunk/%{version}/+download/intltool-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:        perl perl(XML::Parser)
Requires:       automake gettext-devel perl(XML::Parser) perl(Getopt::Long) patch

%description
Intltool is a collection of scripts that helps with extracting translatable
strings from various source files, and merging them back into template files.

%files
%doc README
%license COPYING AUTHORS
%{_bindir}/intltool*
%{_datadir}/intltool
%{_datadir}/aclocal/intltool*
%{_mandir}/man8/*

%changelog
%{?autochangelog}
