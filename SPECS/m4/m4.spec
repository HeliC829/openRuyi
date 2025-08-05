# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Define build conditionals for optional features
%bcond nls 0

Name:           m4
Version:        1.4.20
Release:        %autorelease
Summary:        The GNU macro processor
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/m4/
#!RemoteAsset
Source0:         https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz

BuildSystem:    autotools
BuildOption(conf): --without-included-regex
%if %{with nls}
BuildOption(conf): --enable-nls
%else
BuildOption(conf): --disable-nls
%endif

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
%if %{with nls}
BuildRequires:  gettext
%endif

%description
A GNU implementation of the traditional UNIX macro processor. M4 is
useful for writing text files which can be logically parsed, and is used
by many programs, such as autoconf, as part of their build process.

%if %{with nls}
%install -a
rm -f %{buildroot}%{_infodir}/dir

%find_lang %{name} --generate-subpackages
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/m4
%{_mandir}/man1/m4.1*
%{_infodir}/m4.info*

%changelog
%{?autochangelog}
