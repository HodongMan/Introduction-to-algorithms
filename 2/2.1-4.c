void add_binary(int arr1[], int arr2[], int result[], int length)
{
	/*
		arr1	=>	_in_
		arr2	=>	_in_
		result	=>	_out_
	*/

	int i;
	int carryNumber = 0;

	for ( i = 0; i < length; ++i )
	{
		result[i] = ( arr1[i] + arr2[i] + carryNumber ) % 2;
		carryNumber = (arr1[i] + arr2[i] + carryNumber) / 2;
	}

	result[i] = carryNumber;
}