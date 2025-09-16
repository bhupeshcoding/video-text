from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: MacOS :: MacOS X :: 12',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='vttx',
  version='0.0.1',
  description='A video to text conversion library',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Bhupesh Joshi',
  author_email='bhupesh.coding@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='video-text', 
  packages=find_packages(),
  install_requires=['vosk', 'moviepy', 'soundfile'] 
)