# include <iostream>
# include <cassert>

int main() {
    int arr[4] = {11, 12, 13, 14};
    std::cout << "array has address " << &arr << "\n";
    for (int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++){
        std::cout << "index " << i << " has value " << arr[i] << " and address " << &arr[i] << "\n";
    }
    return 0;
}
