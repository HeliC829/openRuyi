# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:       lsscsi
Version:    0.32
Release:    %autorelease
Summary:    The lsscsi command lists information about SCSI devices in Linux.
License:    GPLv2+
URL:        http://sg.danny.cz/scsi/lsscsi.html
#!RemoteAsset
Source0:    http://sg.danny.cz/scsi/%{name}-%{version}.tgz

BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildSystem:   autotools

%description
Using SCSI terminology, lsscsi lists SCSI logical units (or SCSI targets
when the '--transport' option is given). The default action is to produce
one line of output for each SCSI device currently attached to the system.
In version 0.30 of this utility, support was added to list NVMe namespaces
(under SCSI devices(LUs)) and NVMe controllers (under SCSI hosts).

%files
%doc ChangeLog INSTALL README CREDITS AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
%{?autochangelog}
