# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Mahno <bestwow2014@gmail.com>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           luajit
# LuaJIT is a rolling release, see http://luajit.org/status.html
%global luajit_version 2.1
# The commit that could be patched
%global commit_date 20250113
%global commit a4f56a4
Version:        %{commit_date}+git%{commit}
Release:        %autorelease
Summary:        Just-In-Time Compiler for Lua
License:        MIT
URL:            http://luajit.org
#!RemoteAsset
Source0:        https://github.com/LuaJIT/LuaJIT/archive/%{commit}.tar.gz
# Support for risc-v patch, should remove once PR is mereged
Patch0:         0001-add_riscv_support.patch
# Enable Lua 5.2 features
Patch1:         0002-enable-lua52compat.patch
# Preserve timestamps during installation
Patch2:         0003-preserve-timestamps.patch
# not autotools, use this for ease
BuildSystem:    autotools
BuildOption(build): amalg Q= E=@: PREFIX=%{_prefix} TARGET_STRIP=:
BuildOption(build): CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"
BuildOption(build): MULTILIB=%{_lib}
BuildOption(install): PREFIX=%{_prefix} MULTILIB=%{_lib}
BuildRequires:  gcc
BuildRequires:  make

%description
LuaJIT implements the full set of language features defined by Lua 5.1.
The virtual machine (VM) is API- and ABI-compatible to the standard
Lua interpreter and can be deployed as a drop-in replacement.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}

%description devel
This package contains development files for %{name}.

# overwrite conf process, don't do anything here
%conf

%install -a
# Remove static .a
find %{buildroot} -type f -name *.a -delete -print

%files
%license COPYRIGHT
%doc README
%{_bindir}/luajit*
%{_libdir}/libluajit-*.so.*
%{_mandir}/man1/luajit.1*
%{_datadir}/luajit-%{luajit_version}

%files devel
%doc doc/*
%{_includedir}/luajit-%{luajit_version}/
%{_libdir}/libluajit-*.so
%{_libdir}/pkgconfig/luajit.pc

%changelog
%{?autochangelog}
