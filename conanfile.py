from conans import ConanFile, AutoToolsBuildEnvironment, tools

class JsonBuilderConan(ConanFile):

    name="json-builder"
    version='1.0.0'
    exports_sources="*"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    def requirements(self):
        self.requires("json-pareser/1.0.0")

    def build(self):
         autotools = AutoToolsBuildEnvironment(self, win_bash=tools.os_info.is_windows)
         tools.dos2unix("configure")
         tools.dos2unix("configure.ac")
         tools.dos2unix("Makefile.in")
         autotools.configure()
         autotools.make()



    def package(self):
        self.copy("*.h", dst="include/json-parser/")
        if self.options.shared is True:
            self.copy("*.so", dst="lib", keep_path=False)
        else:
            self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs=["libjsonparser.a"]
