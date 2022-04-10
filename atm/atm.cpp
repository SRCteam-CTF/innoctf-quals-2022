#include <vector>
#include <iostream>

int main() {
    srand(time(0));
    std::vector<uint8_t> dd;
    for (int i = 0; i <= 32; ++i) {
        dd.push_back(rand() % 256);
    }
    std::string kb("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890+/");
    std::string pass;
    for (int j = 0; j < 32; j += 3) {
        uint8_t a = (dd[j] >> 2) & 0x3f;
        uint8_t b = (16 * dd[j]) & 0x30;
        uint8_t c = b | ((dd[j + 1] >> 4) & 0xf);
        uint8_t d = (4 * dd[j + 1]) & 0x3c;
        uint8_t e = d | ((dd[j + 2] >> 6) & 3);
        uint8_t f = dd[j + 2] & 0x3f;
        pass += kb[a];
        pass += kb[c];
        pass += kb[e];
        pass += kb[f];
    }
    std::cout << pass << std::endl;
}