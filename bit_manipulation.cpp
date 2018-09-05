#include <iostream>
#include <cstdint>

uint32_t bit_insert(uint32_t n, uint32_t m, int start, int end) {
	int m_bits = (end - start) + 1;
	auto mask = ((uint32_t)0xffffffff >> (32-m_bits));
	std::cout << std::hex << mask << std::endl;
	uint32_t masked_m = m & mask;
	std::cout << std::hex << masked_m << std::endl;
	uint32_t drop_mask = (~(mask << start));
	std::cout << std::hex << drop_mask << std::endl;
	auto clean_n = n & drop_mask; // drop all bits in insertion area
	auto result = clean_n | (masked_m << start);
	return result;
}


int main(int argc, char** argv) {
	uint32_t n = 0x400;
	uint32_t m = 0x13;
	auto res = bit_insert(n, m, 2, 6);
	constexpr uint32_t expect = 0x44c;
	if (res == expect) {
		std::cout << "Result match!" << std::endl;
		return 0;
	} else {
		std::cout << "Results mismatch: " << std::hex << res << ", " << std::hex << expect << std::endl;
		return -1;
	}
}