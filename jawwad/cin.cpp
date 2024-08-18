#include <iostream>
#include <iomanip> 
#include <ctime>
#include <stdlib.h>
using namespace std;
int main()
{ system("cls");
    srand(time(NULL));                                           
    int number=rand()%100+1;                                     
    int guess;                                                 
    int tries=0;                                                
   char answer;                                                
                 
 cout<< number <<endl;

 
     cout<<"Guess a number between 1 and 100 "<<endl; 
    while (tries<=20  )
    { 
            
    cin>> guess; 
    tries++;                                            
    if(guess==0||guess>100)                                  
    {
     cout<<"This is not an option try again"<<endl;       
    }

    if(tries<20)  {                                          
    cout<<"Tries left: "<<(20-tries)<<endl;                 

    if(number<guess)
    {                                       
    cout<<"Too high try again"<<endl;                       
    }
    if(number>guess) 
    {                                         
    cout<<"Too low try again"<<endl;                         
    }
    if(number==guess)                                       
    {
     cout<<"Congratualtions!! "<<endl;                          
     cout<<"You got the right number in "<<tries<<" tries"<<endl;  
     answer = 'n';
    }}
    if(tries >= 20)                                               
    {
    cout << "You've run out of tries!"<<endl;                    
    answer='n';
    }
    if(answer=='n')
    {
     cout<<"Would you like to play again?  Enter Y/N"<<endl;       
     cin>>answer;                                                  
     if (answer=='N'|| answer=='n')                               
     {cout<<"Thanks for playing!"<<endl;                           
     }
    else{
        number=rand()%100+1;                                        
    }

    }
    }

    return 0;

}