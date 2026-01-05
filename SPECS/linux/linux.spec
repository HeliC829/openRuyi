# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0
%global modpath %{_prefix}/lib/modules/%{kver}

%ifarch riscv64
#!BuildConstraint: hardware:jobs 32
%endif

# Whether dtbs needed for arch
%ifarch riscv64
%global need_dtbs 1
%else
%global need_dtbs 0
%endif

%global signmodules 1
%global kver %{version}-%{release}
%global kernel_make_flags LD=ld.bfd KBUILD_BUILD_VERSION=%{release}
Name:             linux
Version:          6.18.3
Release:          %autorelease
Summary:          The Linux Kernel
License:          GPL-2.0-only
URL:              https://www.kernel.org/

#!RemoteAsset:    sha256:7a8879167b89c4bae077d6f39c4f2130769f05dbdad2aad914adab9afb7d7f9a
Source0:          https://cdn.kernel.org/pub/linux/kernel/v6.x/%{name}-%{version}.tar.xz
Source1:          config.%{_arch}

BuildRequires:    gcc, bison, binutils, glibc-devel, make, perl
BuildRequires:    flex, bison
BuildRequires:    bc, cpio, dwarves, gettext, python3, rsync, tar, xz, zstd
BuildRequires:    libasm-devel
BuildRequires:    libdebuginfod-dummy-devel
BuildRequires:    ncurses-devel
BuildRequires:    libcap-devel
BuildRequires:    libssh-devel
BuildRequires:    libdw-devel
BuildRequires:    libelf-devel
BuildRequires:    zstd-devel
BuildRequires:    python3-devel
BuildRequires:    slang-devel
BuildRequires:    zlib-devel
BuildRequires:    openssl-devel
BuildRequires:    kmod
BuildRequires:    rpm-config-openruyi

Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-modules%{?_isa} = %{version}-%{release}
%if %{need_dtbs}
Requires:       %{name}-dtbs%{?_isa} = %{version}-%{release}
%endif
Requires(post):   kmod
Requires(post):   kernel-install
Requires(postun): kernel-install

