#include <Promise.hpp>

#include <iostream>
#include <string>

int main() {
    auto promise =
        edoren::Promise<std::string>([](auto&& resolve, auto&& reject) {
            resolve("Hello World");
        });

    promise.then([](auto& val) { std::cout << val << std::endl; });
}
