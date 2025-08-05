# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           boringssl
Version:        0.20251002.0
Release:        %autorelease
Summary:        Fork of OpenSSL that is designed to meet Google's needs.
License:        Apache-2.0
URL:            https://boringssl.googlesource.com/boringssl/
#!RemoteAsset
Source:         https://github.com/google/boringssl/releases/download/%{version}/%{name}-%{version}.tar.gz

Patch1:         Fix-install-cmake-prefix-path.patch

BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  ninja

BuildOption(conf):  -GNinja

# FIXME: Avoid having warnings treated as errors on line asn1_test.cc:2441
%global optflags %{optflags} -Wno-array-bounds

%description
Although BoringSSL is an open source project, it is not intended for general
use, as OpenSSL is.  We don't recommend that third parties depend upon it.
Doing so is likely to be frustrating because there are no guarantees of API
or ABI stability.

%package        devel
Summary:        Fork of OpenSSL that is designed to meet Google's needs.

%description    devel
Fork of OpenSSL that is designed to meet Google's needs.

Although BoringSSL is an open source project, it is not intended for general
use, as OpenSSL is.  We don't recommend that third parties depend upon it.
Doing so is likely to be frustrating because there are no guarantees of API
or ABI stability.


%files
%{_bindir}/bssl
%{_libdir}/libcrypto.so
%{_libdir}/libssl.so
%license LICENSE

%files devel
%{_includedir}/openssl
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/OpenSSL
%{_libdir}/cmake/OpenSSL/*.cmake

%changelog
%{?autochangelog}
