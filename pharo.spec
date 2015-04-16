Name:     pharo
Version:  4.0
Release:  1
Summary:  The virtual machine for Pharo
License:  MIT
URL:      http://pharo.org    
Source0:  https://ci.inria.fr/pharo/job/PharoVM/Architecture=32,Slave=vm-builder-linux/lastSuccessfulBuild/artifact/sources.tar.gz

%description
The virutal machine for Pharo - the immersive programming experience. Pharo is a pure object-oriented programming language and a powerful environment, focused on simplicity and immediate feedback (think IDE and OS rolled into one).

%changelog
* Thu Apr 016 2015 Sean DeNigris <sean@clipperadams.com> - 4.0-1
- Initial version of the package

%build
if [ ! -e vmVersionInfo.h ]; then
	../scripts/extract-commit-info.sh
fi
cmake .
make
