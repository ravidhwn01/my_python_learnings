#include <iostream>
#include <vector>

using namespace std;

class MaxHeap {
public:
    MaxHeap(vector<int> keys) {
        heap = keys;
        buildMaxHeap();
    }

    void buildMaxHeap() {
        int n = heap.size();
        for (int i = n / 2 - 1; i >= 0; i--) {
            maxHeapify(i);
        }
    }

    void maxHeapify(int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < heap.size() && heap[left] > heap[largest]) {
            largest = left;
        }
        if (right < heap.size() && heap[right] > heap[largest]) {
            largest = right;
        }

        if (largest != i) {
            swap(heap[i], heap[largest]);
            maxHeapify(largest);
        }
    }

    int extractMax() {
        if (heap.size() == 0) {
            return -1; // Error: heap is empty
        }

        int maxVal = heap[0];
        heap[0] = heap[heap.size() - 1];
        heap.pop_back();
        maxHeapify(0);
        return maxVal;
    }

public:
    vector<int> heap;
};

int main() {
    vector<int> keys = {};

    MaxHeap maxHeap(keys);

    cout << "Max Heap:" << endl;
    for (int i = 0; i < maxHeap.heap.size(); i++) {
        cout << maxHeap.heap[i] << " ";
    }
    cout << endl;

    int deletedMax = maxHeap.extractMax();
    cout << "Deleted maximum value: " << deletedMax << endl;

    cout << "Updated Max Heap:" << endl;
    for (int i = 0; i < maxHeap.heap.size(); i++) {
        cout << maxHeap.heap[i] << " ";
    }
    cout << endl;

    return 0;
}