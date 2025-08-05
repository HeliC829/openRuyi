# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Suyun114 <ziyu.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           efivar
Version:        39
Release:        %autorelease
Summary:        Tools to manage UEFI variables
License:        LGPL-2.1-only
URL:            https://github.com/rhboot/efivar
#!RemoteAsset
Source:         https://github.com/rhboot/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(install): libdir=%{_libdir}
BuildRequires:  mandoc

%description
efivar provides a simple command line interface to the UEFI variable facility.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description    devel
Development headers required to use libefivar.

%conf
# efivar has no configuration script

%files
%license COPYING
%{_bindir}/efivar
%{_bindir}/efisecdb
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%{?autochangelog}
