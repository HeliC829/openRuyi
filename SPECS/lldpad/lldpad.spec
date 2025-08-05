# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:               lldpad
Version:            1.1.0
Release:            %autorelease
Summary:            Intel LLDP Agent for Data Center Bridging
License:            GPL-2.0-only
URL:                http://open-lldp.org/
#!RemoteAsset
Source:             https://github.com/openSUSE/lldpad/archive/refs/tags/v%{version}.tar.gz
BuildSystem:        autotools

BuildOption(conf): --disable-static
BuildOption(build): CFLAGS="%{optflags} -Wno-error -fcommon"

BuildRequires:      automake
BuildRequires:      autoconf
BuildRequires:      libtool
BuildRequires:      flex >= 2.5.33
BuildRequires:      util-linux
BuildRequires:      libconfig-devel
BuildRequires:      libnl-devel
BuildRequires:      readline-devel
BuildRequires:      systemd-rpm-macros
BuildRequires:      make gcc

Requires:           readline
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

%description
This package contains the Linux user space daemon and configuration tool for
the Intel LLDP Agent, enabling Data Center Bridging (DCB) features.

%package            devel
Summary:            Development files for %{name}
Requires:           %{name} = %{version}
Provides:           dcbd-devel = %{version}

%description        devel
The %{name}-devel package contains header files for developing applications
that use %{name}.

%conf -p
./bootstrap.sh

%install -a
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}

%post
%systemd_post lldpad.service lldpad.socket

%preun
%systemd_preun lldpad.service lldpad.socket

%postun
%systemd_postun_with_restart lldpad.service lldpad.socket

%files
%doc COPYING README ChangeLog
%{_sbindir}/*
%{_libdir}/liblldp_clif.so.*
%dir %{_sharedstatedir}/lldpad
%{_unitdir}/lldpad.service
%{_unitdir}/lldpad.socket
%{_sysconfdir}/bash_completion.d/*
%{_mandir}/man3/*
%{_mandir}/man8/*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/liblldp_clif.so

%changelog
%{?autochangelog}
