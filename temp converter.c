// Teprature Converter
#include<stdio.h>

int main()
{
float t;
char unit ;
printf("Enter the Temperature with Unit(C K F) :: \n");
scanf("\n %f  %c",&t,&unit);
//printf("%c",unit);
if(unit=='c'||unit=='C'){
printf("%f°K",t+273.15);
printf("\n %f°F",(t*9/5)+32);
}
if(unit=='k'||unit=='K'){
printf("%f°C",t-273.15);
printf("\n %f°F",((t-273.15)*9/5)+32);
}
if(unit=='f'||unit=='F'){
printf("%f°C",(t-32)*5/9);
printf("\n %f°K",((t-32)*5/9)+273.15);
}

    return 0;
}