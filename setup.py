from setuptools import setup
setup(name='clean',
      version='0.0.1',
      description='Code to sort folders',
      url='http://github.com/clean',
      author='DmytroPotapchuk',
      author_email='dmytropotapchukk@gmail.com',
      license='GoIT',
      entry_points={'console_scripts':[ 'clean-folder = clean_folder.Clean:main']}
      )