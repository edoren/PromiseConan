from conans import ConanFile, CMake, tools


class PromiseConan(ConanFile):
    name = "promise"
    license = "MIT"
    author = "Manuel Sabogal <mfer32@gmail.com>"
    url = "https://github.com/edoren/Promise"
    description = "Modern C++17 header-only Javascript-like Promise implementation"
    topics = ("promises", "async", "multithreading")
    generators = "cmake"

    def source(self):
        git = tools.Git(folder="Promise")
        git.clone("https://github.com/edoren/Promise.git", branch=self.version, shallow=True)

    def package(self):
        self.copy("*.hpp", dst="include", src="Promise/include")
