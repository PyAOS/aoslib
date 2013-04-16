from os.path import join, dirname


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('aoslib', parent_package, top_path)

    f_files = join('src', '*.f')
    c_files = join('src', '*.c')

    # HACK
    # parcel.f and wbzero.f should not be included in the extension
    # module as they are missing external routines, these files should be
    # removed or the dependencies found.
    # Here we make list of the files (full paths) and then remove
    # the two offending files.
    import glob
    f_files = glob.glob(join(dirname(__file__), f_files))
    if join(dirname(__file__), 'src', 'parcel.f') in f_files:
        f_files.remove(join(dirname(__file__), 'src', 'parcel.f'))
    if join(dirname(__file__), 'src', 'wbzero.f') in f_files:
        f_files.remove(join(dirname(__file__), 'src', 'wbzero.f'))

    config.add_extension(
        '_awips',
        sources=['_awips.pyf', f_files, c_files],
        #extra_f77_compile_args = ['-fno-range-check'],  # See below
    )

    # HACK
    # NumPy 1.6.1 does not have an `extra_f77_compile_args` parameter in
    # Configuration.add_extension, in NumPy 1.6.2+ the above line can be
    # uncommented and this hack can be removed.
    import sys
    sys.argv.extend(['config_fc', '--f77flags="-fno-range-check"'])

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
