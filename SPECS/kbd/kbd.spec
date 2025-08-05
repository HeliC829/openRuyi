# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond nls 0

# It is traditionally used for kdb data (console fonts, keymaps, ...).
%global kbd_datadir %{_libdir}/kbd

Name:           kbd
Version:        2.8.0
Release:        %autorelease
Summary:        Tools for configuring the console (keyboard, virtual terminals, etc.)
License:        GPL-2.0-or-late
URL:            http://www.kbd-project.org/
#!RemoteAsset
Source0:        https://www.kernel.org/pub/linux/utils/%{name}/%{name}-%{version}.tar.xz
Source1:        vlock.pamd
BuildSystem:    autotools

BuildOption(conf):  --prefix=%{_prefix}
BuildOption(conf):  --datadir=%{kbd_datadir}
BuildOption(conf):  --mandir=%{_mandir}
BuildOption(conf):  --localedir=%{_datadir}/locale

%if %{with nls}
BuildOption(conf):  --enable-nls
%else
BuildOption(conf):  --disable-nls
%endif

BuildOption(conf):  --disable-tests
BuildOption(build):  KEYCODES_PROGS=yes
BuildOption(build):  RESIZECONS_PROGS=yes
BuildOption(install):  KEYCODES_PROGS=yes
BuildOption(install):  RESIZECONS_PROGS=yes

BuildRequires:  bison
BuildRequires:  flex

%if %{with nls}
BuildRequires:  gettext
%endif

BuildRequires:  pam-devel
BuildRequires:  make
BuildRequires:  automake

%description
The %{name} package contains tools for managing a Linux
system's console's behavior, including the keyboard, the screen
fonts, the virtual terminals and font files.

%prep -a
aclocal
autoconf -fiv

%install -a
# Install PAM configuration for vlock
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/vlock
%if %{with nls}
%find_lang %{name} --generate-subpackages
%endif

%files
%license COPYING
%doc ChangeLog AUTHORS README docs/doc/font-formats/*.html docs/doc/dvorak/*
%{_bindir}/*
%{_mandir}/*/*
%config(noreplace) %{_sysconfdir}/pam.d/vlock
%{kbd_datadir}/consolefonts/*
%{kbd_datadir}/consoletrans/*
%{kbd_datadir}/unimaps/*
%{kbd_datadir}/keymaps/*

%changelog
%{?autochangelog}
