# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: jchzhou <zhoujiacheng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           hwdata
Version:        0.398
Release:        %autorelease
Summary:        Hardware identification and configuration data
License:        GPL-2.0-or-later
URL:            https://github.com/vcrhonek/hwdata
#!RemoteAsset
Source0:        https://github.com/vcrhonek/hwdata/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    autotools
BuildOption(install): libdir=%{_libdir}

BuildRequires:  make

%description
hwdata contains various hardware identification and configuration data,
such as the pci.ids and usb.ids databases.

%files
%license COPYING
%doc LICENSE
%dir %{_datadir}/%{name}
%{_prefix}/lib/modprobe.d/dist-blacklist.conf
%{_datadir}/%{name}/*
%{_datadir}/pkgconfig/hwdata.pc

%changelog
%{?autochangelog}
