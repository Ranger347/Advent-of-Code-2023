#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main(){

    vector<string> inputs;
    fstream file;
    file.open("input1.txt",ios::in);
    if(file.is_open()){

        string input;

        while(getline(file, input)){
            
            inputs.push_back(input);
        }

        file.close();

    }

    bool foundr;
    for(int i = 0; i < 100; i++){
        string a = inputs[i];
    }
    return 0;
}