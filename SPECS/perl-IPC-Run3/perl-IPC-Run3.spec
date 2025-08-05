# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global tar_name IPC-Run3

Name:           perl-IPC-Run3
Version:        0.049
Release:        %autorelease
Summary:        Run a subprocess in batch mode
License:        GPL-1.0-or-later OR Artistic-1.0-Perl OR BSD-2-Clause
URL:            https://metacpan.org/release/IPC-Run3
#!RemoteAsset
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{tar_name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More) >= 0.31
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
# For improved tests
#BuildRequires:  perl(Test::Pod::Coverage)
#BuildRequires:  perl(Test::Pod)

%description
This module allows you to run a subprocess and redirect stdin, stdout,
and/or stderr to files and perl data structures. It aims to satisfy 99% of
the need for using system, qx, and open3 with a simple, extremely Perlish
API and none of the bloat and rarely used features of IPC::Run.

%conf
# No configure

%build -p
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
%{?autochangelog}
