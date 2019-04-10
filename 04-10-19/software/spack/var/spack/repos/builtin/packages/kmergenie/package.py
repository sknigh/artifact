# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Kmergenie(MakefilePackage):
    """KmerGenie estimates the best k-mer length for genome de novo assembly.
    """

    homepage = "http://kmergenie.bx.psu.edu/"
    url      = "http://kmergenie.bx.psu.edu/kmergenie-1.7044.tar.gz"

    version('1.7044', '407209c8181f1631ecb79b0ca735d18f')

    depends_on('python', type=('build', 'run'))
    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('r', type=('build', 'run'))
    depends_on('zlib')

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix.bin)