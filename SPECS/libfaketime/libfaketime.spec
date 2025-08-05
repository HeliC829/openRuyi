# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _test_target test

Name:           libfaketime
Version:        0.9.12
Release:        %autorelease
Summary:        FakeTime Preload Library
License:        GPL-2.0-only
URL:            https://github.com/wolfcw/libfaketime
#!RemoteAsset
Source:         https://github.com/wolfcw/libfaketime/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):   PREFIX=%{_prefix}
BuildOption(build):   LIBDIRNAME=%{_libdir}/%{name}
BuildOption(install): DESTDIR=%{buildroot}
BuildOption(install): PREFIX=%{_prefix}
BuildOption(install): LIBDIRNAME=/%{_lib}

%description
libfaketime allows you to report a faked system time to programs without
having to change the system-wide time, using a preload library.

# No configure
%conf

%files
%doc NEWS README
%license COPYING
%{_bindir}/faketime
%{_mandir}/man1/faketime.1*
%doc %{_docdir}/faketime
%{_libdir}/lib*.so*

%changelog
%{?autochangelog}