%patchlist
0001-UPSTREAM-drm-ttm-add-pgprot-handling-for-RISC-V.patch
0002-UPSTREAM-riscv-sophgo-dts-add-PCIe-controllers-for-S.patch
0003-UPSTREAM-riscv-sophgo-dts-enable-PCIe-for-PioneerBox.patch
0004-UPSTREAM-riscv-sophgo-dts-enable-PCIe-for-SG2042_EVB.patch
0005-UPSTREAM-riscv-sophgo-dts-enable-PCIe-for-SG2042_EVB.patch
0006-UPSTREAM-riscv-dts-sophgo-Add-SPI-NOR-node-for-SG204.patch
0007-UPSTREAM-riscv-dts-sophgo-Enable-SPI-NOR-node-for-Pi.patch
0008-UPSTREAM-riscv-dts-sophgo-Enable-SPI-NOR-node-for-SG.patch
0009-UPSTREAM-riscv-dts-sophgo-Enable-SPI-NOR-node-for-SG.patch
0010-UPSTREAM-dt-bindings-net-sophgo-sg2044-dwmac-add-phy.patch
0011-UPSTREAM-perf-vendor-events-riscv-add-T-HEAD-C920V2-.patch
0012-UPSTREAM-rust-macros-Add-support-for-imports_ns-to-m.patch
0013-UPSTREAM-pwm-Export-pwmchip_release-for-external-use.patch
0014-UPSTREAM-rust-pwm-Add-Kconfig-and-basic-data-structu.patch
0015-UPSTREAM-rust-pwm-Add-complete-abstraction-layer.patch
0016-UPSTREAM-rust-pwm-Add-module_pwm_platform_driver-mac.patch
0017-UPSTREAM-rust-pwm-Drop-wrapping-of-PWM-polarity-and-.patch
0018-UPSTREAM-rust-pwm-Fix-broken-intra-doc-link.patch
0019-UPSTREAM-pwm-Add-Rust-driver-for-T-HEAD-TH1520-SoC.patch
0020-UPSTREAM-dt-bindings-pwm-thead-Add-T-HEAD-TH1520-PWM.patch
0021-UPSTREAM-pwm-Fix-Rust-formatting.patch
0022-UPSTREAM-pwm-th1520-Fix-clippy-warning-for-redundant.patch
0023-UPSTREAM-pwm-th1520-Use-module_pwm_platform_driver-m.patch
0024-UPSTREAM-pwm-th1520-Fix-missing-Kconfig-dependencies.patch
0025-UPSTREAM-riscv-dts-thead-add-xtheadvector-to-the-th1.patch
0026-UPSTREAM-riscv-dts-thead-add-ziccrse-for-th1520.patch
0027-UPSTREAM-riscv-dts-thead-add-zfh-for-th1520.patch
0028-UPSTREAM-riscv-dts-thead-Add-PWM-controller-node.patch
0029-UPSTREAM-riscv-dts-thead-Add-PWM-fan-and-thermal-con.patch
0030-UPSTREAM-dt-bindings-vendor-prefixes-Add-UltraRISC.patch
0031-UPSTREAM-dt-bindings-interrupt-controller-Add-UltraR.patch
0032-UPSTREAM-irqchip-sifive-plic-Cache-the-interrupt-ena.patch
0033-UPSTREAM-irqchip-sifive-plic-Add-support-for-UltraRI.patch
0034-FROMLIST-riscv-errata-Add-ERRATA_THEAD_WRITE_ONCE-fi.patch
0035-FROMLIST-PCI-Release-BAR0-of-an-integrated-bridge-to.patch
0036-BACKPORT-FROMLIST-drm-ttm-save-the-device-s-DMA-cohe.patch
0037-BACKPORT-FROMLIST-drm-ttm-downgrade-cached-to-write_.patch
0038-FROMLIST-dt-bindings-clock-thead-th1520-clk-ap-Add-I.patch
0039-FROMLIST-clk-thead-th1520-ap-Poll-for-PLL-lock-and-w.patch
0040-FROMLIST-clk-thead-th1520-ap-Add-C910-bus-clock.patch
0041-FROMLIST-clk-thead-th1520-ap-Support-setting-PLL-rat.patch
0042-FROMLIST-clk-thead-th1520-ap-Add-macro-to-define-mul.patch
0043-FROMLIST-clk-thead-th1520-ap-Support-CPU-frequency-s.patch
0044-FROMLIST-NFU-riscv-dts-thead-Add-CPU-clock-and-OPP-t.patch
0045-FROMLIST-dt-bindings-vendor-prefixes-add-verisilicon.patch
0046-FROMLIST-dt-bindings-display-add-verisilicon-dc.patch
0047-FROMLIST-drm-verisilicon-add-a-driver-for-Verisilico.patch
0048-FROMLIST-dt-bindings-display-bridge-add-binding-for-.patch
0049-FROMLIST-drm-bridge-add-a-driver-for-T-Head-TH1520-H.patch
0050-FROMLIST-riscv-dts-thead-add-DPU-and-HDMI-device-tre.patch
0051-FROMLIST-riscv-dts-thead-lichee-pi-4a-enable-HDMI.patch
0052-FROMLIST-MAINTAINERS-assign-myself-as-maintainer-for.patch
0053-FROMLIST-mailmap-map-all-Icenowy-Zheng-s-mail-addres.patch
0054-FROMLIST-dt-bindings-usb-Add-T-HEAD-TH1520-USB-contr.patch
0055-FROMLIST-usb-dwc3-add-T-HEAD-TH1520-usb-driver.patch
0056-FROMLIST-rust-export-BINDGEN_TARGET-from-a-separate-.patch
0057-FROMLIST-rust-generate-a-fatal-error-if-BINDGEN_TARG.patch
0058-FROMLIST-rust-add-a-Kconfig-function-to-test-for-sup.patch
0059-FROMLIST-RISC-V-handle-extension-configs-for-bindgen.patch
0060-FROMLIST-PCI-MSI-Conservatively-generalize-no_64bit_.patch
0061-FROMLIST-PCI-MSI-Check-msi_addr_mask-in-msi_verify_e.patch
0062-FROMLIST-drm-radeon-Raise-msi_addr_mask-to-40-bits-f.patch
0063-FROMLIST-ALSA-hda-intel-Raise-msi_addr_mask-to-dma_b.patch
0064-FROMLIST-PCI-ASPM-Avoid-L0s-and-L1-on-Sophgo-2042-PC.patch
0065-FROMLIST-PCI-ASPM-Avoid-L0s-and-L1-on-Sophgo-2044-PC.patch
0066-FROMLIST-rust-clk-implement-Send-and-Sync.patch
0067-FROMLIST-tyr-remove-impl-Send-Sync-for-TyrData.patch
0068-FROMLIST-pwm-th1520-remove-impl-Send-Sync-for-Th1520.patch
0069-FROMLIST-riscv-boot-Always-make-Image-from-vmlinux-n.patch
0070-XUANTIE-riscv-dts-th1520-add-licheepi4a-16g-support.patch
0071-XUANTIE-riscv-dts-thead-Add-TH1520-USB-nodes.patch
0072-XUANTIE-riscv-dts-thead-Add-TH1520-I2C-nodes.patch
0073-XUANTIE-riscv-dts-thead-Add-Lichee-Pi-4A-IO-expansio.patch
0074-XUANTIE-riscv-dts-thead-Enable-Lichee-Pi-4A-USB.patch
0075-REVYOS-riscv-dts-th1520-rename-thead-to-xuantie.patch
0076-REVYOS-riscv-dts-th1520-add-xuantie-th1520-mbox-r.patch
0077-SOPHGO-dt-bindings-nvmem-Add-SG2044-eFuse-controller.patch
0078-SOPHGO-nvmem-Add-Sophgo-SG2044-eFuse-driver.patch
0079-SOPHGO-riscv-dts-sophgo-sg2044-Add-eFUSE-device.patch
0080-SOPHGO-dts-sg2044-Modify-pcie-bar-address.patch
0081-REVYSR-dt-bindings-net-ultrarisc-dp1000-gmac-Add-sup.patch
0082-REVYSR-net-stmmac-add-support-for-dwmac-5.10a.patch
0083-RVCK-riscv-dp1000-8250_dw-support-ultrarisc-dp1000-u.patch
0084-RVCK-riscv-dts-add-dp1000.dts-for-UltraRIsc-DP1000-S.patch
0085-RVCK-riscv-dp1000-arch-add-UltraRISC-DP1000-SoC-supp.patch
0086-RVCK-riscv-dp1000-pci-support-UltraRISC-pcie-rc.patch
0087-RVCK-pcie-update-the-outbound-mapping-process.patch
0088-RVCK-pinctrl-add-pinctrl-dirver-for-UltraRisc-DP1000.patch
0089-RVCK-dts-add-pinctrl-dtsi-dts-for-UltraRisc-DP1000.patch
0090-RVCK-pci-Update-the-number-of-outbound-and-inbound.patch
0091-RVCK-riscv-dp1000-pci-Add-custom-PCI-host-ops.patch
0092-RVCK-riscv-dp1000-dts-add-the-dts-of-UltraRISC-dp100.patch
0093-RVCK-riscv-dp1000-dts-Move-mmc0-node-from-SoC-to-boa.patch
0094-RVCK-riscv-dp1000-plic-add-plic-early-init-supports.patch
0095-RVCK-pcie-ultrarisc-Add-suspend-resume-support.patch
0096-RVCK-riscv-dp1000-dts-Move-chosen-node-from-common-t.patch
0097-RVCK-dts-riscv-ultrarisc-Refactor-DP1000-device-tree.patch
0098-RVCK-riscv-pinctrl-ultrarisc-Implement-pin-configura.patch
0099-RVCK-riscv-dts-dp1000-add-dts-dtsi-for-Milk-V-Titan-.patch

