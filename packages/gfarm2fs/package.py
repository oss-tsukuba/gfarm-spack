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
#     spack install gfarm2fs
#
# You can edit this file again by typing:
#
#     spack edit gfarm2fs
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Gfarm2fs(AutotoolsPackage):
    """A plugin to mount gfarm filesystem"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://oss-tsukuba.org/software/gfarm"
    url = "https://sourceforge.net/projects/gfarm/files/gfarm2fs/1.2.12/gfarm2fs-1.2.12.tar.gz"

    version('develop', svn='https://svn.code.sf.net/p/gfarm/code/gfarm2fs/trunk', preferred=True)
    version('1.2.12', sha256='e61d6898d58c32f96d989b573ac0356068f174516be7659c33e603e160fbab8b')

    # FIXME: Add dependencies if required.
    depends_on('gfarm')

    variant(
         'acl', default=True, description='Builds with acl'
     )

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        spec = self.spec
        args = []

        if not '+acl' in spec:
            args.append('--disable-acl')

        args.append('--with-gfarm={0}'.format(spec['gfarm'].prefix))

        return args
