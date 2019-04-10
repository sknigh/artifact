# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RMethodss3(RPackage):
    """Methods that simplify the setup of S3 generic functions and
    S3 methods. Major effort has been made in making definition of
    methods as simple as possible with a minimum of maintenance for
    package developers. For example, generic functions are created
    automatically, if missing, and naming conflict are automatically
    solved, if possible. The method setMethodS3() is a good start
    for those who in the future may want to migrate to S4. This is
    a cross-platform package implemented in pure R that generates
    standard S3 methods."""

    homepage = "https://cran.r-project.org/package=R.methodsS3"
    url      = "https://cran.r-project.org/src/contrib/R.methodsS3_1.7.1.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/R.methodsS3"

    version('1.7.1', 'c88e815837f268affd4f2a39c737d969')
