# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: ayostl <yao_xp@yeah.net>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tmux
Version:        3.5a
Release:        %autorelease
Summary:        A terminal multiplexer
# SOURCE0 licensed under ISC AND BSD, SOURCE1 licensed under GPL-2.0-only
License:        ISC AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only
URL:            https://tmux.github.io/
#!RemoteAsset
Source0:        https://github.com/tmux/tmux/releases/download/%{version}/tmux-%{version}.tar.gz
#!RemoteAsset
Source1:        https://github.com/imomaliev/tmux-bash-completion/raw/refs/heads/master/completions/tmux
BuildSystem:    autotools

BuildOption(conf):  --enable-sixel
BuildOption(conf):  --enable-systemd
BuildOption(conf):  --enable-utempter
BuildOption(conf):  --enable-utf8proc

BuildRequires:  gcc
BuildRequires:  pkgconfig(libevent) >= 2
BuildRequires:  (pkgconfig(tinfo) or pkgconfig(ncurses) or pkgconfig(ncursesw))
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  libutempter-devel
BuildRequires:  bison

%description
tmux is a "terminal multiplexer."  It enables a number of terminals (or
windows) to be accessed and controlled from a single terminal.  tmux is
intended to be a simple, modern, BSD-licensed alternative to programs such
as GNU Screen.

%install -a

install -Dpm 644 %{S:1} %{buildroot}%{_datadir}/bash-completion/completions/tmux

%files
%license COPYING
%{_mandir}/man1/tmux.1*
%{_bindir}/tmux
%{_datadir}/bash-completion/completions/tmux

%changelog
%{?autochangelog}
