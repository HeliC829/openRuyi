# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define package_version 9.1
%define patchlevel 1629

%define vimdir vim91

Name:           vim
Version:        %{package_version}.%{patchlevel}
Release:        %autorelease
Summary:        Tools needed to create Texinfo format documentation files
License:        Vim AND LGPL-2.1-or-later AND MIT AND GPL-1.0-only AND (GPL-2.0-only OR Vim) AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-or-later AND GPL-3.0-or-later AND OPUBL-1.0 AND Apache-2.0
URL:            https://www.vim.org/
#!RemoteAsset
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  gettext
BuildRequires:  acl-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel

%description
Texinfo is a documentation system that can produce both online
information and printed output from a single source file. The GNU
Project uses the Texinfo file format for most of its documentation.

Install texinfo if you want a documentation system for producing both
online and print documentation from the same source file and/or if you
are going to write documentation for the GNU Project.

%package     -n xxd
Summary:        A hex dump utility

%description -n xxd
xxd creates a hex dump of a given file or standard input.  It can also convert
a hex dump back to its original binary form.

%install -a
# Remove unecessary duplicate manpages - 251
rm -rf %{buildroot}%{_mandir}/fr.ISO8859-1/
rm -rf %{buildroot}%{_mandir}/fr.UTF-8/
rm -rf %{buildroot}%{_mandir}/pl.ISO8859-2/
rm -rf %{buildroot}%{_mandir}/pl.UTF-8/
rm -rf %{buildroot}%{_mandir}/ru.KOI8-R/
rm -rf %{buildroot}%{_mandir}/it.ISO8859-1/
rm -rf %{buildroot}%{_mandir}/it.UTF-8/
rm -rf %{buildroot}%{_mandir}/da.UTF-8/
rm -rf %{buildroot}%{_mandir}/de.UTF-8/
rm -rf %{buildroot}%{_mandir}/da.ISO8859-1/
rm -rf %{buildroot}%{_mandir}/de.ISO8859-1/
rm -rf %{buildroot}%{_mandir}/tr.ISO8859-9/
rm -rf %{buildroot}%{_mandir}/tr.UTF-8/

%find_lang %{name} --all-name --with-man --generate-subpackages

%files
%license %{_datadir}/%{name}/%{vimdir}/LICENSE
%doc %{_datadir}/%{name}/%{vimdir}/README.txt
%{_bindir}/vim
%{_bindir}/rvim
%{_bindir}/vimdiff
%{_bindir}/vimtutor
%{_bindir}/ex
%{_bindir}/rview
%{_bindir}/view
%{_datadir}/%{name}/%{vimdir}/autoload
%{_datadir}/%{name}/%{vimdir}/colors
%{_datadir}/%{name}/%{vimdir}/compiler
%{_datadir}/%{name}/%{vimdir}/pack
%{_datadir}/%{name}/%{vimdir}/doc
%{_datadir}/%{name}/%{vimdir}/*.vim
%exclude %{_datadir}/%{name}/%{vimdir}/defaults.vim
%{_datadir}/%{name}/%{vimdir}/ftplugin
%{_datadir}/%{name}/%{vimdir}/import/dist/vimhelp.vim
%{_datadir}/%{name}/%{vimdir}/import/dist/vimhighlight.vim
%{_datadir}/%{name}/%{vimdir}/indent
%{_datadir}/%{name}/%{vimdir}/keymap
%{_datadir}/%{name}/%{vimdir}/lang/*.vim
%{_datadir}/%{name}/%{vimdir}/lang/*.txt
%{_datadir}/%{name}/%{vimdir}/macros
%{_datadir}/%{name}/%{vimdir}/plugin
%{_datadir}/%{name}/%{vimdir}/print
%{_datadir}/%{name}/%{vimdir}/syntax
%{_datadir}/%{name}/%{vimdir}/tutor
%{_datadir}/%{name}/%{vimdir}/spell
%{_datadir}/%{name}/%{vimdir}/tools
%{_mandir}/man1/vim.*
%{_mandir}/man1/ex.*
%{_mandir}/man1/rview.*
%{_mandir}/man1/view.*
%{_mandir}/man1/evim.*
%{_mandir}/man1/rvim.*
%{_mandir}/man1/vimdiff.*
%{_mandir}/man1/vimtutor.*
# If we need GUI then add these back
%exclude %{_datadir}/applications/vim.desktop
%exclude %{_datadir}/applications/gvim.desktop
%exclude %{_datadir}/icons/hicolor/*/apps/gvim.*
%exclude %{_datadir}/icons/locolor/*/apps/gvim.*

%files -n xxd
%license LICENSE
%{_bindir}/xxd
%{_mandir}/man1/xxd.*

%changelog
%{?autochangelog}
