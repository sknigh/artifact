# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class LinuxHeaders(Package):
    """The Linux kernel headers."""

    homepage = "https://www.kernel.org/"
    url      = "https://www.kernel.org/pub/linux/kernel/v4.x/linux-4.9.10.tar.xz"
    list_url = "https://www.kernel.org/pub/linux/kernel"
    list_depth = 2

    version('4.9.10', 'ce5ab2a86c9b880617e36e84aa2deb6c')

    def setup_environment(self, spack_env, run_env):
        # This variable is used in the Makefile. If it is defined on the
        # system, it can break the build if there is no build recipe for
        # that specific ARCH
        spack_env.unset('ARCH')

    def install(self, spec, prefix):
        make('headers_install', 'INSTALL_HDR_PATH={0}'.format(prefix))