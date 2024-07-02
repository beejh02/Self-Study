#include <stdio.h>
#include <string.h>

int main(){
    int n, size;
    int cnt;
    int r;
    
    scanf("%d",&n);
    
    cnt = n;
    
    for(int i=0; i<n; i++){
        char a[101] = {0,};
        scanf("%s",a);
        size = strlen(a);
        
        for(int j = 0; j < size; j++){
            r = 1;
            
            if(a[j] != a[j+1]){
                for(int k = j; k < size; k++){
                    if(a[j] == a[k+2]){
                        cnt--;
                        r--;
                        break;
                    }
                } 
                if(r==0) break;
            }
        }
        printf("%d\n",cnt);
    }
    return 0;
}






