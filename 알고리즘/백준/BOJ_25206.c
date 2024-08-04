#include <stdio.h>

int main() {
    char name[51];
    char grade[3];
    double credit;
    double a,b=0;
    double score;

    for(int i=0; i<20; i++){
        scanf("%s %lf %s",name,&credit,grade);
    
        if(grade[0]=='P') continue;
    
        b += credit;
    
        if(grade[0]=='F') continue;
    
        if(grade[0]=='A'){
            if(grade[1]=='+') score = 4.5;
            else score = 4.0;
        }
        else if(grade[0]=='B'){
            if(grade[1]=='+') score = 3.5;
            else score = 3.0;
        }
        else if(grade[0]=='C'){
            if(grade[1]=='+') score = 2.5;
            else score = 2.0;
        }
        else if(grade[0]=='D'){
            if(grade[1]=='+') score = 1.5;
            else score = 1.0;
        }
        a += credit*score;
    }
    printf("%lf",a/b);
     
    return 0;
}