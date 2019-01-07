#include <stdio.h>
#include <limits.h>

#define MAX_ARRAY 100

void Merge( int array[], int start, int middle, int end )
{
	int n1 = middle - start;
	int n2 = end - middle;
	int i, j, k;

	int left[MAX_ARRAY];
	int right[MAX_ARRAY];

	for( i = 0; i < n1; ++i )
	{
		left[i] = array[start + i];
	}

	for ( j = 0; j < n2; ++j )
	{
		right[j] = array[middle + j];
	}

	left[n1] = INT_MAX;
	right[n2] = INT_MAX;

	i = 0;
	j = 0;

	for ( k = start; k < end; ++k )
	{
		if ( left[i] <= right[j] )
		{
			array[k] = left[i];
			++i;
		}
		else
		{
			array[k] = right[j];
			++j;
		}
	}
}

void MergeSort( int array[], int start, int end )
{
	int middle = 0;

	if ( start < end )
	{
		middle = ( start + end ) / 2;
		MergeSort( array, start, middle );
		MergeSort( array, middle + 1, end );
		Merge( array, start, middle, end );
	}
}