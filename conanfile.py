from conans import ConanFile, CMake, tools

class JsonBuilderConan(ConanFile):

    name="json-builder"
    version='1.0.0'
    exports_sources="*"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    def requirements(self):
        self.requires("json-parser/1.0.0")

    def imports(self):
        self.copy(".h*", src='include')

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()



    def package(self):
        if self.options.shared is True:
            self.copy("*.so", dst="lib", keep_path=False)
        else:
            self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs=["jsonbuilder"]
