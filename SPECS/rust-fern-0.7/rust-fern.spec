# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fern
%global full_version 0.7.1
%global pkgname fern-0.7

Name:           rust-fern-0.7
Version:        0.7.1
Release:        %autorelease
Summary:        Rust crate "fern"
License:        MIT
URL:            https://github.com/daboross/fern
#!RemoteAsset:  sha256:4316185f709b23713e41e3195f90edef7fb00c3ed4adc79769cf09cc762a3b29
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(log-0.4/std) >= 0.4.29
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/meta-logging-in-format)

%description
Source code for takopackized Rust crate "fern"

%package     -n %{name}+chrono
Summary:        Simple, efficient logging - feature "chrono" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(chrono-0.4/clock) >= 0.4.0
Requires:       crate(chrono-0.4/std) >= 0.4.0
Provides:       crate(%{pkgname}/chrono)
Provides:       crate(%{pkgname}/date-based)

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust fern crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "date-based" feature.

%package     -n %{name}+colored
Summary:        Simple, efficient logging - feature "colored"
Requires:       crate(%{pkgname})
Requires:       crate(colored-2.0/default) >= 2.1.0
Provides:       crate(%{pkgname}/colored)

%description -n %{name}+colored
This metapackage enables feature "colored" for the Rust fern crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Simple, efficient logging - feature "libc"
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2/default) >= 0.2.58
Provides:       crate(%{pkgname}/libc)

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust fern crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+reopen-03
Summary:        Simple, efficient logging - feature "reopen-03"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/libc)
Requires:       crate(%{pkgname}/reopen03)
Provides:       crate(%{pkgname}/reopen-03)

%description -n %{name}+reopen-03
This metapackage enables feature "reopen-03" for the Rust fern crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+reopen-1
Summary:        Simple, efficient logging - feature "reopen-1"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/libc)
Requires:       crate(%{pkgname}/reopen1)
Provides:       crate(%{pkgname}/reopen-1)

%description -n %{name}+reopen-1
This metapackage enables feature "reopen-1" for the Rust fern crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+reopen03
Summary:        Simple, efficient logging - feature "reopen03"
Requires:       crate(%{pkgname})
Requires:       crate(reopen-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/reopen03)

%description -n %{name}+reopen03
This metapackage enables feature "reopen03" for the Rust fern crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+reopen1
Summary:        Simple, efficient logging - feature "reopen1"
Requires:       crate(%{pkgname})
Requires:       crate(reopen-1.0/default) >= 1.0.0
Requires:       crate(reopen-1.0/signals) >= 1.0.0
Provides:       crate(%{pkgname}/reopen1)

%description -n %{name}+reopen1
This metapackage enables feature "reopen1" for the Rust fern crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+syslog3
Summary:        Simple, efficient logging - feature "syslog3" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(syslog-3.0/default) >= 3.0.0
Provides:       crate(%{pkgname}/syslog-3)
Provides:       crate(%{pkgname}/syslog3)

%description -n %{name}+syslog3
This metapackage enables feature "syslog3" for the Rust fern crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "syslog-3" feature.

%package     -n %{name}+syslog4
Summary:        Simple, efficient logging - feature "syslog4" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(syslog-4.0/default) >= 4.0.0
Provides:       crate(%{pkgname}/syslog-4)
Provides:       crate(%{pkgname}/syslog4)

%description -n %{name}+syslog4
This metapackage enables feature "syslog4" for the Rust fern crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "syslog-4" feature.

%package     -n %{name}+syslog6
Summary:        Simple, efficient logging - feature "syslog6" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(syslog-6.0/default) >= 6.0.0
Provides:       crate(%{pkgname}/syslog-6)
Provides:       crate(%{pkgname}/syslog6)

%description -n %{name}+syslog6
This metapackage enables feature "syslog6" for the Rust fern crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "syslog-6" feature.

%package     -n %{name}+syslog7
Summary:        Simple, efficient logging - feature "syslog7" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(syslog-7.0/default) >= 7.0.0
Provides:       crate(%{pkgname}/syslog-7)
Provides:       crate(%{pkgname}/syslog7)

%description -n %{name}+syslog7
This metapackage enables feature "syslog7" for the Rust fern crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "syslog-7" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
