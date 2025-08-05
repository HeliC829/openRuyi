# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Mahno <bestwow2014@gmail.com>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           minicom
Summary:        A text-based modem control and terminal emulation program
Version:        2.10
Release:        %autorelease
URL:            https://salsa.debian.org/minicom-team/minicom
# The file 'src/wildmat.c' is in Public Domain
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
#!RemoteAsset
Source0:        https://salsa.debian.org/minicom-team/minicom/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make gcc
BuildRequires:  ncurses-devel autoconf automake gettext-devel
Recommends:       lrzsz
BuildSystem:    autotools

%description
Minicom is a simple text-based modem control and terminal emulation
program somewhat similar to MSDOS Telix. Minicom includes a dialing
directory, full ANSI and VT100 emulation, an (external) scripting
language, and other features.

%build -a
# Remove unused files to make sure we've got the License tag right.
rm -f lib/snprintf.c

%install -a
%find_lang %{name} --generate-subpackages

%files
%doc ChangeLog AUTHORS NEWS TODO
%license COPYING
%{_bindir}/minicom
%{_bindir}/runscript
%{_bindir}/xminicom
%{_bindir}/ascii-xfr
%{_mandir}/man1/*

%changelog
%{?autochangelog}
