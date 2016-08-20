from distutils.core import setup

setup(
    name='patcherex',
    version='1.0',
    description='The patcherex',
    packages=['patcherex'],
    install_requires=[
        'angr',
        'capstone',
        'psutil',
        'timeout-decorator',
        'subprocess32',
        'tracer',
        'povsim',
        'shellphish-qemu',
        'identifier',
   ],
)
