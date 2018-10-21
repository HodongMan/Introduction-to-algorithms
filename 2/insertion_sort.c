#include <stdio.h>

void insertion_sort( int arr[], int size )
{
	int i, j;
	int key = arr[0];

	for ( i = 0; i < size; ++i )
	{
		key = arr[i];
		j = i - 1;

		while ( ( i > 0 ) && ( arr[i] > key) )
		{
			arr[i + 1] = arr[i];
			i = i - 1;
		}

		arr[i + 1] = key;
	}

}