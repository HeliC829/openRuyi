# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           irqbalance
Version:        1.9.4
Release:        %autorelease
Summary:        IRQ balancing daemon
License:        GPL-2.0-only
URL:            https://github.com/Irqbalance/irqbalance
#!RemoteAsset
Source0:        %{url}/archive/v%{version}/irqbalance-%{version}.tar.gz
BuildSystem:    autotools

# https://github.com/Irqbalance/irqbalance/commit/b6a831d692ed7e12db7748db49b3b39516d151d2
Patch0:         0001-add-void-to-fix-strict_-_prototypes.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libcap-ng
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(numa)

Requires:       numactl

%description
irqbalance is a daemon that evenly distributes IRQ load across
multiple CPUs for enhanced performance.

%conf -p
# Otherwise configure will not happy - 251
./autogen.sh

%install -a
install -D -p -m 0644 ./misc/irqbalance.service %{buildroot}/%{_unitdir}/irqbalance.service
install -D -p -m 0644 ./misc/irqbalance.env %{buildroot}%{_sysconfdir}/sysconfig/irqbalance

%post
%systemd_post irqbalance.service

%preun
%systemd_preun irqbalance.service

%postun
%systemd_postun_with_restart irqbalance.service

%files
%doc COPYING AUTHORS
%{_sbindir}/irqbalance
%{_unitdir}/irqbalance.service
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/sysconfig/irqbalance
# Should we include this? - 251
%exclude %{_sbindir}/irqbalance-ui

%changelog
%{?autochangelog}
