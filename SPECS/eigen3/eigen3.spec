# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           eigen3
Version:        5.0.0
Release:        %autorelease
Summary:        A lightweight C++ template library for vector and matrix math
License:        MPL-2.0 AND LGPL-2.1-or-later AND BSD-3-Clause
URL:            http://eigen.tuxfamily.org/index.php?title=Main_Page
#!RemoteAsset
Source0:        https://gitlab.com/libeigen/eigen/-/archive/%{version}/eigen-%{version}.tar.bz2
BuildSystem:    cmake

BuildOption(conf): -DINCLUDE_INSTALL_DIR:PATH=%{_includedir}/eigen3

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Eigen is a C++ template library for linear algebra: matrices, vectors,
numerical solvers, and related algorithms. This package contains the
header files needed for development.

%files
%license COPYING.README COPYING.BSD COPYING.MPL2
%{_includedir}/eigen3/
%dir %{_datadir}/eigen3
%{_datadir}/eigen3/cmake/
%{_datadir}/pkgconfig/eigen3.pc

%changelog
%{?autochangelog}
