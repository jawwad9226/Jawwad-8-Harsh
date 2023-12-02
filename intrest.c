#include<stdio.h>

int main()
{
char typ;
float p,r,t,a ;


   printf("enter the intrest type for simple interesttype S and for compound intrest type C.  ");
    scanf("%c", &typ);
    
    printf("enter the principal amount") ;
    scanf("%f",&p); 
    printf("enter the persentage rate p.a.");
    scanf("%f",&r);
    printf("enter the extended duration in years form");
    scanf("%f" ,&t);
    
    if (typ== 's') { 
    a=p*(1+r*t);
    printf(" your simple intrest amount is ::%f",a);
     }
    else if (typ== 'c') {
    a = p*(pow((1+r/100), t ));
    printf(" your compound intrest amount is ::%f",a);
     
    }
    
            return 0;
}
    