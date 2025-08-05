# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           kyua
Version:        0.14.1
Release:        %autorelease
Summary:        A testing framework for infrastructure software
License:        BSD-2-Clause
URL:            https://github.com/jmmv/kyua
#!RemoteAsset
Source:         https://github.com/freebsd/kyua/archive/refs/tags/kyua-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf): --with-atf=yes
BuildOption(conf): --without-doxygen

BuildOption(build):   pkgtestsdir=%{_libexecdir}/%{name}/tests
BuildOption(build):   testsdir=%{_libexecdir}/%{name}/tests
BuildOption(install): pkgtestsdir=%{_libexecdir}/%{name}/tests
BuildOption(install): testsdir=%{_libexecdir}/%{name}/tests

BuildRequires:  make gcc-c++ autoconf automake libtool
BuildRequires:  libatf-c++-devel >= 0.17
BuildRequires:  libatf-sh-devel >= 0.15
BuildRequires:  pkgconfig(lutok) >= 0.4
BuildRequires:  pkgconfig(sqlite3) >= 3.6.22

%description
Kyua is a testing framework for infrastructure software, originally designed
to equip BSD-based operating systems with a test suite.

%conf -p
autoreconf -fiv

%files
%license LICENSE
%doc %{_docdir}/kyua
%doc AUTHORS CONTRIBUTORS NEWS.md README.md
%{_bindir}/kyua
%{_datadir}/kyua/
%{_mandir}/man1/kyua*.1*
%{_mandir}/man5/kyua*.5*

%changelog
%{?autochangelog}
