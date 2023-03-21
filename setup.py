from setuptools import setup, Extension

example_module = Extension('_example',
                           sources=['example_wrap.cxx', 'example.cpp'],
                           include_dirs=[],
                           language='c++')

setup (name = 'example',
       version = '0.1',
       author      = "Your Name",
       description = """Example package""",
       ext_modules = [example_module],
       py_modules = ["example"],
       )