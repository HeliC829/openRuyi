# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sarama
%define go_import_path  github.com/IBM/sarama

Name:           go-github-ibm-sarama
Version:        1.61.0
Release:        %autorelease
Summary:        Go client for Apache Kafka
License:        MIT
URL:            https://github.com/IBM/sarama
#!RemoteAsset:  sha256:ac954c4e4b89cf724c324e5f654f24d00b5a1044003b66f8881a06434a78c025
Source0:        https://github.com/IBM/sarama/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Fix printf diagnostics while retaining vet and strict unit tests.
Patch2000:      2000-fix-log-and-mock-error-formatting.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/eapache/go-resiliency)
BuildRequires:  go(github.com/eapache/go-xerial-snappy)
BuildRequires:  go(github.com/eapache/queue)
BuildRequires:  go(github.com/fortytw2/leaktest)
BuildRequires:  go(github.com/hashicorp/errwrap)
BuildRequires:  go(github.com/hashicorp/go-multierror)
BuildRequires:  go(github.com/jcmturner/gofork)
BuildRequires:  go(github.com/jcmturner/gokrb5/v8)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/pierrec/lz4/v4)
BuildRequires:  go(github.com/rcrowley/go-metrics)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/IBM/sarama) = %{version}

Requires:       go(github.com/davecgh/go-spew)
Requires:       go(github.com/eapache/go-resiliency)
Requires:       go(github.com/eapache/go-xerial-snappy)
Requires:       go(github.com/eapache/queue)
Requires:       go(github.com/hashicorp/errwrap)
Requires:       go(github.com/hashicorp/go-multierror)
Requires:       go(github.com/jcmturner/gofork)
Requires:       go(github.com/jcmturner/gokrb5/v8)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/pierrec/lz4/v4)
Requires:       go(github.com/rcrowley/go-metrics)
Requires:       go(golang.org/x/net)

%description
Sarama is a pure-Go client for Apache Kafka 0.8 and later. MinIO uses
it as a Kafka event-notification target.

%prep -a
# examples/ are sample programs with nested modules, not the library.
rm -rf examples
# tools/ holds kafka-console-* diagnostics and a performance client,
# not an upstream-distributed program. This RPM is the importable library.
rm -rf tools

%files
%doc README.md CHANGELOG.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
