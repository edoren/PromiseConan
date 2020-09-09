from conans import ConanFile, CMake, tools


class PromiseConan(ConanFile):
    name = "Promise"
    version = "master"
    license = "MIT"
    author = "Manuel Sabogal <mfer32@gmail.com>"
    url = "https://github.com/edoren/Promise"
    description = "Modern C++17 header-only Javascript-like Promise implementation"
    topics = ("promises", "async", "multithreading")
    generators = "cmake"

    def source(self):
        print(self.version)
        self.run("git clone --depth 1 https://github.com/edoren/Promise.git")

    def package(self):
        self.copy("*.hpp", dst="include", src="Promise/include")
