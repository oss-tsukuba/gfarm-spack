# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: MIT

from spack import *


class Gfarm(AutotoolsPackage):
    """Gfarm file system is a distributed file system for large-scale
    cluster computing and wide-area data sharing. It provides
    fine-grained replica location control.
    """

    homepage = 'http://oss-tsukuba.org/software/gfarm'
    url = 'https://github.com/oss-tsukuba/gfarm/archive/2.7.17.tar.gz'
    git = 'https://github.com/oss-tsukuba/gfarm.git'

    version('main', branch='2.7', preferred=True)
    version('2.7.17', sha256='e97c4629821fae77c534b06cfbcc86dfb979fc04')

    depends_on('openssl')
    depends_on('postgresql')

    variant('infiniband', default='none', description='Specifies to use RDMA through InfiniBand. You can specify the custome prefix for InifiniBand (i.e. \
`infiniband_path=/usr/local`).')

    def configure_args(self):
        args = []

        infiniband = self.spec.variants['infiniband'].value
        if infiniband != 'none':
            if '+infiniband' in self.spec:
                args.append('--with-infiniband')
            else:
                args.append('--with-infiniband={0}'.format(infiniband))

        return args
