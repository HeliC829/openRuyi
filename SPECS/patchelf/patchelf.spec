# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           patchelf
Version:        0.18.0
Release:        %autorelease
Summary:        A utility for patching ELF binaries
License:        GPL-3.0-or-later
URL:            https://nixos.org/patchelf.html
#!RemoteAsset
Source0:        https://github.com/NixOS/patchelf/archive/refs/tags/%{version}/patchelf-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  gcc gcc-c++ make autoconf automake libtool

%description
PatchELF is a simple utility for modifying an existing ELF executable
or library. It can change the dynamic loader ("ELF interpreter")
of an executable and change the RPATH of an executable or library.

%prep -a
# package ships elf.h - delete to use glibc-headers one
%{__rm} -f src/elf.h

%conf -p
autoreconf -fiv

%files
%license COPYING
%doc README.md
%doc %{_docdir}/%{name}
%{_bindir}/patchelf
%{_mandir}/man1/patchelf.1*
%{_datadir}/zsh/site-functions/_patchelf

%changelog
%{?autochangelog}
