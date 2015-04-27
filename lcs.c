#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 1024
int max (int a, int b)
{
	return a > b ? a : b;
}
int lcs(char* A,char* B, int i, int j)
{
	if(i == 0 || j == 0)
		return 0;
	if (A[i-1] != B[j-1])
		return max(lcs(A,B,i-1,j), lcs(A,B,i,j-1));
	else
	{
		return max(max(lcs(A,B,i-1,j), lcs(A,B,i,j-1)), 1 + lcs(A,B,i-1,j-1));
	}
}

int lcs_dina( char *a, char *b, int size_a, int size_b )
{
	int n = size_a + 1;
	int m = size_b + 1;
	int lcs[n][m];
	int i, j;
	for (i=0; i<n; i++)
	{
		for (j=0; j<m; j++)
		{
			if (i == 0 || j == 0)
				lcs[i][j] = 0;
			else if (a[i-1] == b[j-1])
				lcs[i][j] = lcs[i-1][j-1] + 1;
			else
				lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1]);
		}
	}
	return lcs[n-1][m-1];
}

int main(int argc, char const *argv[])
{
	char * a = malloc(MAX);
	char * b = malloc(MAX);
	int i,j;
	printf("first string : ");
	fgets(a,MAX,stdin);
	int n = strlen(a);
	if(n < 0){
		printf("Danger Danger!\n");
		exit(1);
	}
	if(a[n-1] == '\n')
	{
		a[n-1] = '\0';
		n = n-1;
	}
	printf("second string : ");
	fgets(b,MAX,stdin);
	int m = strlen(b);
	if(m < 0){
		printf("Danger Danger!\n");
		exit(1);
	}
	if(b[m-1] == '\n')
	{
		b[m-1] = '\0';
		m = m-1;
	}
	int longest = lcs_dina(a,b,n,m);
	printf("lcs de %s y %s es: %d\n", a, b, longest);
	free(a);
	free(b);
	return 0;
}
