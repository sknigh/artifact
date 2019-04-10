# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Mira(AutotoolsPackage):
    """MIRA is a multi-pass DNA sequence data assembler/mapper for whole genome
       and EST/RNASeq projects."""

    homepage = "http://sourceforge.net/projects/mira-assembler/"
    url      = "https://downloads.sourceforge.net/project/mira-assembler/MIRA/stable/mira-4.0.2.tar.bz2"

    version('4.0.2', '1921b426910653a34a6dbb37346f28ea')

    depends_on('boost@1.46:')
    depends_on('expat@2.0.1:')
    depends_on('gperftools')

    conflicts('%gcc@6:', when='@:4.0.2')

    def patch(self):
        with working_dir(join_path('src', 'progs')):
            edit = FileFilter('quirks.C')
            edit.filter('#include <boost/filesystem.hpp>',
                        '#include <boost/filesystem.hpp>\n#include <iostream>')

    def configure_args(self):
        args = ['--with-boost=%s' % self.spec['boost'].prefix,
                '--with-expat=%s' % self.spec['expat'].prefix]
        return args
