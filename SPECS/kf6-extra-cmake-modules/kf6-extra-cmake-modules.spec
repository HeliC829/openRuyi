# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           kf6-extra-cmake-modules
Version:        6.20.0
Release:        %autorelease
Summary:        CMake modules
License:        BSD-3-Clause
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/extra-cmake-modules
#!RemoteAsset
Source0:        https://invent.kde.org/frameworks/extra-cmake-modules/-/archive/v%{version}/extra-cmake-modules-%{version}.tar.gz
BuildSystem:    cmake


BuildRequires:  cmake >= 3.16
BuildRequires:  kf6-filesystem
BuildRequires:  gcc-c++
BuildRequires:  gcc-PIE
BuildRequires:  qt6-base

Requires:       gcc-c++
Requires:       gcc-PIE
Requires:       cmake >= 3.16
Requires:       kf6-filesystem
# BuildRequires:  python-sphinx

Provides:       extra-cmake-modules = %{version}
Obsoletes:      extra-cmake-modules < %{version}

BuildOption(conf): -DQT_MAJOR_VERSION=6

BuildArch: noarch

# TODO: Fix tests.
%check

%description
Extra modules and scripts for CMake.

%files
%license LICENSES/*
%{_datadir}/ECM/

%changelog
%{?autochangelog}
