# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Mahno <bestwow2014@gmail.com>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mold
Version:        2.40.4
Release:        %autorelease
Summary:        A Modern Linker
License:        MIT AND (Apache-2.0 OR MIT)
URL:            https://github.com/rui314/mold
#!RemoteAsset
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Allow building against the system-provided `xxhash.h`
Patch0:         0001-Use-system-compatible-include-path-for-xxhash.h.patch
BuildSystem:    cmake
# use bundled mimalloc
# BuildOption(conf):  -DMOLD_USE_SYSTEM_MIMALLOC=ON

# use bundled blake3 to decrease dependency
# BuildRequires:  blake3-devel
BuildRequires:  cmake
BuildRequires:  gcc gcc-c++
# BuildRequires:  mimalloc-devel
BuildRequires:  xxhash-devel zlib-devel zstd-devel
Provides:       bundled(tbb) = 2022.1
Provides:       bundled(blake3)
Provides:       bundled(mimalloc)

Requires(post): update-alternatives
Requires(preun):update-alternatives

%description
mold is a faster drop-in replacement for existing Unix linkers.
It is several times faster than the LLVM lld linker.
mold is designed to increase developer productivity by reducing
build time, especially in rapid debug-edit-rebuild cycles.

%post
if [ "$1" = 1 ]; then
  update-alternatives --install %{_bindir}/ld ld %{_bindir}/ld.mold 100
fi

%postun
if [ "$1" = 0 ]; then
  update-alternatives --remove ld %{_bindir}/ld.mold
fi

%files
%license %{_docdir}/mold/LICENSE
%ghost %{_bindir}/ld
%{_bindir}/mold
%{_bindir}/ld.mold
%{_libdir}/mold/mold-wrapper.so
%{_libexecdir}/mold/ld
%{_mandir}/man1/ld.mold.1*
%{_mandir}/man1/mold.1*

%changelog
%{?autochangelog}
