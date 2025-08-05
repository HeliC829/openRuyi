# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tdb
Version:        1.4.14
Release:        %autorelease
Summary:        A Trivial Database library
License:        LGPL-3.0-or-later
URL:            https://tdb.samba.org/
#!RemoteAsset
Source:         https://samba.org/ftp/tdb/tdb-%{version}.tar.gz

BuildSystem:    autotools

BuildOption(conf):    --disable-rpath --bundled-libraries=NONE --builtin-libraries=replace
BuildOption(conf):    --disable-python --without-gettext

BuildRequires:  python3

%description
The Tdb library implements a trivial database that is used by Samba and
other projects. It is extremely fast and designed for concurrent access.

%package tools
Summary:        Command-line tools for managing Tdb databases
Requires:       %{name} = %{version}

%description tools
This package contains tools to create, view, and manage Tdb database files,
such as tdbdump and tdbtool.

%package devel
Summary:        Development files for the Tdb library
Requires:       %{name} = %{version}
Requires:       tdb-tools = %{version}

%description devel
This package contains the header files, pkg-config file, and development
documentation needed to build applications that use the Tdb library.


%files
%license LICENSE
%{_libdir}/libtdb.so.*

%files tools
%{_bindir}/tdbbackup
%{_bindir}/tdbdump
%{_bindir}/tdbtool
%{_bindir}/tdbrestore
# Man pages disabled due to docbook dependency issues

%files devel
%{_includedir}/tdb.h
%{_libdir}/libtdb.so
%{_libdir}/pkgconfig/tdb.pc

%changelog
%{?autochangelog}
