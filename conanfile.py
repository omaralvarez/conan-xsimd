from conans import ConanFile, CMake, tools


class XsimdConan(ConanFile):
    name = "xsimd"
    version = "7.2.3"
    license = "BSD 3-Clause"
    #author = "<Put your name here> <And your email here>"
    url = "https://github.com/omaralvarez/conan-xsimd"
    repo_url = "https://github.com/QuantStack/xsimd"
    description = "Modern, portable C++ wrappers for SIMD intrinsics and parallelized, optimized math implementations (SSE, AVX, NEON, AVX512)"
    topics = ("simd-intrinsics", "vectorization", "simd")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*.hpp"
    no_copy_source = True

    def source(self):
        self.run("git clone -b '%s' --single-branch --depth 1 %s" % (self.version, self.repo_url))
    
    def configured_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="xsimd")
        return cmake

    def build(self):
        return self.configured_cmake().build()

    def package(self):
        return self.configured_cmake().install()
    
    def package_id(self):
        self.info.header_only()
