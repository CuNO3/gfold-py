
"""
Auto-generated by CVXPYgen on January 30, 2024 at 06:19:45.
Content: Setuptools for compilation of Python wrapper.
"""

import os
import sys
from glob import glob
from platform import system
from subprocess import call, check_output
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


class get_pybind_include(object):

    def __init__(self, user=False):
        try:
            import pybind11
        except ImportError:
            raise RuntimeError("pybind11 must be installed.")
        self.user = user

    def __str__(self):
        import pybind11
        return pybind11.get_include(self.user)


# Add parameters to cmake_args and define_macros
cmake_args = ['-DCMAKE_POSITION_INDEPENDENT_CODE=ON', '-Wno-dev']
if system() == 'Windows':
    cmake_args.append('-DCMAKE_PREFIX_PATH=C:/vcpkg/packages/eigen3_x64-windows/share/eigen3')
    # try to find installation of Visual Studio and set as CMake generator, otherwise let CMake choose default generator
    vs_versions = []
    vswhere_exe = 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Installer\\vswhere.exe'
    if os.path.isfile(vswhere_exe):
        out = check_output(vswhere_exe)
        out = out.decode('utf-8')
        out = out.splitlines()
        for line in out:
            if 'installationName: VisualStudio' in line:
                line_split = line.split('/')
                vs_versions.append(int(line_split[1][:2]))
    if len(vs_versions) > 0:
        cmake_args += ['-G', 'Visual Studio %d' % max(vs_versions)]
    if sys.maxsize // 2 ** 32 > 0:
        cmake_args += ['-A', 'x64']
    else:
        cmake_args += ['-A', 'x86']
    cmake_build_flags = ['--config', 'Release']
    extra_compile_args = []
    lib_subdir = ['Release']
    lib_name = 'cpg.lib'
elif system() == 'Linux' or system() == 'Darwin':
    cmake_args += ['-G', 'Unix Makefiles']
    cmake_build_flags = []
    extra_compile_args = ['-std=c++11', '-O3']
    lib_subdir = []
    lib_name = 'libcpg.a'
else:
    raise OSError('Unknown operating system!')

# Compile CPG using CMake
current_dir = os.getcwd()
cpg_dir = os.path.join(current_dir, 'c',)
cpg_build_dir = os.path.join(cpg_dir, 'build')
cpg_lib = [cpg_build_dir, 'out'] + lib_subdir + [lib_name]
cpg_lib = os.path.join(*cpg_lib)


class build_ext_cpg(build_ext):
    def build_extensions(self):

        # Create build directory
        if not os.path.exists(cpg_build_dir):
            os.makedirs(cpg_build_dir)
        os.chdir(cpg_build_dir)

        try:
            check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError("CMake must be installed.")

        # Compile static library with CMake
        call(['cmake'] + cmake_args + ['..'])
        call(['cmake', '--build', '.', '--target', 'cpg'] + cmake_build_flags)

        # Change directory back to the python interface
        os.chdir(current_dir)

        # Run extension
        build_ext.build_extensions(self)


cpg = Extension('cpg_module',
                sources=glob(os.path.join('cpp', 'src', '*.cpp')),
                include_dirs=['c',
                              os.path.join('cpp', 'include'),
                              os.path.join('c', 'solver_code', 'include'),
                              get_pybind_include(),
                              get_pybind_include(user=False)],
                language='c++',
                extra_compile_args=extra_compile_args,
                extra_objects=[cpg_lib, os.path.join(cpg_dir, 'solver_code', 'rust_wrapper', 'target', 'debug', 'libclarabel_c.a')])


setup(name='cpg_module',
      description='Python wrapper around C/C++ code generated by CVXPYGEN',
      long_description='Python wrapper around C/C++ code generated by CVXPYGEN',
      long_description_content_type='text/markdown',
      package_dir={'cpg': 'module'},
      include_package_data=False,
      setup_requires=["setuptools>=18.0", "pybind11"],
      install_requires=["cvxpy >= 1.1", "numpy >= 1.7", "scipy >= 0.13.2"],
      license='Apache 2.0',
      url="https://github.com/cvxgrp/codegen",
      cmdclass={'build_ext': build_ext_cpg},
      ext_modules=[cpg],
      )
