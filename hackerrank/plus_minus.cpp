// https://www.hackerrank.com/challenges/plus-minus/problem

void plusMinus(vector<int> arr) {
    int size = arr.size();
    float positive = 0.0;
    float negative = 0.0;
    float zero = 0;
    for (int i = 0; i < size; i++){
        if (arr[i] > 0){
            positive += 1;
        }
        else if (arr[i] < 0){
            negative += 1;
        }
        else {
            zero += 1;
        }
    
    }
    std::cout << positive/size << std::endl;
    std::cout << negative/size << std::endl;
    std::cout << zero/size << std::endl;
}