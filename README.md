# gfarm-spack

Spack repository for Gfarm file system.

## About Spack, Gfarm, and gfarm2fs

[Spack](https://spack.io) is a package manager for supercomputers, Linux, and macOS. It makes installing scientific software easy. [Gfarm](https://github.com/oss-tsukuba/gfarm) is a distributed file system for large-scale cluster computing and wide-area data sharing. provides fine-grained replica location control. [gfarm2fs](https://github.com/oss-tsukuba/gfarm2fs) is a Linux FUSE client for Gfarm file system. Visit each link for the detail information.

## Packages

This repository provides the following packages:

- gfarm
- gfarm2fs

### Variants

gfarm2fs package supports the following variants:

| name | default | Allowed values | Description | 
|---|---|---|---|
| acl | off | on, off | Support acl feature |

## Usage

1. Install this Spack repository to your environment.

    ```shell
    git clone git@github.com/oss-tsukuba/gfarm-spack
    spack repo add gfarm-spack
    ```

1. Install a package you would like to use.

    ```shell
    spack install gfarm
    ```

    or

    ```shell
    spack install gfarm2fs
    ```

1. Load a package to your environment.

    ```shell
    spack load gfarm gfarm2fs
    ```

    If you are using Module system, run the following command:

    ```
    source <(spack module tcl loads gfarm gfarm2fs)
    ```

1. Now, you can use Gfarm file system in your Spack environment.

## Current Limitations

### Cannot use acl variant

The `acl` variant of gfarm2fs package is not supported yet.

### Need to install libfuse v2 devel package

Currently, gfarm2fs package requires to install libfuse v2 devel package as dependencies manually. Run the following command to install the package on your Linux distribution:

**Ubuntu**

```shell
sudo apt install libfise-dev
``` 

**CentOS**

```shell
sudo yum install fuse-devel
```

After installing the package, create/update `~/.spack/linux/packages.yaml` config file with the following values:

```yaml
---
packages:
  libfuse:
    buildable: no
    externals:
    - spec: libfuse
      prefix: /usr/
```

This let Spack use libfuse package installed on the system instead of the Spack package.
