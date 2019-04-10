# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Othervirtual(Package):
    homepage = "http://somewhere.com"
    url      = "http://somewhere.com/stuff-1.0.tar.gz"

    version('1.0', '67890abcdef1234567890abcdef12345')

    provides('stuff')

    def install(self, spec, prefix):
        pass
