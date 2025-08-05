# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dtc
Version:        1.7.2
Release:        %autorelease
Summary:        Device Tree Compiler
License:        GPL-2.0-or-later
URL:            https://devicetree.org/
#!RemoteAsset
Source0:        https://www.kernel.org/pub/software/utils/%{name}/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://www.kernel.org/pub/software/utils/%{name}/%{name}-%{version}.tar.sign
Patch1:         backport-pylibfdt-libfdt.i-fix-backwards-compatibility-of-return-values.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  swig
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel
Provides:       libfdt = %{version}-%{release}
Obsoletes:      libfdt < %{version}-%{release}
BuildSystem:    autotools
BuildOption(install): V=1 DESTDIR=%{buildroot} PREFIX=%{buildroot}/%{_prefix}
BuildOption(install): LIBDIR=%{_libdir} BINDIR=%{_bindir} INCLUDEDIR=%{_includedir}

%description
The devicetree is a data structure for describing hardware. Rather than hard coding
every detail of a device into an operating system, many aspects of the hardware can
be described in a data structure that is passed to the operating system at boot time.
The devicetree is used by OpenFirmware, OpenPOWER Abstraction Layer (OPAL), Power
Architecture Platform Requirements (PAPR) and in the standalone Flattened Device
Tree (FDT) form.

%package        devel
Summary:        Development headers for device tree library
Requires:       libfdt = %{version}-%{release}
Provides:       libfdt-static = %{version}-%{release}
Provides:       libfdt-devel = %{version}-%{release}
Obsoletes:      libfdt-static < %{version}-%{release}
Obsoletes:      libfdt-devel < %{version}-%{release}

%description    devel
This package provides development files for dtc.

%package        -n python3-libfdt
Summary:        Python 3 bindings for device tree library
%{?python_provide:%python_provide python3-libfdt}
Requires:       %{name} = %{version}-%{release}

%description    -n python3-libfdt
This package provides python3 bindings for libfdt

# no configure
%conf

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%install -p
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}


%check -p
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%license GPL README.license
%doc Documentation/manual.txt
%{_bindir}/*
%{_libdir}/libfdt.so.*

%files devel
%{_libdir}/libfdt.so
%{_includedir}/*
%{_libdir}/libfdt.a

%files -n python3-libfdt
%{python3_sitearch}/*

%changelog
%{?autochangelog}
