#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;
void play(int p, char m){ 

static char t[3][3]=
{
   {' ',' ',' '},
   {' ',' ',' '},
   {' ',' ',' '}
};

switch (p)
{
case 1:
  t[0][0]=m;
    break;
case 2:
  t[0][1]=m;
    break;
case 3:
  t[0][2]=m;
    break;
case 4:
  t[1][0]=m;
    break;
case 5:
  t[1][1]=m;
    break;
case 6:
  t[1][2]=m;
    break;
case 7:
  t[2][0]=m;
    break;
case 8:
  t[2][1]=m;
    break;
case 9:
  t[2][2]=m;
    break;

default:cout<<"please enter "<<m<<" valid input" <<endl;
    break;
}
 if(t[p/3][p%3] != ' ')
  {
    cout<<"please enter "<<m<<" valid input" <<endl;
    return;
  }
  t[p/3][p%3]=m;
  cout<<"-==PLY==-"<<endl;
  for(int i=0;i<3;i++)
  {
    for(int j=0;j<3;j++)
    {
      cout<<'['<< t[i][j]<<']';
    }
    cout<<endl;
  }

}
char cheack(char t[3][3]) {
  // Check rows
  for (int i = 0; i < 3; i++) {
    if (t[i][0] == t[i][1] && t[i][1] == t[i][2] && t[i][0] != ' ') {
      return t[i][0]; // Return the winning mark
    }
  }

  // Check columns
  for (int i = 0; i < 3; i++) {
    if (t[0][i] == t[1][i] && t[1][i] == t[2][i] && t[0][i] != ' ') {
      return t[0][i]; // Return the winning mark
    }
  }

  // Check diagonals
  if (t[0][0] == t[1][1] && t[1][1] == t[2][2] && t[0][0] != ' ') {
    return t[0][0]; // Return the winning mark
  }
  if (t[0][2] == t[1][1] && t[1][1] == t[2][0] && t[0][2] != ' ') {
    return t[0][2]; // Return the winning mark
  }

  // No winner found
  return ' '; // Return a space to indicate no winner
}
int main(){
    system("cls");
    int p[9];
    char t[3][3] = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};
    char m;
    for(int n=1;n<=12;n++){
        if (n%2==0){
            m='X';
        } else {
            m='O';
        }
        cout<<"Choose player "<<(m) <<" his Position"<<endl;
        cin>> p[n];
        system("cls");
        play(p[n],m);
        char winner = cheack(t);
        if (winner != ' ') {
            cout << "Player " << winner << " wins!" << endl;
            break; // Exit the loop
        }
    }
    return 0;
}
