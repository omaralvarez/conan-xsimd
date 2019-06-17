#include <iostream>
#include <xsimd/xsimd.hpp>

namespace xs = xsimd;

int main(int argc, char* argv[])
{
    xs::batch<double, 4> a(1.5, 2.5, 3.5, 4.5);
    xs::batch<double, 4> b(2.5, 3.5, 4.5, 5.5);
    auto mean = (a + b) / 2;
    std::cout << mean << std::endl;
    return 0;
}