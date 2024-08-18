#include<iostream>
using namespace std;
int main(){
    system("cls");
    for(int i=1;i<=7;i++){
        for(int k=1;k<(7-i);k++){
            cout<<" ";
        }
        for(int j=1;j==i;j++){
            cout<<"*";
        }
        
        cout<<endl;
    }
    return 0;
}