%description
This is a meta-package that installs the core kernel image and modules.
For a minimal boot environment, install the 'linux-core' package instead.

%package core
Summary:        The core Linux kernel image and initrd

%description core
Contains the bootable kernel image (vmlinuz) and a generic, pre-built initrd,
providing the minimal set of files needed to boot the system.

%package modules
Summary:        Kernel modules for the Linux kernel
Requires:       %{name}-core = %{version}-%{release}

%description modules
Contains all the kernel modules (.ko files) and associated metadata for
the hardware drivers and kernel features.

%package devel
Summary:          Development files for building external kernel modules
Requires:         %{name} = %{version}-%{release}
Requires:         dwarves

%description devel
This package provides the kernel headers and Makefiles necessary to build
external kernel modules against the installed kernel. The development files are
located at %{_usrsrc}/kernels/%{kver}, with symlinks provided under
%{_prefix}/lib/modules/%{kver}/ for compatibility.

%if %{need_dtbs}

%package dtbs
Summary:          Devicetree blob files from Linux sources

%description dtbs
This package provides the DTB files built from Linux sources that may be used
for booting.

%endif

%prep
%autosetup -p1
cp %{SOURCE1} .config
echo "-%{release}" > localversion

%conf
%make_build %{kernel_make_flags} olddefconfig

%build

%make_build %{kernel_make_flags}

%if %{need_dtbs}
%make_build %{kernel_make_flags} dtbs
%endif

%install
%define ksrcpath %{buildroot}%{_usrsrc}/kernels/%{kver}
install -d %{buildroot}%{modpath} %{ksrcpath}

%make_build %{kernel_make_flags} INSTALL_MOD_PATH=%{buildroot}%{_prefix} INSTALL_MOD_STRIP=1 DEPMOD=true modules_install

%if %{need_dtbs}
%make_build %{kernel_make_flags} INSTALL_DTBS_PATH=%{buildroot}%{modpath}/dtb dtbs_install
%endif

%make_build run-command %{kernel_make_flags} KBUILD_RUN_COMMAND="$(pwd)/scripts/package/install-extmod-build %{ksrcpath}"

pushd %{buildroot}%{modpath}
ln -sf %{_usrsrc}/kernels/%{kver} build
ln -sf %{_usrsrc}/kernels/%{kver} source
popd

install -Dm644 $(make %{kernel_make_flags} -s image_name) %{buildroot}%{modpath}/vmlinuz

echo "Module signing would happen here for version %{kver}."

%post
%{_bindir}/kernel-install add %{kver} %{modpath}/vmlinuz

%postun
if [ $1 -eq 0 ] ; then
    %{_bindir}/kernel-install remove %{kver}
fi

%files
%license COPYING
%doc README

%files core
%{modpath}/vmlinuz

%files modules
%{modpath}/*
%exclude %{modpath}/vmlinuz
%exclude %{modpath}/build
%exclude %{modpath}/source

%files devel
%{_usrsrc}/kernels/%{kver}/
%{modpath}/build
%{modpath}/source

%if %{need_dtbs}
%files dtbs
%{modpath}/dtb
%endif

%changelog
%{?autochangelog}
