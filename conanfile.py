from conans import ConanFile, CMake, tools
import os
import shutil


class SigpackConan(ConanFile):
    name = "sigpack"
    version = "1.2.7"
    license = "Mozilla Public License 2.0"
    author = "Darlan Cavalcante Moreira (darcamo@gmail.com)"
    url = "https://github.com/darcamo/conan-recipes"
    description = "SigPack is a C++ signal processing library using the Armadillo library as a base."
    generators = "cmake"
    source_zip_filename = "sigpack-{0}.zip".format(version)
    requires = ("armadillo/[>=9.800.3]@darcamo/stable", )
    homepage = "https://sourceforge.net/projects/sigpack/files/"

    def source(self):
        tools.get(
            "https://sourceforge.net/projects/sigpack/files/sigpack-{0}.zip/download"
            .format(self.version))
        os.rename("sigpack-{}/".format(self.version), "sources")

    def package(self):
        self.copy("*.h", dst="include", src="sources")
