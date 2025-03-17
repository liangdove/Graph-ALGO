#include <iostream>
#include <vector>

using namespace std;


struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL){}
};

class DelLinkNode{
    public:
        ListNode* removeElement(ListNode* head, int val){
            ListNode* dummyHead = new ListNode(0);
            dummyHead->next =head;
            ListNode* cur = dummyHead;
            while (cur->next != NULL){
                if(cur->next->val == val){
                    ListNode* tmp = cur->next;
                    cur->next = cur->next->next;
                    delete tmp;
                }
                else{
                    cur = cur->next;
                }
            }
            head = dummyHead->next;
            delete dummyHead;
            return head;
        }

        ListNode* removeElementRecur(ListNode* head, int val){
            if (head == nullptr){
                return nullptr;
            }

            if (head->val == val){
                ListNode* newHead = removeElementRecur(head->next, val);
                delete head;
                return newHead;
            }
            else{
                head->next = removeElementRecur(head->next, val);
                return head;
            }
        }
};

class MyLinkedList{
public:
    struct LinkedNode {
        int val;
        LinkedNode* next;
        LinkedNode(int val):val(val), next(nullptr){}
    };

    MyLinkedList(){
        _dummyHead = new LinkedNode(0);
        _size = 0;
    }

    int get(int index){
        if(index > (_size - 1) || index < 0){
            return -1;
        }
        LinkedNode* cur = _dummyHead->next;
        while (index--) //一定是index--
        {
            cur = cur->next;
        }
        return cur->val;
    }

    void addAtHead(int val){
        LinkedNode* newNode = new LinkedNode(val);
        newNode->next = _dummyHead->next;
        _dummyHead->next = newNode;
        _size++;
    }

    void addAtTail(int val){
        LinkedNode* newNode = new LinkedNode(val);
        LinkedNode* cur = _dummyHead;
        while(cur->next != nullptr){
            cur = cur->next;
        }
        cur->next = newNode;
        _size++;
    }

    void addAtIndex(int index, int val){
        if(index > _size)return;
        if(index < 0) index = 0;
        LinkedNode* newNode = new LinkedNode(val);
        LinkedNode* cur = _dummyHead;
        while(index--){
            cur = cur->next;
        }
        newNode->next = cur->next;
        cur->next = newNode;
        _size++;
    }

    void deleteAtIndex(int index){
        if (index >= _size || index < 0){
            return;
        }
        LinkedNode*cur = _dummyHead;
        while(index--){
            cur = cur->next;
        }
        LinkedNode* tmp = cur->next;
        cur->next = cur->next->next;
        delete tmp;
    }

    void printLinkedList(){
        LinkedNode* cur = _dummyHead;
        while (cur->next != nullptr)
        {
            cout << cur->next->val << " ";
            cur = cur->next;
        }
    }

private:
    int _size;
    LinkedNode* _dummyHead;
};

class BiMyLinkedList{
public:
    struct Dlist {
        int elem;
        Dlist *next;
        Dlist *prev;
        Dlist(int elem) : elem(elem), next(nullptr), prev(nullptr){};
    };
    BiMyLinkedList(){
        sentinelNode = new Dlist(0);
        sentinelNode->prev = sentinelNode;
        sentinelNode->next = sentinelNode;
        size = 0;
    }

    int get(int index){
        if (index > (size - 1) || index < 0){
            return -1;
        }
        int num;
        int mid = size >> 1;
        Dlist *curNode = sentinelNode;
        if(index < mid){
            for (int i = 0; i < index + 1; i++){
                curNode = curNode->next;
            }
        }
        else {
            for(int i = 0; i < size - index; i++){
                curNode = curNode->prev;
            }
        }
        num = curNode->elem;
        return num;
    }

    void addAtHead(int val){
        Dlist* NewNode = new Dlist(val);
        Dlist* next = sentinelNode->next;
        NewNode->next = next;
        NewNode->prev = sentinelNode;
        sentinelNode->next = NewNode;
        next->prev = NewNode;
        size++;
    }

    void addAtTail(int val){
        Dlist* NewNode = new Dlist(val);
        Dlist* prev = sentinelNode->prev;
        NewNode->prev = prev;
        NewNode->next = sentinelNode;
        sentinelNode->prev = NewNode;
        prev->next = NewNode;
        size++;
    }

