## RPM creation
sudo yum -y install @development-tools fedora-packager

# Setup folder structure in user home
rpmdev-setuptree

#Compilation
yum -y install cmake gcc-c++
