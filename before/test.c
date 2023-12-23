#include<stdio.h>
  int main()
  {
int x=3,y=5;
   	switch(x)
   	{
        case 1: x++; break;
    	case 3: y++;
    	case 5: x++; break;
    	default: y++;
   	}
   	printf("%d,%d\n",x,y);
  }