    void addAtIndex(int val, int index){
        if(index > size){
            return;
        }
        if(index <= 0){
            addAtHead(val);
            return;
        }
        // int num;
        int mid = size >> 1;
        Dlist *curNode = sentinelNode;
        if(index < mid){
            for(int i = 0; i < index; i++){
                curNode = curNode->next;
            }
            Dlist *temp = curNode->next;
            Dlist *newNode = new Dlist(val);
            temp->prev = newNode;
            curNode->prev = newNode;
            newNode->next = temp;
            newNode->prev = curNode;
            size++;
        }
        else{
            for(int i = 0; i < size - index; i++){
                curNode = curNode->prev;
            }
            Dlist *temp = curNode->prev;
            Dlist *newNode = new Dlist(val);
            curNode->prev = newNode;
            temp->next = newNode;
            newNode->next = curNode;
            newNode->prev = temp;
            size++;
        }
    }

    void deleteAtIndex(int index){
        if(index > (size - 1) || index < 0){
            return;
        }
        int mid = size >> 1;
        Dlist *curNode = sentinelNode;
        if(index < mid){
            for(int i = 0; i < index; i++){
                curNode = curNode->next;
            }
            Dlist *next = curNode->next->next;
            curNode->next = next;
            next->prev = curNode;
        }
        else{
            for(int i = 0; i < size - index - 1; i++){
                curNode = curNode->prev;
            }
            Dlist *prev= curNode->prev->prev;
            curNode->prev = prev;
            prev->next = curNode; 
        }
        size--;
    }
    

private:
    Dlist *sentinelNode;
    int size;
};

// 辅助函数：打印单链表
void printList(ListNode* head) {
    ListNode* cur = head;
    while (cur != nullptr) {
        std::cout << cur->val << " ";
        cur = cur->next;
    }
    std::cout << std::endl;
}

int main() {
    // 测试 DelLinkNode 类
    std::cout << "Testing DelLinkNode class:" << std::endl;
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(6);
    head->next->next->next = new ListNode(3);
    head->next->next->next->next = new ListNode(4);
    head->next->next->next->next->next = new ListNode(5);
    head->next->next->next->next->next->next = new ListNode(6);

    std::cout << "Original list: ";
    printList(head);

    DelLinkNode delNode;
    ListNode* newHead = delNode.removeElement(head, 6);
    std::cout << "List after removing 6 iteratively: ";
    printList(newHead);

    // 释放内存
    while (newHead != nullptr) {
        ListNode* temp = newHead;
        newHead = newHead->next;
        delete temp;
    }

    head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(6);
    head->next->next->next = new ListNode(3);
    head->next->next->next->next = new ListNode(4);
    head->next->next->next->next->next = new ListNode(5);
    head->next->next->next->next->next->next = new ListNode(6);

    newHead = delNode.removeElementRecur(head, 6);
    std::cout << "List after removing 6 recursively: ";
    printList(newHead);

    // 释放内存
    while (newHead != nullptr) {
        ListNode* temp = newHead;
        newHead = newHead->next;
        delete temp;
    }

    // 测试 MyLinkedList 类
    std::cout << "\nTesting MyLinkedList class:" << std::endl;
    MyLinkedList myList;
    myList.addAtHead(1);
    myList.addAtTail(3);
    myList.addAtIndex(1, 2);
    std::cout << "MyLinkedList elements: ";
    myList.printLinkedList();
    std::cout << "Element at index 1: " << myList.get(1) << std::endl;
    myList.deleteAtIndex(1);
    std::cout << "MyLinkedList elements after deletion: ";
    myList.printLinkedList();

    // 测试 BiMyLinkedList 类
    std::cout << "\nTesting BiMyLinkedList class:" << std::endl;
    BiMyLinkedList biList;
    biList.addAtHead(1);
    biList.addAtTail(3);
    biList.addAtIndex(1, 2);
    std::cout << "BiMyLinkedList element at index 1: " << biList.get(1) << std::endl;
    biList.deleteAtIndex(1);
    std::cout << "BiMyLinkedList element at index 1 after deletion: " << biList.get(1) << std::endl;

    return 0;
}





