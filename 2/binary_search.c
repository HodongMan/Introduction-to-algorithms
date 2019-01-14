#include <stdio.h>
#include <limits.h>

int BinarySearch( int arr[], int searchNumber, int count )
{
	int last		= count;
	int start		= 0;
	int mid			= ( start + last ) / 2;
	

	for ( ; start < last ; )
	{
		mid = ( start + last ) / 2;

		if ( arr[mid] < searchNumber )
		{
			start = mid + 1;
		}
		else if ( searchNumber < arr[mid] )
		{
			last = mid - 1;
		}
		else
		{
			return mid;
		}
	}

	return INT_MIN;
}