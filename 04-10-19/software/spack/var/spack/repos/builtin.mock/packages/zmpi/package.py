# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Zmpi(Package):
    """This is a fake MPI package used to demonstrate virtual package providers
       with dependencies."""
    homepage = "http://www.spack-fake-zmpi.org"
    url      = "http://www.spack-fake-zmpi.org/downloads/zmpi-1.0.tar.gz"

    version('1.0', 'foobarbaz')

    provides('mpi@:10.0')
    depends_on('fake')

    def install(self, spec, prefix):
        pass
