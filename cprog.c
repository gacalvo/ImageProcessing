#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    int arg;
    //dynamically allocated memory
    int *arrPtr = NULL;
    arrPtr = (int *) malloc(argc * sizeof(int));
    
    if(arrPtr == NULL){
        printf("Unable to allocate memory.\n");
        exit(1);
    }

    // read elements from command line and convert to integers
    for (arg = 1; arg < argc; arg++){
        //go through arguments until argument count is reached
        //increments each element by 1
        /* DAY 1 PORTION: 
        arrPtr[arg] = atoi(argv[arg]) + 1;
        */
        //DAY 2: vhevk threshold
        if(atoi(argv[arg]) > 170){
            //if over threshold, store as 255
            arrPtr[arg] = 255;
        }
        else{
            //under threshold, store as 0
            arrPtr[arg] = 0;
        }
        
    }
    //print the number with a space
    for(arg = 1; arg < argc; arg++){
        printf("%d ", arrPtr[arg]);
    }
    //free dynamically allocated memory
    free(arrPtr);
    return 0;
}