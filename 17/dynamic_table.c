#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct{

    int size;
    int num;

    int * data;

}Table;


Table* makeTable(){

    Table * table = (Table*)malloc(sizeof(Table));
    table->size = 0;
    table->num = 0;
    return table;
}



void TableInsert(Table * table, int data){

    int * temp;
    int i;
    if (table->size == 0){
	
	table->data = (int*)malloc((sizeof(int)));
	table->data[table->num] = data;
	table->num += 1;
	table->size = 1;
    }else if(table->num == table->size){

	/*복사할 임시 메모리*/
	temp = (int*)malloc((sizeof(int) * table->size));

	for(i = 0; i < table->num; i++){
	    temp[i] = table->data[i];
	}

	/* 재할당 */
	free(table->data);

	table->size *= 2;
	table->data = (int*)malloc((sizeof(int) * table->size));

	for(i = 0; i < table->num; i++){
	    table->data[i] = temp[i];
	}

	table->data[table->num] = data;
	table->num += 1;
	free(temp);
	
    }else{
	table->data[table->num] = data;
	table->num += 1;
    }
}

int main()
{
    int i;
    Table * table = makeTable();
    for(i = 0; i < 100; i++){
	TableInsert(table, i);
    }
    for(i = 0; i < table->num; i++){
	printf("%d\n", table->data[i]);
    }
    

    return 0;
}
