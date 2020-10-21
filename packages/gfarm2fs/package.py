# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: MIT

from spack import *


class Gfarm2fs(AutotoolsPackage):
    """Linux FUSE client of Gfarm"""

    homepage = 'http://oss-tsukuba.org/software/gfarm'
    url = 'https://github.com/oss-tsukuba/gfarm2fs/archive/1.2.14.tar.gz'
    git = 'https://github.com/oss-tsukuba/gfarm2fs.git'

    version('main', branch='master', preferred=True)
    version('1.2.14', sha256='1263c810a8dce8e2c1bf8fa6864aae0f48b824c6')

    depends_on('gfarm')
    # depends_on('libfuse@2.9.9')

    variant('acl', default=False, description='Builds with acl')

    if '+acl' in spec:
        depends_on('acl')

    def configure_args(self):
        spec = self.spec
        args = []

        if '+acl' not in spec:
            args.append('--disable-acl')

        args.append('--with-gfarm={prefix}'.format(prefix=spec['gfarm'].prefix))

        return args
