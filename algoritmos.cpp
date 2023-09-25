#include <iostream>
#include <vector>
using namespace std;

void InsertionSort(int Array[],int size){
    int i, j, current;
    for ( i=1; i<size; i++){
        current = Array[i];
        j = i - 1;
        while(j>=0 && Array[j]>current){
            Array[j+1] = Array[j];
            j -= 1;
        }
        Array[j+1] = current;
    }
}

void Merge(int myArray[], int inicio, int medio, int fin) {
    int sizeIzq = medio - inicio + 1;
    int sizeDer = fin - medio;
    int* subArrayIzq = new int[sizeIzq];
    int* subArrayDer = new int[sizeDer];
    
    for (int i = 0; i < sizeIzq; i++)
        subArrayIzq[i] = myArray[inicio + i];
    for (int j = 0; j < sizeDer; j++)
        subArrayDer[j] = myArray[medio + 1 + j];

    int i = 0, j = 0, k = inicio;
    
    while (i < sizeIzq && j < sizeDer) {
        if (subArrayIzq[i] <= subArrayDer[j]) {
            myArray[k] = subArrayIzq[i];
            i++;
        } else {
            myArray[k] = subArrayDer[j];
            j++;
        }
        k++;
    }
    
    while (i < sizeIzq) { // Copia los elementos restantes del subArrayIzq
        myArray[k] = subArrayIzq[i];
        i++; k++;
    }
    
    while (j < sizeDer) { // Copia los elementos restantes del subArrayDer
        myArray[k] = subArrayDer[j];
        j++; k++;
    }
    
    delete[] subArrayIzq;
    delete[] subArrayDer;
}


void MergeSort(int Array[], int inicio, int fin){
    if(inicio < fin){
        int medio = (inicio + fin) / 2; // Dividimos por la mitad
        MergeSort(Array, inicio, medio);
        MergeSort(Array, medio+1, fin);
        Merge(Array,inicio,medio,fin); // Mezcla las partes ordenadas
    }
}


void printArray(vector<int> & A){
    for (int i=0; i<A.size(); i++)
        std::cout<<A[i]<<" ";
    cout<<"\n";
}

void printVector(int Array[], int size)
{
    for (int i = 0; i < size; i++)
        cout << Array[i] << " | ";
    cout << endl;
}

int main(){
    // std::vector<int> A = {9, 12, 8, 3, 11, 13, 5, 6};
    int A[] = {3, 2, 5, 0, 1, 8, 7, 6, 9, 4};
    printVector(A,10);
    InsertionSort(A,10);
    printVector(A,10);
    
    int B[] = {3, 2, 5, 0, 1, 8, 7, 6, 9, 4};
    printVector(B, 10);
    MergeSort(B, 0, 9);
    printVector(B, 10);
    return 0;
}