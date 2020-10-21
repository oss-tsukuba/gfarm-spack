# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install gfarm
#
# You can edit this file again by typing:
#
#     spack edit gfarm
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Gfarm(AutotoolsPackage):
    """Gfarm file system is a network shared file system that supports scalable I/O performance in distributed environment. It can federate local disks of network-connected PCs and compute nodes in several clusters."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://oss-tsukuba.org/software/gfarm"
    url = "https://sourceforge.net/projects/gfarm/files/gfarm_v2/2.7.13/gfarm-2.7.13.tar.gz"

    version('develop', svn='https://svn.code.sf.net/p/gfarm/code/gfarm_v2/branches/2.7', preferred=True)
    version('2.7.13', sha256='836554560df52bf03a355130815cc4d1851c6e061cd1459c2086873059eb0ab6')

    # FIXME: Add dependencies if required.
    depends_on('openssl')
    depends_on('postgresql')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
